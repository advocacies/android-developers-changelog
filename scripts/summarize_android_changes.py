#!/usr/bin/env python3
"""
Summarize changes in Android Developers documentation.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime, timezone
import json
import logging
from dotenv import load_dotenv
import subprocess
import re

load_dotenv(override=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).parent.parent
DOCS_DIR = ROOT_DIR / 'docs'
CHANGELOG_JSON = ROOT_DIR / 'pages' / 'changelog.json'

PREVIEW_MAX_CHARS = 300

def get_git_diff(file_path, commit_hash=None):
    """Get the git diff for a file."""
    try:
        if commit_hash:
            result = subprocess.run(
                ['git', 'diff', f'{commit_hash}^', commit_hash, '--', file_path],
                capture_output=True, text=True, check=False
            )
            return result.stdout

        result = subprocess.run(
            ['git', 'diff', '--cached', file_path],
            capture_output=True, text=True, check=False
        )
        if result.stdout.strip():
            return result.stdout

        result = subprocess.run(
            ['git', 'diff', file_path],
            capture_output=True, text=True, check=False
        )
        return result.stdout
    except Exception as e:
        logger.error(f"Failed to get diff for {file_path}: {e}")
        return None

def extract_title_from_content(content, filename, url=None):
    """Extract actual document title from markdown frontmatter, H1 or live URL."""
    if content:
        title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            if not title.startswith('http'):
                return title

        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()

    if url:
        try:
            import urllib.request
            import html
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                html_text = response.read().decode('utf-8', errors='ignore')
                title_match = re.search(r'<title>(.*?)</title>', html_text, re.IGNORECASE)
                if title_match:
                    title = html.unescape(title_match.group(1)).strip()
                    title = title.split('|')[0].strip()
                    title = title.split('&')[0].strip()
                    return title if title else filename
        except Exception:
            pass

    return filename

def strip_frontmatter(content):
    if content.startswith('---'):
        end = content.find('\n---', 3)
        if end != -1:
            return content[end + 4:]
    return content

def is_skippable_line(line):
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith('#'):
        return True
    # Lines that are only images / image-links / standalone links
    if re.fullmatch(r'(\[!\[.*?\]\(.*?\)\]\(.*?\)|!\[.*?\]\(.*?\)|\[.*?\]\(.*?\))(\s*)', stripped):
        return True
    return False

def extract_preview(content):
    """Extract the first meaningful paragraph from markdown as a short preview."""
    if not content:
        return ""

    body = strip_frontmatter(content)
    paragraph_lines = []
    for raw_line in body.splitlines():
        if is_skippable_line(raw_line):
            if paragraph_lines:
                break
            continue
        paragraph_lines.append(raw_line.strip())

    paragraph = ' '.join(paragraph_lines).strip()
    if len(paragraph) > PREVIEW_MAX_CHARS:
        paragraph = paragraph[:PREVIEW_MAX_CHARS].rstrip() + '…'
    return paragraph

def load_changelog():
    if not CHANGELOG_JSON.exists():
        return []
    try:
        return json.loads(CHANGELOG_JSON.read_text(encoding='utf-8'))
    except:
        return []

def save_changelog(data):
    CHANGELOG_JSON.parent.mkdir(exist_ok=True)
    CHANGELOG_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

def get_commit_date(commit_hash):
    """Get the commit date in ISO 8601 format."""
    try:
        iso_date = subprocess.check_output(
            ['git', 'show', '-s', '--format=%cI', commit_hash],
            text=True
        ).strip()
        return iso_date
    except Exception as e:
        logger.warning(f"Failed to get commit date for {commit_hash}: {e}")
        return datetime.now(timezone.utc).isoformat()

def update_json_data(updates, commit_hash=None):
    if not updates:
        return load_changelog()

    history = load_changelog()

    if commit_hash:
        date_str = get_commit_date(commit_hash)
    else:
        date_str = datetime.now(timezone.utc).isoformat()

    new_entry = {
        "date": date_str,
        "commit_hash": commit_hash,
        "entries": updates
    }

    history.insert(0, new_entry)
    save_changelog(history)
    return history

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--commit-hash', default=None)
    args = parser.parse_args()

    if not args.files:
        return

    updates = []
    base_url = "https://developer.android.com"

    for file_arg in args.files:
        if ':' in file_arg:
            status, file_path = file_arg.split(':', 1)
        else:
            status, file_path = 'M', file_arg

        filename = os.path.basename(file_path)
        if not filename.endswith('.md'):
            continue

        logger.info(f"Processing {filename} (Status: {status})...")

        tag_text = "UPDATE"
        tag_class = "update"
        if status == 'A':
            tag_text = "NEW"
            tag_class = "new"
        elif status == 'D':
            tag_text = "DELETE"
            tag_class = "delete"

        rel_path = file_path
        if 'docs/' in rel_path:
             rel_path = rel_path.split('docs/', 1)[1]

        url_path = rel_path.replace('.md', '')
        url = f"{base_url}/{url_path}"

        if status == 'D':
            updates.append({
                'title': filename,
                'summary': "Documentation has been removed.",
                'tag_text': tag_text,
                'tag_class': tag_class
            })
            continue

        doc_title = filename
        full_content = ""
        try:
            full_content = Path(file_path).read_text(encoding='utf-8')
            doc_title = extract_title_from_content(full_content, filename, url)
        except Exception as e:
            logger.warning(f"Failed to read full content for {file_path}: {e}")

        diff_content = get_git_diff(file_path, args.commit_hash)

        if status == 'M' and not diff_content:
            continue
        if status == 'A' and not full_content:
            continue

        summary_text = extract_preview(full_content)

        entry = {
            'title': f'<a href="{url}" target="_blank">{doc_title}</a>',
            'path': rel_path,
            'summary': summary_text,
            'tag_text': tag_text,
            'tag_class': tag_class
        }

        if tag_class == 'update' and diff_content:
            diffs_dir = ROOT_DIR / 'pages' / 'diffs'
            diffs_dir.mkdir(parents=True, exist_ok=True)
            safe_hash = args.commit_hash if args.commit_hash else 'local'
            diff_filename = f"{safe_hash}_{filename}.txt"
            diff_path = diffs_dir / diff_filename
            diff_path.write_text(diff_content, encoding='utf-8')
            entry['diff_file'] = f"pages/diffs/{diff_filename}"

        updates.append(entry)

    if updates:
        update_json_data(updates, args.commit_hash)

        release_body_path = ROOT_DIR / 'release_body.md'
        release_content = "## Android Docs Updates\n\n"
        for update in updates:
            path_str = f"`{update['path']}`\n" if 'path' in update else ""
            release_content += f"### {update['tag_text']} {update['title']}\n{path_str}{update['summary']}\n\n"
        release_body_path.write_text(release_content, encoding='utf-8')

if __name__ == '__main__':
    main()

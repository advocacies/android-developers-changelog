#!/usr/bin/env python3
"""Remove changelog entries and diff files older than 60 days."""

import json
import os
import shutil
from datetime import datetime, timedelta, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANGELOG_PATH = os.path.join(REPO_ROOT, "pages", "changelog.json")
DIFFS_DIR = os.path.join(REPO_ROOT, "pages", "diffs")
RETENTION_DAYS = 30


def main():
    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
    print(f"Cutoff date: {cutoff.isoformat()}")

    # Load changelog
    with open(CHANGELOG_PATH, "r") as f:
        groups = json.load(f)

    kept = []
    removed_hashes = set()

    for group in groups:
        try:
            date_str = group["date"]
            dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except (ValueError, KeyError):
            kept.append(group)
            continue

        if dt >= cutoff:
            kept.append(group)
        else:
            removed_hashes.add(group.get("commit_hash", ""))

    removed_count = len(groups) - len(kept)
    print(f"Changelog: {len(groups)} -> {len(kept)} (removed {removed_count} entries)")

    # Delete diff files for removed commits
    deleted_files = 0
    if removed_hashes and os.path.isdir(DIFFS_DIR):
        for filename in os.listdir(DIFFS_DIR):
            for h in removed_hashes:
                if h and filename.startswith(h):
                    filepath = os.path.join(DIFFS_DIR, filename)
                    os.remove(filepath)
                    deleted_files += 1
                    break

    print(f"Diffs: deleted {deleted_files} files")

    # Write pruned changelog
    with open(CHANGELOG_PATH, "w") as f:
        json.dump(kept, f, ensure_ascii=False)

    print("Done.")


if __name__ == "__main__":
    main()

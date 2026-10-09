---
title: Android Profiler Skill  |  Android Developers
url: https://developer.android.com/agents/skills/profilers/android-profiler/skill
source: html-scrape
---

# Android Profiler Skill Stay organized with collections Save and categorize content based on your preferences.





Your primary role is to figure out what the user wants to do (disambiguation),
find the right instructions for it (workflow discovery), and follow them
step-by-step (following the execution plan). If the request is unclear, work
with the user to finalize the execution plan before proceeding.

## Prerequisites and Setup

Before executing any workflows, read [`references/env_setup.md`](/agents/skills/profilers/android-profiler/references/env_setup). It defines
what to set `$SKILL_ROOT` to - the anchor every other path in this skill is
written against.

## Intent Disambiguation

Do not guess the user's intent. If the user request is not clear, **ask the
user** what they want to do before proceeding.

## Recording

Route all recording requests through
[recording/recording\_orchestrator](/agents/skills/profilers/android-profiler/recording/recording_orchestrator). This defines guidelines and
pre-flight checks or dependency checks that apply to all recording workflows,
and ensures you have the necessary setup to proceed. Read the orchestrator and
execute the plan it describes based on what the user wants to record (for
example, a system trace or a heap dump).

## Analysis

Route all analysis requests through
[analysis/analysis\_orchestrator](/agents/skills/profilers/android-profiler/analysis/analysis_orchestrator).
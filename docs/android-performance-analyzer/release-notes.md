---
title: Android Performance Analyzer release notes  |  Android Developers
url: https://developer.android.com/android-performance-analyzer/release-notes
source: html-scrape
---

Android Performance Analyzer is currently intended for profiling games and Vulkan-based graphics. For all other apps, use the [profilers in Android Studio](/studio/profile).

* [Home](https://developer.android.com/)
* [Android Performance Analyzer](https://developer.android.com/android-performance-analyzer)
* [Google Play](https://developer.android.com/distribute)
* [Guides](https://developer.android.com/games/guides)

# Android Performance Analyzer release notes Stay organized with collections Save and categorize content based on your preferences.





This page contains release notes for current and previous releases of
Android Performance Analyzer.

## 0.10.0-canary (September 2026)

This release brings the experimental rollout of the Frame Profiler component.

## 0.9.0 (July 2026)

This release brings various usability improvements such as slice search and
property copy/paste. It also contains various bug fixes for loading and
displaying traces.

### New features and enhancements

* Support searching for slices and navigating to next/previous with Enter/Shift-Enter.
* Accelerated data load times on zoom by 2.5x for large traces.
* Add 'm' keyboard shortcut to toggle timeline measurement.
* Support select/copy texts from the properties panel.
* Support regex in slice search and track filter.
* Improved precision and visualization of timestamps in timeline ruler.
* Label the process/thread the pinned track is rooted in.
* Add checkbox to enable/disable vsync highlights.

### Fixes

* Fix: Core titles remains hidden after clearing search.
* Fix: No GPU Counters displayed for Exynos devices.
* Fix: A horizontal blue row appears and disappears when navigating trace.
* Fix: Landscape screenshot previews are squished.
* Fix: VSync highlights masked by new background color in light mode.
* Fix: Wobbly zoom on Mac trackpad when using Cmd+Scroll.

### Other

* Updated Trace Processor to v56.
* Support overriding Android SDK Location via Settings.

## 0.8.1 (June 2026)

This point release fixes a critical trace loading issue, improves light mode
visibility, and delivers smoother navigation and visual polish.

### Fixes

* Fixed an issue where traces were failing to parse or load by updating the Trace Processor to v55.3.
* Fixed an issue where VSYNC highlights were not showing up properly when using light mode.
* Fixed the wobbly zoom behavior on Mac trackpads when using Cmd + Scroll.
* Resolved a layout overlap bug in the toolbar.
* Restored the missing divider line next to expanded track groups.
* Ensured landscape screenshots are correctly oriented before being scaled down.

## 0.8.0 (May 2026)

Android Performance Analyzer is publicly released.
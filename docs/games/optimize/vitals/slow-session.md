---
title: Slow Sessions  |  Android Developers
url: https://developer.android.com/games/optimize/vitals/slow-session
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Guides](https://developer.android.com/games/guides)

# Slow Sessions Stay organized with collections Save and categorize content based on your preferences.





In Android vitals, a slow session is a session in which more than 25% of the
frames are slow. A frame is slow if it is not presented less than 50ms after the
previous frame (equivalent to 20 FPS). Android vitals also reports a second Slow
Sessions metric with a target of 34ms (equivalent to 30 FPS). Using Slow
Sessions, you can understand the frame-rate performance of your game, which
impacts how smooth and fluid your game feels to users.

In due course, Play will start steering users away from games that cannot
achieve 20 FPS on their phones. Note that Android vitals only begins monitoring
frame rate after your game has been running for one minute.

Visit our [Help Center](https://support.google.com/googleplay/android-developer/answer/9844486#slow_frames&zippy=%2Cslow-session-rate-fps-or-fps-games-only%2Cexcessive-slow-frames-apps-only) for more details
about the metric.

![Pie chart-like graphics that show the number of slow frames and non-slow frames.](/static/google/play/vitals/images/slow-session.png)


**Figure 1.** A slow session in Android vitals.

**Note:** The Slow Sessions metric is computed with data collected from
[SurfaceFlinger](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager#surfaceflinger). More concretely, the frame rate of a
session is estimated based on the time in between frames drawn on surfaces
owned by the app. The estimated frame rate includes frames rendered by OpenGL,
Vulkan, as well as Android UI toolkit. This metric is available only for games.
If your apps use the `View`-based UI toolkit, where the user-visible portion of
the app is drawn from [`Canvas`](/reference/android/graphics/Canvas) or
the `View` hierarchy, refer to [Slow Rendering](/google/play/vitals/render).**Note:** For information on how to diagnose and resolve this issue, see
[Slow Sessions (games only)](/topic/performance/issues/slow-session).
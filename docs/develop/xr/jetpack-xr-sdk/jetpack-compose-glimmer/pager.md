---
title: Horizontal pagers in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/pager
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Horizontal pagers in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Display Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, [`GlimmerHorizontalPager`](/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPager.composable) is a lazily
composed, horizontally scrollable layout that arranges its pages sequentially.
It's similar to the standard [`HorizontalPager`](/reference/kotlin/androidx/compose/foundation/pager/HorizontalPager.composable) found in Compose
Foundation, but tailored for display glasses with Glimmer behaviors and
default values.

By default, only one page is prominently displayed at a time.
To provide a polished experience, the pager uses snap animations to ensure that
a page always settles exactly into the viewport boundaries after a user's
scrolling gesture ends.

![](/static/images/design/ui/glasses/guides/glasses_components_pager_opacity_do.png)


**Figure 1.** An example of `GlimmerHorizontalPager`.

## Key parameters and layout options

A `GlimmerHorizontalPager` provides customizable parameters to control spacing,
layout alignment, and lazy loading. Some of these parameters are:

| Parameter | Description |
| --- | --- |
| `state` | A [`GlimmerPagerState`](/reference/kotlin/androidx/xr/glimmer/pager/GlimmerPagerState) object that manages, observes, and programmatically controls the pager's scroll position and active page. |
| `contentPadding` | Padding applied around the overall content boundaries after clipping, useful for adding leading or trailing edge padding before the first page or after the last page. |
| `pageSpacing` | The horizontal spacing between individual pages in the pager. |
| `pageIndicator` | A composable slot rendering the active page indicator. Defaults to [`GlimmerHorizontalPagerDefaults.PageIndicator(state)`](/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPagerDefaults#PageIndicator(androidx.xr.glimmer.pager.GlimmerPagerState,androidx.compose.ui.Modifier)). |
| `beyondViewportPageCount` | The number of pages to compose and lay out beyond the visible viewport as a pre-loading optimization. Avoid setting large values to preserve lazy composition efficiency. |

See the full [reference documentation](/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPager.composable) for information on all available
parameters.

## Animated text motion recommendation

**Caution:** When rendering text inside a `GlimmerHorizontalPager`, We
recommended setting [`textMotion`](/reference/kotlin/androidx/compose/ui/text/style/TextMotion#Animated()) on text styles to
[`TextMotion.Animated`](/reference/kotlin/androidx/compose/ui/text/style/TextMotion#Animated()).

During pager snap animations and transitions on display glasses, default
text rendering can exhibit pixel-snapping artifacts. Setting
`TextMotion.Animated` ensures smooth rendering throughout layout animations:

```
Text(
    text = "Page: $page",
    style = LocalTextStyle.current.copy(textMotion = TextMotion.Animated),
)

GlimmerHorizontalPagerSample.kt
```

## Example: Horizontal pager

The following code demonstrates how to create a basic horizontal pager with
10 pages, placing a Card inside each page:

```
// Hoist the pager state, specifying the total page count with a lambda.
val pagerState = rememberGlimmerPagerState(pageCount = { 10 })

GlimmerHorizontalPager(
    state = pagerState,
    modifier = Modifier.fillMaxSize(),
) { page ->
    // Use Glimmer components like Card and Text for optimized glasses styling.
    Card(modifier = Modifier.fillMaxWidth()) {
        Text(
            text = "Page: $page",
            // Recommended: use TextMotion.Animated for smooth transitions in a pager.
            style = LocalTextStyle.current.copy(textMotion = TextMotion.Animated),
        )
    }
}

GlimmerHorizontalPagerSample.kt
```

### Key points about the code

* **State**: Initializes a [`GlimmerPagerState`](/reference/kotlin/androidx/xr/glimmer/pager/rememberGlimmerPagerState.composable) using
  `rememberGlimmerPagerState(pageCount = { 10 })` to manage the state of the
  pager.
* **Page slot content**: Receives the page index `page` inside the
  `GlimmerPagerScope` lambda to render each card.
* **Smooth animation text style**: Copies `LocalTextStyle.current` and
  explicitly enables `TextMotion.Animated`.
* **Automatic page indicator**: Unlike standard Compose pagers that require
  an external indicator component, `GlimmerHorizontalPager` automatically
  embeds a dot-style page indicator by default.

## Page indicators

By default, `GlimmerHorizontalPager` renders a dot-based page indicator using
[`GlimmerHorizontalPagerDefaults.PageIndicator`](/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPagerDefaults). The indicator automatically
adapts its color scheme:

* The active dot uses the content color resolved from the nearest surrounding
  [`surface`](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/surfaces).

You can pass a customized `PageIndicator` to specify explicit colors, or
replace the dot with your own custom layout:

```
GlimmerHorizontalPager(
    state = pagerState,
    modifier = Modifier.fillMaxSize(),
    // Use a page numbers instead of the default dot-indicator
    pageIndicator = {
        Text(
            text = "${pagerState.currentPage + 1} / ${pagerState.pageCount}",
            style = LocalTextStyle.current.copy(textMotion = TextMotion.Animated),
        )
    }
)

GlimmerHorizontalPagerSample.kt
```
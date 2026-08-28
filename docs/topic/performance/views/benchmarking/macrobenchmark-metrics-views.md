---
title: Capture Macrobenchmark metrics  |  Views  |  Android Developers
url: https://developer.android.com/topic/performance/views/benchmarking/macrobenchmark-metrics-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)
* [Guides](https://developer.android.com/topic/performance/views/benchmarking/macrobenchmark-control-app-views)

# Capture Macrobenchmark metrics Stay organized with collections Save and categorize content based on your preferences.





[Concepts and Jetpack Compose implementationarrow\_forward](/topic/performance/benchmarking/macrobenchmark-metrics)

Metrics are the main type of information extracted from your benchmarks. They
are passed to the [`measureRepeated`](/reference/kotlin/androidx/benchmark/macro/junit4/MacrobenchmarkRule#measureRepeated(kotlin.String,kotlin.collections.List,androidx.benchmark.macro.CompilationMode,androidx.benchmark.macro.StartupMode,kotlin.Int,kotlin.Function1,kotlin.Function1)) function as a `List`, which lets you
specify multiple measured metrics at once. At least one type of metric is
required for the benchmark to run.

The following code snippet captures frame timing and custom trace section
metrics:

### Kotlin

```
benchmarkRule.measureRepeated(
    packageName = TARGET_PACKAGE,
    metrics = listOf(
        FrameTimingMetric(),
        TraceSectionMetric("RV CreateView"),
        TraceSectionMetric("RV OnBindView"),
    ),
    iterations = 5,
    // ...
)
```

### Java

```
benchmarkRule.measureRepeated(
    TARGET_PACKAGE,     // packageName
    Arrays.asList(      // metrics
        new StartupTimingMetric(),
        new TraceSectionMetric("RV CreateView"),
        new TraceSectionMetric("RV OnBindView"),
    ),
    5,                  // Iterations
    // ...
);
```

In this example, [`RV CreateView`](https://cs.android.com/search?q=TRACE_CREATE_VIEW_TAG&sq=&ss=androidx%2Fplatform%2Fframeworks%2Fsupport) and [`RV OnBindView`](https://cs.android.com/search?q=TRACE_BIND_VIEW_TAG) are the IDs of
traceable blocks that are defined in [`RecyclerView`](/reference/androidx/recyclerview/widget/RecyclerView). The [source code for
the `createViewHolder()`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:recyclerview/recyclerview/src/main/java/androidx/recyclerview/widget/RecyclerView.java;l=7950-7964) method is an example of how you can define
traceable blocks within your own code.

[`StartupTimingMetric`](#startup-timing), [`TraceSectionMetric`](#trace-section), and
[`FrameTimingMetric`](#frame-timing) are covered in detail later in this document. For a
full list of metrics, check out subclasses of [`Metric`](/reference/kotlin/androidx/benchmark/macro/Metric).

Benchmark results are output to Android Studio, as shown in figure 1. If
multiple metrics are defined, all of them are combined in the output.

![Results of TraceSectionMetric and FrameTimingMetric.](/static/topic/performance/images/benchmark_images/macrobenchmark_results_frames_tracing.png)


**Figure 1.** Results of `TraceSectionMetric` and
`FrameTimingMetric`.

## StartupTimingMetric

[`StartupTimingMetric`](/reference/kotlin/androidx/benchmark/macro/StartupTimingMetric) captures app startup timing metrics with the
following values:

* `timeToInitialDisplayMs`: The amount of time from when the system receives a
  launch intent to when it renders the first frame of the destination
  [`Activity`](/reference/android/app/Activity).
* `timeToFullDisplayMs`: The amount of time from when the system receives a
  launch intent to when the app reports fully drawn using the
  [`reportFullyDrawn()`](/reference/android/app/Activity#reportFullyDrawn()) method. The measurement stops at the completion
  of rendering the first frame after—or containing—the
  `reportFullyDrawn()` call. This measurement might not be available on
  Android 10 (API level 29) and earlier.

`StartupTimingMetric` outputs the minimum, median, and maximum values from the
startup iterations. To assess startup improvement, always focus on median
values, since they provide the best estimate of typical user startup times. For
more information about what contributes to app startup time, see [App startup
time](/topic/performance/vitals/launch-time).

![StartupTimingMetric results](/static/topic/performance/images/benchmark_images/macrobenchmark_results_fully_drawn_startup.png)


**Figure 2.** `StartupTimingMetric` results.

## FrameTimingMetric

[`FrameTimingMetric`](/reference/kotlin/androidx/benchmark/macro/FrameTimingMetric) captures timing information from frames produced by a
benchmark, such as scrolling or animation, and outputs the following values:

* `frameOverrunMs`: the amount of time a given frame misses its deadline by.
  Positive numbers indicate a dropped frame accompanied by visible jank or
  stutter. Negative numbers indicate how much faster a frame completed
  relative to the subsystem hardware deadline. Note: This metric is available
  only on Android 12 (API level 31) and later.
* `frameDurationCpuMs`: the amount of time the frame takes to be produced on
  the CPU on both the UI thread and the `RenderThread`.

These measurements are collected in a distribution of 50th, 90th, 95th, and 99th
percentile.

For more information on how to identify and improve slow frames, see [Slow
rendering](/topic/performance/vitals/render).

![FrameTimingMetric results](/static/topic/performance/images/benchmark_images/macrobenchmark_results_frames.png)


**Figure 3.** `FrameTimingMetric` results.

## TraceSectionMetric

**Experimental:** This class is experimental.

[`TraceSectionMetric`](/reference/kotlin/androidx/benchmark/macro/TraceSectionMetric) captures the number of times a specific trace section
occurs and the absolute amount of time it takes to execute. For time tracking,
it outputs the minimum, median, and maximum times in milliseconds.

The target trace section is defined either by the function call
[`trace(sectionName)`](/reference/kotlin/androidx/tracing/package-summary#trace(kotlin.String,kotlin.Function0)) or the lower-level block boundaries between
[`Trace.beginSection(sectionName)`](/reference/kotlin/androidx/tracing/Trace#beginSection(java.lang.String)) and [`Trace.endSection()`](/reference/kotlin/androidx/tracing/Trace#endSection()) or their
async variants. It always selects the first instance of a trace section captured
during a measurement. It only outputs trace sections from your package by
default; to include processes outside your package, set `targetPackageOnly =
false`.

For more information about tracing, see [Overview of system tracing](/topic/performance/tracing) and
[Define custom events](/topic/performance/tracing/custom-events).

![TraceSectionMetric](/static/topic/performance/images/benchmark_images/macrobenchmark_results_tracing.png)


**Figure 4.** `TraceSectionMetric` results.



## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Create Baseline Profiles {:#creating-profile-rules}](/topic/performance/baselineprofiles/create-baselineprofile)
* [Writing a Macrobenchmark](/topic/performance/benchmarking/macrobenchmark-overview)
* [App startup analysis and optimization {:#app-startup-analysis-optimization}](/topic/performance/appstartup/analysis-optimization)
---
title: AEP guideline: Night Mode  |  Apps Experience Program  |  Android Developers
url: https://developer.android.com/distribute/aep/aep-req-night-mode
source: html-scrape
---

You are currently viewing the Apps Experience Program (AEP) documentation.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Apps Experience Program](https://developer.android.com/distribute/aep)

# AEP guideline: Night Mode Stay organized with collections Save and categorize content based on your preferences.





Adopt Night Mode to enable hardware-accelerated low light photo capture with the
in-app camera, ensuring your app leverages the same advanced image processing as
the native camera app for high-quality results in low-light environments.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

* Support the Night Mode Camera Extension by using either the Jetpack CameraX
  Extensions API or the Android Camera2 Extensions API.
* Implement the platform-recommended Night Mode Indicator API (available in
  Android 16) to inform users when a low-light capture is recommended.

## Guideline applicability

This guideline applies to:

* Apps that support still image capture.
* Phone, tablet, and foldable form factors.

## Exemptions

The following exemptions apply for this guideline:

* Apps that **only** capture video content, as Night Mode is specifically for
  still image capture.
* Apps can use an equivalent alternative framework that provides similar
  quality, user capabilities, stability and compatibility across the
  ecosystem. [Contact support](/distribute/aep/aep-get-support) if you have a suitable framework for
  consideration.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Night Mode** feature. These resources are for your reference only and
don't contain additional program requirements.

* [Low light photography and videography solutions](/media/camera/lowlight)
* [CameraX Extensions API](/media/camera/camerax/extensions-api)
* [Real-time Capture Latency Estimate (CameraX)](/reference/kotlin/androidx/camera/core/ImageCapture#getRealtimeCaptureLatencyEstimate())
* [Night Mode Extension (Camera2)](/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_NIGHT)
* [Night Mode Indicator Result (Camera2)](/reference/android/hardware/camera2/CaptureResult#EXTENSION_NIGHT_MODE_INDICATOR)
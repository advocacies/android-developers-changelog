---
title: AEP guideline: Physics Based Motion  |  Apps Experience Program  |  Android Developers
url: https://developer.android.com/distribute/aep/aep-req-physics-based-motion
source: html-scrape
---

You are currently viewing the Apps Experience Program (AEP) documentation.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Apps Experience Program](https://developer.android.com/distribute/aep)

# AEP guideline: Physics Based Motion Stay organized with collections Save and categorize content based on your preferences.





Implement physics-based motion dynamics for primary user interactions to elevate
the perceived quality, fluidity, and responsiveness of your apps. Use
spring-driven mechanics instead of duration-based, fixed easing curves to ensure
that motion preserves the momentum of the user's gesture and remains fully
interruptible, eliminating rigid transitions.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

* The app must not have 0ms visual transitions during primary navigation or
  state changes, including immediate screen replacements or instantaneous
  layout shifts.
* All core app interactions, navigations, and transient views must utilize
  visual transitions with a duration greater than 0 ms.
* Maintain user context through interpolation methods such as cross-fades,
  standard easing, shared element transitions, or physics-based spring
  animations.

**Tip**: If you are using Jetpack Compose to develop the app's UI, use the
[`spring() AnimationSpec`](/develop/ui/compose/animation/customize#animationspec) for positional and state changes, and tune the
*dampingRatio* and *stiffness* to create a natural, responsive feel.

## Guideline applicability

This guideline applies:

* To apps that provide a comparable Physics Based Motion implementation on a
  non-Android platform.
* To all form factors on which the app is available.

## Exemptions

There are no exemptions for this guideline.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Physics Based Motion** feature. These resources are for your reference
only and don't contain additional program requirements.

* [Jetpack Compose Tutorial](/develop/ui/compose/tutorial)
* [Customize animations](/develop/ui/compose/animation/customize#spring)
* [Animate movement using spring physics](/develop/ui/views/animations/spring-animation)
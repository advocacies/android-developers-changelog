---
title: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
url: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
source: md.txt
---

[Documentation](https://developer.android.com/blog/categories/documentation)

# Upcoming Changes to the Nearby Connections API

1 min read ![](https://developer.android.com/static/blog/assets/Upcoming_Changes_to_the_Nearby_Connections_API_Strapi_11b1de50e2_ZGVCnW.webp) 20 Jul 2026 [![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp)](https://developer.android.com/blog/authors/wei-wang) [Wei Wang](https://developer.android.com/blog/authors/wei-wang) Engineering Manager, Android BeTo User privacy and transparency are core to the Android experience. To better align with these principles, we are updating the default behavior of the Nearby Connections API regarding how it interacts with device radios.

### **What is changing?**

Previously, the Nearby Connections API could automatically toggle Wi-Fi and Bluetooth radios ON to facilitate connections without explicit user intervention. Moving forward, the API will no longer automatically enable these radios for 1P and 3P applications.

### **What this means for developers**

If your app relies on Nearby Connections, you will need to update your implementation to account for these changes:

- **Manual Radio Management:**You must ensure that the necessary radios (Wi-Fi or Bluetooth) are enabled before initiating Nearby Connections tasks.
- **User Notification:**If the required radios are disabled, your app must now inform the user and request that they enable them manually. The API will no longer programmatically turn them on for you.

### **Timing**

These changes are scheduled to take effect in late 2026. We recommend reviewing your connection workflows now to ensure a seamless transition for your users.
Written by:

-

  ## [Wei Wang](https://developer.android.com/blog/authors/wei-wang)

  ###### Engineering Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/wei-wang) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp)
Continue reading
- [![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_Z2l461S.webp)](https://developer.android.com/blog/authors/rob-orgiu) 31 Aug 2026 31 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_123_Streamline_adaptive_testing_with_emulator_commands_Strapi_0d1336f9a2_1recRz.webp) [Documentation](https://developer.android.com/blog/categories/documentation)

  ## [Emulator control for adaptive app development](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development)

  [arrow_forward](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development) Adaptive app development is fundamental on Android, but making sure everything looks good and every feature works the way it should require multiple tests on multiple devices. Or does it?
  [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu) • 2 min read
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
- 3 Authors 20 Oct 2026 20 Oct 2026 ![](https://developer.android.com/static/blog/assets/header_068afa9a28_dpgDg.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Remote Compose Gaming Widgets](https://developer.android.com/blog/posts/remote-compose-gaming-widgets)

  [arrow_forward](https://developer.android.com/blog/posts/remote-compose-gaming-widgets) Did you know you can build an interactive Android gaming widget? This blog post series will show you how with a new alpha library called Remote Compose.
  [Ash Nohe](https://developer.android.com/blog/authors/ash-nohe), [John Hoford](https://developer.android.com/blog/authors/john-hoford), [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) • 15 min read
  - [#Remote Compose](https://developer.android.com/blog/topics/remote-compose)
- 3 Authors 19 Oct 2026 19 Oct 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Grab_Strapi_2000x1000_STATIC_1_dbb884ce74_22df0m.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Grab Reduces ANRs by 32% and improves startup time by 35% with R8 and Profile guided optimization](https://developer.android.com/blog/posts/grab-r8-profile-guided-optimization-anr-startup-time)

  [arrow_forward](https://developer.android.com/blog/posts/grab-r8-profile-guided-optimization-anr-startup-time) Grab is Southeast Asia's leading superapp, offering deliveries, mobility, and financial services to millions of users across eight countries through a single app.
  [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai), [Nguyen Van Minh](https://developer.android.com/blog/authors/nguyen-van-minh), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 5 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)
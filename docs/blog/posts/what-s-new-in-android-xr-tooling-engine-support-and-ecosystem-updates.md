---
title: What’s New in Android XR: Tooling, Engine Support, and Ecosystem Updates  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



[Product News](/blog/categories/product-news)

# What’s New in Android XR: Tooling, Engine Support, and Ecosystem Updates

2 min read

![](/static/blog/assets/MM_Android_XR_Meta_a489e757ed_Z1R62M0.webp)

15

Jun
2026

[![View Stevan Silva's profile](/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](/blog/authors/stevan-silva)[![View Vinny DaSilva's profile](/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](/blog/authors/vinny-da-silva)

[Stevan Silva](/blog/authors/stevan-silva)
&
[Vinny DaSilva](/blog/authors/vinny-da-silva)

From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today. Alongside the latest updates from [Google I/O](/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4)  and this week's Augmented World Expo (AWE), we are rolling out new tooling, broader engine support, and ecosystem resources to help you build and scale experiences for Android XR.

To get a quick look at what’s new, check out our video recap!

Ready to dive deeper? Let’s jump into the major updates that will streamline your XR development workflow.

### Build, Prototype, and Iterate with Developer Preview 4

[Developer Preview 4 of the Android XR SDK](/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4) delivers the APIs and tools you need to design and build right from your laptop. This update includes the specific libraries required to target both immersive and augmented experiences. Check out the video below for a comprehensive breakdown of the latest in Android XR:

To test all of these interactions without needing physical hardware, you can emulate and iterate on your code entirely within [Android Studio](/studio/preview). Check out our tooling deep dive to see how you can use XR emulator today:

#### Extending your mobile apps for intelligent eyewear

Building for audio and display glasses doesn't mean starting from scratch. With the [Jetpack Projected library](/develop/xr/jetpack-xr-sdk#jetpack-projected), you can take your existing mobile app to create a complementary augmented experience. The new release includes a [Device Availability API](/develop/xr/jetpack-xr-sdk/glasses/check-availability) that hooks into standard Android Lifecycle states, allowing your app to natively adapt its behavior based on whether the glasses are being worn.

To accelerate your development journey, use [Android CLI](/tools/agents) and the [display glasses skil](https://github.com/android/skills)l to extend your mobile app into an augmented experience. The skill is packed with specialized knowledge of Jetpack Compose Glimmer, enabling it to build your UI using our recommended design patterns.

We’ve also updated [Jetpack Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) to optimize text legibility on optical see-through displays and provide touchpad-optimized navigation components.

See how it looks in action: Developers at [NAVER Papago](https://play.google.com/store/apps/details?id=com.naver.labs.translator) are already exploring how to seamlessly bring their [mobile experience directly to display glasses.](https://blog.naver.com/nv_papago/224314256256)

To learn how to leverage these tools, watch this session on extending mobile apps for AI glasses:

#### Building global, location-based immersive experiences

For developers focused on immersive experiences, Developer Preview 4 brings modern, Kotlin-first architectural upgrades across our core perception libraries. We have also introduced an early preview of the Geospatial API for wired XR glasses. By combining [ARCore for Jetpack XR](/develop/xr/jetpack-xr-sdk/arcore) with Google's Visual Positioning System (VPS), you can anchor digital content to high-precision real-world locations.

### Leverage the Platforms You Know with Expanded Engine Support

We want you to build using the ecosystems and workflows you already know best. To make it easier to bring your existing XR experiences over to Android XR, we are thrilled to introduce [official support for Unreal Engine and Godot](/blog/posts/android-xr-updates-for-unity-unreal-and-godot) alongside [Unity’s support for wired XR glasses](https://unity.com/blog/unity-android-xr-wired-glasses-support).

With this expansion, we are introducing the [Android XR Engine Hub,](/develop/xr/engine-hub) a desktop tool for Windows that shortens iteration cycles by bringing real-time testing directly into your engines viewport. Catch the full breakdown of our engine updates here:

### Apply Today for the Android XR Developer Catalyst Program

In addition to providing the platform, we want to fuel your innovation directly through ecosystem resources. The [Android XR Developer Catalyst Program](/develop/xr/catalyst) is designed to support developers with access to pre-release hardware, including display glasses, and wired XR glasses.

Accepted developers will receive resources, support forums, and launch guidance to prepare their apps for Google Play. Applications are open right now, so don't wait to [submit your project ideas](/develop/xr/catalyst).

### Start Building!

The ecosystem is growing rapidly, and the tools are ready for you to explore. Samsung Galaxy XR is available now, and you can dive in today with [Developer Preview 4 of the Android XR SDK](/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4). If you don’t have hardware yet, check out the tools and to get started with the [XR Emulator in Android Studio](http://google.com/url?sa=j&url=http%3A%2F%2Fgoo.gle%2Fxr-setup&uct=1765473974&usg=L4MkW244XAfYytuJciS39GjuDv0.&opi=73833047&source=chat).

For a complete look at all of our technical sessions, browse the full [Android XR Playlist on YouTube](https://youtube.com/playlist?list=PLWz5rJ2EKKc-feGl0F3rXtUste_8TkvZJ&si=zggz4T3eiQmH5xL2) to see what else is possible. We can’t wait to see what you build!

* [#Android XR](/blog/topics/android-xr)
* [#Developer Preview 4](/blog/topics/developer-preview-4)

Written by:

* ## [Stevan Silva](/blog/authors/stevan-silva)

  ###### Group Product Manager

  [read\_more
  View profile](/blog/authors/stevan-silva)

  ![View Stevan Silva's profile](/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)

  ![View Stevan Silva's profile](/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)
* ## [Vinny DaSilva](/blog/authors/vinny-da-silva)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/vinny-da-silva)

  ![View Vinny DaSilva's profile](/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)

  ![View Vinny DaSilva's profile](/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)

Continue reading

* [![View Amy Zeppenfeld's profile](/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp)](/blog/authors/amy-zeppenfeld)[![View Stevan Silva's profile](/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](/blog/authors/stevan-silva)

  19

  May
  2026

  19

  May
  2026

  ![](/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp)

  [Product News](/blog/categories/product-news)

  ## [Updates to the Android XR SDK: Introducing Developer Preview 4](/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4)

  [arrow\_forward](/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4)

  We're excited to launch Developer Preview 4 of the Android XR SDK, continuing our focus on unifying cross-device development for headsets, wired XR glasses, and intelligent eyewear.

  [Amy Zeppenfeld](/blog/authors/amy-zeppenfeld),
  [Stevan Silva](/blog/authors/stevan-silva)
  •
  5 min read
  + [#Android XR](/blog/topics/android-xr)
  + [#Android XR SDK](/blog/topics/android-xr-sdk)
  + [#Developer Preview](/blog/topics/developer-preview)
  + [#Unity](/blog/topics/unity)
  + [#Google I/O](/blog/topics/google-i-o)
  + +3
    ↩
* 3
  Authors

  18

  Aug
  2026

  18

  Aug
  2026

  ![](/static/blog/assets/Android_XR_beta_release_Strapi_a23ed1d892_Z1YdYO1.webp)

  [Product News](/blog/categories/product-news)

  ## [Jetpack XR SDK core libraries reach beta: The next milestone for Android XR](/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr)

  [arrow\_forward](/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr)

  Since introducing the Android XR SDK, developers have transformed their ideas into innovative immersive experiences across headsets and wired XR glasses.

  [Amy Zeppenfeld](/blog/authors/amy-zeppenfeld),
  [Greg Underwood](/blog/authors/greg-underwood),
  [Yasmine Evjen](/blog/authors/yasmine-evjen)
  •
  2 min read
  + [#Jetpack XR SDK](/blog/topics/jetpack-xr-sdk)
  + [#Android XR](/blog/topics/android-xr)
  + [#Android XR SDK](/blog/topics/android-xr-sdk)
  + +1
    ↩
* [![View Luke Hopkins's profile](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](/blog/authors/luke-hopkins)[![View Ryan Bartley's profile](/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](/blog/authors/ryan-bartley)

  19

  May
  2026

  19

  May
  2026

  ![](/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  [Product News](/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow\_forward](/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  [Luke Hopkins](/blog/authors/luke-hopkins),
  [Ryan Bartley](/blog/authors/ryan-bartley)
  •
  4 min read
  + [#Android XR](/blog/topics/android-xr)
  + [#Google I/O](/blog/topics/google-i-o)
  + [#Game engine development](/blog/topics/game-engine-development)
  + +1
    ↩

Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)
---
title: Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/build-android-xr-devices-tools
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



[Product News](/blog/categories/product-news)

# Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit

3 min read

![](/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp)

06

Nov
2026

[![View Amy Zeppenfeld's profile](/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](/blog/authors/amy-zeppenfeld)[![View Vinny DaSilva's profile](/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](/blog/authors/vinny-da-silva)

[Amy Zeppenfeld](/blog/authors/amy-zeppenfeld)
&
[Vinny DaSilva](/blog/authors/vinny-da-silva)

From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users wherever they are. At [Android Developer Summit](/events/dev-summit), we marked an exciting milestone with the launch of [XREAL AURA](https://blog.google/products-and-platforms/platforms/android/xreal-aura/), the first wired XR glasses powered by Android XR. Designed for lightweight comfort at under 95 grams with a portable compute puck, XREAL AURA leverages a shared Android foundation so your existing apps work out of the box on day one, giving you the perfect starting point to expand into richer spatial interactions.

To help you build for this expanding hardware landscape, we're delivering production-grade tools across the entire platform stack. We've graduated core Jetpack XR libraries and device emulators to stable, added real-world anchoring in ARCore for Jetpack XR, streamlined 3D engine workflows across Unity, Godot, and Unreal Engine.

Read the highlights of our announcements here, and head over to the [Android Developer Summit XR Session Playlist](https://www.youtube.com/playlist?list=PLYoZJLA8zYxU) to watch all technical walkthroughs on demand.

### **Stabilizing core Jetpack XR foundations and developer tooling**

For developers building native experiences with Kotlin and Compose, production readiness begins at the platform layer. The core Jetpack XR SDK libraries have officially graduated to stable, providing long-term API stability and production performance. This stable release includes [Jetpack SceneCore](/jetpack/androidx/releases/xr-scenecore) for building and manipulating the Android XR scene graph with 3D content, [ARCore for Jetpack XR](/jetpack/androidx/releases/xr-arcore) to handle environment perception, and [XR Runtime](/jetpack/androidx/releases/xr-runtime) for standardized session management. Alongside these libraries, Android XR emulators in [Android Studio](/studio) are now stable, letting you build, iterate, and visually validate layouts across XR devices directly from your laptop without needing physical hardware.

To see how these foundation APIs translate into real-world applications, watch[Moving beyond 2D with custom 3D geometry in the Jetpack XR SDK](https://youtu.be/mssk4zPs0zU?si=M0o-G0ZY1pZVtdX5). Discover how to animate glTF models, manipulate subnodes, use custom PBR materials at runtime, and generate real-time procedural 3D meshes in Kotlin using Jetpack SceneCore.

### **Anchoring digital experiences to the physical world**

The[Geospatial APIs](/develop/xr/jetpack-xr-sdk/arcore/geospatial) in ARCore for Jetpack XR are now stable, enabling you to anchor digital content to real-world coordinates with high precision and robust local tracking. These capabilities unlock contextual, location-aware experiences across wired XR glasses by combining visual positioning services with local device perception.

In [Build world anchored experiences for XREAL AURA wired XR glasses](https://youtu.be/4NGBZnfnD6o?si=pXU36JeVKC1blGE1), you will learn how to design glanceable optical see-through UIs with Jetpack Compose Glimmer and anchor them to real-world locations. For teams building in game engines, [Architecting Spatial Content on Android XR with Unity](https://youtu.be/bz_01jWmNZc?si=RfTZm-o185du2w4G)explores how to map physical spaces, persist 3D placements across sessions, and synchronize shared multi-user experiences in Unity using Spatial Entities, Cloud Anchors, and ARCore Geospatial APIs.

### **Scaling across familiar 3D engines**

Android XR meets developers wherever they already build, including rich interactive environments crafted in dedicated real-time engines. The Android XR Engine Hub is now stable, streamlining setup, configuration, and optimization pipelines across Unity, Godot, and Unreal Engine. The Engine Hub simplifies project scaffolding with pre-configured OpenXR extensions and validated project settings so you can start creating immediately. It also delivers native profiling workflows to help you capture and inspect system traces, thermal limits, and frame budgets across CPU and GPU cores directly within your engine interface.

To see how these runtime systems connect directly with Android UI, watch [Elevate immersive experiences with 3D Engines in Jetpack Compose for XR](https://youtu.be/u8dsUtPvOlY?si=XJZYxVILCtRo6_A7) and see how to embed Godot and Unity as libraries inside native Jetpack Compose apps using OpenXR Spatial Containers.

Supporting familiar engines makes it seamless to adapt existing 3D titles for Android XR form factors. Teams like Contract XR are already leveraging this pipeline with their ported Unity game, Jigsaw Night, on XREAL AURA, creating a collaborative space where players can walk around, pass pieces, and solve puzzles together, demonstrating how lightweight XR glasses and engine workflows unlock natural, multi-user mixed reality experiences.

[](/static/blog/assets/videos/ASFV_028_horizontal_v5_compressed_859c4fcd49/ASFV_028_horizontal_v5_compressed_859c4fcd49.mp4)


Developer Spotlight: Building collaborative mixed reality for XREAL AURA with Contract XR

### **Designing multimodal interactions with on-device audio**

As the device lineup expands into audio interactions, we are introducing new tools to architect lightweight, multimodal experiences. Developers can now leverage the [ML Kit Gen AI Text to Speech API](https://developers.google.com/ml-kit/genai/text-to-speech/android) to generate natural-sounding voices powered by on-device AI. We have launched new design guidance around [best practices for sound](/design/ui/ai-glasses/guides/sound/overview), including [Earcons](/design/ui/ai-glasses/guides/sound/earcons), to guide users through audio-first and augmented environments. To see these pieces in action, watch [Building audio-first experiences for intelligent eyewear with Gemini Nano 4](https://youtu.be/tW3mg0iyi_w?si=X0UYsEbLreVHCNRv) to learn how to combine Jetpack Projected, ML Kit, and on-device Gemini Nano into hands-free, conversational apps.

### **Get started with the latest tools**

With these updates to our core SDKs, emulators, and engine tools, you have the foundation to build immersive and augmented experiences across the Android XR ecosystem. Update to the latest stable release of Android Studio today to set up and test Android XR virtual devices for glasses form factors, add the stable Jetpack XR dependencies to your build files, or install the Android XR Engine Hub plugin for your preferred 3D engine. With new devices like XREAL AURA now available now, it’s the perfect time to build for Android XR. Head over to our [Android XR Developer Site](/develop/xr) for the stable libraries, tools, and guides you need to get started today.

To explore all of our technical sessions and deep dives from the Android Dev Summit, check out the complete[Android XR Session Playlist](https://www.youtube.com/playlist?list=PLYoZJLA8zYxU).

* [#Android XR](/blog/topics/android-xr)

Written by:

* ## [Amy Zeppenfeld](/blog/authors/amy-zeppenfeld)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/amy-zeppenfeld)

  ![View Amy Zeppenfeld's profile](/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)

  ![View Amy Zeppenfeld's profile](/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)
* ## [Vinny DaSilva](/blog/authors/vinny-da-silva)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/vinny-da-silva)

  ![View Vinny DaSilva's profile](/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)

  ![View Vinny DaSilva's profile](/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)

Continue reading

* 3
  Authors

  18

  Aug
  2026

  18

  Aug
  2026

  ![](/static/blog/assets/Android_XR_beta_release_Strapi_a23ed1d892_2wR9tl.webp)

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
* [![View Stevan Silva's profile](/static/blog/assets/Stevan_Silva_7661118077_ZaY4rR.webp)](/blog/authors/stevan-silva)[![View Vinny DaSilva's profile](/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](/blog/authors/vinny-da-silva)

  15

  Jun
  2026

  15

  Jun
  2026

  ![](/static/blog/assets/MM_Android_XR_Meta_a489e757ed_Z1JMs6H.webp)

  [Product News](/blog/categories/product-news)

  ## [What’s New in Android XR: Tooling, Engine Support, and Ecosystem Updates](/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow\_forward](/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.

  [Stevan Silva](/blog/authors/stevan-silva),
  [Vinny DaSilva](/blog/authors/vinny-da-silva)
  •
  2 min read
  + [#Android XR](/blog/topics/android-xr)
  + [#Developer Preview 4](/blog/topics/developer-preview-4)
* [![View Amy Zeppenfeld's profile](/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](/blog/authors/amy-zeppenfeld)[![View Stevan Silva's profile](/static/blog/assets/Stevan_Silva_7661118077_ZaY4rR.webp)](/blog/authors/stevan-silva)

  19

  May
  2026

  19

  May
  2026

  ![](/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_2cdxMf.webp)

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

Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)
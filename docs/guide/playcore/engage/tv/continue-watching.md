---
title: Publish continue watching data  |  Other Play guides  |  Android Developers
url: https://developer.android.com/guide/playcore/engage/tv/continue-watching
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Other Play guides](https://developer.android.com/guide/app-bundle)

# Publish continue watching data Stay organized with collections Save and categorize content based on your preferences.





Continue watching leverages the **Continuation cluster** to show unfinished
videos, and next episodes to be watched from the same TV show, from multiple
apps in one UI grouping. You can feature your entities in this continuation
cluster. Follow this guide to learn how to enhance user engagement through the
continue watching experience using [Engage SDK](/guide/playcore/engage).

You manage the continuation cluster by using the client API in a TV app or from
a REST API:

* [Integrate continue watching on Android TV](/guide/playcore/engage/tv/continue-watching/client)
* [Integrate continue watching using REST API](/guide/playcore/engage/tv/continue-watching/rest)

## Sample code

This [sample app](https://github.com/googlesamples/tv-video-discovery-samples) demonstrates how you can integrate with Engage SDK
to send personalized user data to Google. It shows how to build a common module
that you can import in both mobile and TV apps. The sample also illustrates
when to call the publish and delete APIs, as well as how to use Workers to
make these calls.
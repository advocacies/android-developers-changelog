---
title: Test your app with ARCore test rules  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/testing
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Test your app with ARCore test rules Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

![](/static/images/develop/xr/ai-glasses-icon.svg)


Audio &  
Display Glasses

[Learn about XR device types →](/develop/xr/devices)

Augmented reality apps often depend on specific real-world situations to
function. For example, your app might require a detected surface, like a table,
in order to place a virtual game board. To test your app against different
scenarios, use the [ARCore test rule](/reference/kotlin/androidx/xr/arcore/testing/ArCoreTestRule) APIs to write tests in a
controlled ARCore test environment. The APIs handle session setup and state, so
you can focus on testing your app's core logic.

## Add library dependencies

To use the ARCore test rule, add these dependencies to your app's `build.gradle`
file:

### Kotlin

```
dependencies {
    testImplementation("androidx.xr.arcore:arcore-testing:1.0.0-beta02")
}
```

### Groovy

```
dependencies {
    testImplementation "androidx.xr.arcore:arcore-testing:1.0.0-beta02"
}
```

If your app depends on [XR SceneCore](/jetpack/androidx/releases/xr-scenecore), also include the
[XR SceneCore testing](/jetpack/androidx/releases/xr-scenecore#declaring_dependencies) dependency:

### Kotlin

```
dependencies {
    testImplementation("androidx.xr.scenecore:scenecore-testing:1.0.0-beta02")
}
```

### Groovy

```
dependencies {
    testImplementation "androidx.xr.scenecore:scenecore-testing:1.0.0-beta02"
}
```

## Set up the test rule

In your [JUnit test](/training/testing/local-tests), use a
[`AndroidJUnit4` test runner](/training/testing/local-tests/robolectric) to set up a test:

```
@Rule @JvmField val arCoreTestRule = ArCoreTestRule()
private lateinit var activityController: ActivityController<ComponentActivity>
private lateinit var activity: ComponentActivity
private lateinit var testDispatcher: TestDispatcher
private lateinit var testScope: TestScope
private lateinit var session: Session

@Before
fun setUp() {
    testDispatcher = StandardTestDispatcher()
    testScope = TestScope(testDispatcher)
    activityController = Robolectric.buildActivity(ComponentActivity::class.java)
    activity = activityController.get()

    // Set up the activity permissions.
    shadowOf(activity.application).grantPermissions(HAND_TRACKING)

    activityController.create().start().resume()

    runBlocking {
        val sessionCreateResult = Session.create(context = activity, coroutineContext = testDispatcher)
        session = (sessionCreateResult as SessionCreateSuccess).session
    }

    // Configure the session.
    session.configure(Config.Builder(session.config).setHandTracking(HandTrackingMode.BOTH).build())
}

ArCoreTestRule.kt
```

In the `@Before` step, set up your testing environment, including required
permissions and session configuration.

## Create test cases

[Create a test case](/training/testing/local-tests/robolectric#ui-testing) in order to test a certain scenario. In
this example, we test whether a [hand tracking](/develop/xr/jetpack-xr-sdk/arcore/hands) gesture detector
works with our test data:

```
@Test
fun test_thumbsUp() = runTest(testDispatcher) {
    arCoreTestRule.rightHandTester.isVisible = true
    arCoreTestRule.rightHandTester.handJointMap = gestureThumbsUp
    advanceUntilIdle()
    val handState = Hand.right(session).state.value

    val isThumbsUp = detectThumbsUp(handState)
    assertThat(isThumbsUp).isTrue()
}

ArCoreTestRule.kt
```

A unit test often contains the following steps:

1. To set up the test, use the [`ArCoreTestRule`](/reference/kotlin/androidx/xr/arcore/testing/ArCoreTestRule) to inject
   test data. This object contains the environment data that your app reads from
   the session. Use [`TestScope.advanceUntilIdle`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/advance-until-idle.html) to ensure
   the system is ready to perform the test. In this example, the right hand is
   enabled, and pose data is used to populate the hand joint data.
2. Then, perform the test. Your app doesn't need special behavior to use the
   injected data: the `Session` uses data that was injected into the
   `ArCoreTestRule`.
3. Finally, check the results.

## Additional resources

For more information about testing on Android, consult the following resources:

* [Test apps on Android](/training/testing)
* [Fundamentals of testing Android apps](/training/testing/fundamentals)
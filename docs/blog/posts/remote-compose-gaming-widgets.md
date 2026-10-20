---
title: https://developer.android.com/blog/posts/remote-compose-gaming-widgets
url: https://developer.android.com/blog/posts/remote-compose-gaming-widgets
source: md.txt
---

[How-tos](https://developer.android.com/blog/categories/how-tos)

# Remote Compose Gaming Widgets

15 min read ![](https://developer.android.com/static/blog/assets/header_068afa9a28_dpgDg.webp) 20 Oct 2026 3 Authors [Ash Nohe,](https://developer.android.com/blog/authors/ash-nohe) [John Hoford,](https://developer.android.com/blog/authors/john-hoford) [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) Did you know you can build an interactive Android gaming widget? This blog post series will show you how with a new alpha library called [Remote Compose](https://developer.android.com/jetpack/androidx/releases/compose-remote).
![AndroidPet.gif](https://developer.android.com/static/blog/assets/Android_Pet_1dbefbd629_ZwIMkP.webp) Android Pet ![FlappyDroid.gif](https://developer.android.com/static/blog/assets/Flappy_Droid_53e541d6b7_Z2p0ta3.webp) Flappy Droid

After reading this post you'll know:

- When to use Jetpack Glance and Remote Compose
- How to set up a basic Remote Compose widget using the `creation-compose` library.
- How to manage widget state.

Note: Because the Remote Compose library is currently in alpha, code examples in this blog might need modifications to work with future versions of Remote Compose.

For most cases, you should use [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance) to build Android widgets. It is a backwards compatible library with developer tooling that simplifies building high quality widgets across form factors.

But some delightful widget use cases cannot be built with Jetpack Glance, especially those that require animations. This is because Jetpack Glance uses the legacy `RemoteViews` system that (a) cannot use mathematical expressions (for example to continually rotate an object) and (b) is controlled by the Android system that limits both the size and frequency of your widget updates.

There are clever but unsupported hacks to create widget animations with `RemoteViews`. But now there's a flexible way to create animations with Remote Compose.

Throughout this series, we'll use two gaming widgets we've developed internally to show practical applications of Remote Compose: Android Pet and Flappy Droid. However, the code snippets are simplified to focus on the core concepts.

Android Pet is a customizable virtual pet that evolves after you take care of it. Flappy Droid is a side-scroller where the user flies between and avoids columns.

## Introducing Remote Compose

Remote Compose separates your UI definition from its execution. Your app runs your declarative `@RemoteComposable` code to serialize your layouts and animation expressions into a compact Remote Document (`ByteArray`). Android sends this document to a host process, such as the home screen launcher. In the host process, a Remote Compose player handles interactions, resizing, state changes, and animations locally. This concept is similar to a web browser (the host process with a Remote Compose player) that renders an HTML document (the Remote Document).
![diagram.png](https://developer.android.com/static/blog/assets/diagram_8a86df3751_Z2iXS8p.webp) Diagram showing app process and host process actions with Remote Compose.

Because the player manages updates independently, local to its own process, the app process doesn't need to be awake. Compared with RemoteViews-based widgets, where the app pushes UI updates, Remote Compose is efficient because it reduces the need for IPC round-trips and therefore reduces latency and battery drain. For widgets specifically, this means that once the phone's launcher receives the Remote Document, your app is free to suspend while the widget remains interactive.

Remote Documents are also small, often only a few dozen kilobytes, which is helpful when the app must emit a new Remote Document because it has new information.

This blog walks you through creating a basic Remote Compose widget and introduces two ways to manage widget state. The next two blogs dive deep into animations. The series primarily uses two Remote Compose libraries in alpha: [creation-compose](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/layout/package-summary) and the [creation](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/package-summary) library.

## Create a basic Remote Compose widget

Creating a basic Remote Compose widget follows the same steps as creating an [AppWidget](https://developer.android.com/develop/ui/views/appwidgets), except you'll use Remote Composables for your UI.

Add the [Remote Compose dependencies](https://developer.android.com/jetpack/androidx/releases/compose-remote) to your version catalog and `app/build.gradle.kts`.

`libs.versions.toml`:

```xml
[versions]
remoteCompose = "1.0.0-alpha21"

[libraries]
androidx-compose-remote-core = { group = "androidx.compose.remote", name = "remote-core", version.ref = "remoteCompose" }
androidx-compose-remote-creation = { group = "androidx.compose.remote", name = "remote-creation", version.ref = "remoteCompose" }
androidx-compose-remote-creation-compose = { group = "androidx.compose.remote", name = "remote-creation-compose", version.ref = "remoteCompose" }
```

`app/build.gradle.kts`:

```kotlin
dependencies {
    implementation(libs.androidx.compose.remote.core)
    implementation(libs.androidx.compose.remote.creation)
    implementation(libs.androidx.compose.remote.creation.compose)
}
```

In `AndroidManifest.xml`, register your receiver so your widget shows up in the system's widget picker.

Add the `android.appwidget.action.APPWIDGET_UPDATE` intent filter, which is traditionally used by the system and app to periodically refresh the widget. However, note that Remote Compose allows widgets to handle state changes locally on the host, independent of `APPWIDGET_UPDATE`.

```xml
<receiver
    android:name=".widget.MyGamingWidget"
    android:exported="true">
    <intent-filter>
        <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
    </intent-filter>
    <meta-data
        android:name="android.appwidget.provider"
        android:resource="@xml/my_gaming_widget_info" />
</receiver>
```

Add the [widget XML info](https://developer.android.com/develop/ui/compose/glance/create-app-widget#AppWidgetProviderInfo):

```xml
<?xml version="1.0" encoding="utf-8"?>
<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"
    android:description="@string/app_name"
    android:initialLayout="@android:layout/list_content"
    android:minWidth="180dp"
    android:minHeight="110dp"
    android:resizeMode="horizontal|vertical"
    android:updatePeriodMillis="0"
    android:widgetCategory="home_screen" />
```

Then have your widget class inherit from `RemoteComposeWidget`, which in turn inherits `AppWidgetProvider`. Create your custom `@RemoteComposable Content(...)` function and override `onUpdate` to compile the layout and drawing commands into a serialized binary Remote Document that is sent to the launcher via `updateRemoteView`. For widgets, Remote Compose reuses the `RemoteViews` payload as a transport mechanism to the system's launcher. However, as a developer, you don't interact with the `RemoteViews` transport mechanism directly.

Remote Compose offers several Remote Composables that are similar to regular Composables, like `RemoteBox`, `RemoteColumn`, `RemoteRow`, `RemoteText` and more from the `remote-creation-compose` library.

The below code draws a green circle against a white background, which we'll animate in the next blog posts.

```kotlin
import android.annotation.SuppressLint
import android.appwidget.AppWidgetManager
import android.content.Context
import androidx.compose.remote.creation.compose.layout.RemoteAlignment
import androidx.compose.remote.creation.compose.layout.RemoteBox
import androidx.compose.remote.creation.compose.layout.RemoteCanvas
import androidx.compose.remote.creation.compose.layout.RemoteComposable
import androidx.compose.remote.creation.compose.modifier.RemoteModifier
import androidx.compose.remote.creation.compose.modifier.background
import androidx.compose.remote.creation.compose.modifier.fillMaxSize
import androidx.compose.remote.creation.compose.state.RemotePaint
import androidx.compose.remote.creation.compose.state.rc
import androidx.compose.remote.creation.compose.widgets.RemoteComposeWidget
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

// Use @SuppressLint("RestrictedApi") to suppress warnings for non-public APIs.
// These non-public APIs can change in future releases.
@SuppressLint("RestrictedApi")
class MyGamingWidget : RemoteComposeWidget() {

    override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray
    ) {
        super.onUpdate(context, appWidgetManager, appWidgetIds)
        appWidgetIds.forEach { id ->
            // widget is inherited from RemoteComposeWidget.
            // Pass -1 as the layout ID argument to use the default layout.
            widget.updateRemoteView(context, appWidgetManager, this, id, -1)
        }
    }

    @SuppressLint("RestrictedApi")
    @RemoteComposable
    @Composable
    override fun Content(context: Context, widgetId: Int) {
        RemoteBox(
            modifier = RemoteModifier.fillMaxSize().background(Color.White.rc),
            contentAlignment = RemoteAlignment.Center
        ) {
            RemoteCanvas(modifier = RemoteModifier.fillMaxSize()) {

                val paint = RemotePaint().apply { color = Color(0xFF34A853).rc }
                drawCircle(paint = paint, radius = size.minDimension * 0.2f)
            }
        }
    }
}
```
![simpleWidget.png](https://developer.android.com/static/blog/assets/simple_Widget_859e1a215d_pEyLd.webp) A simple Remote Compose widget, ready to animate.

## Remote Document Transports

There are roughly three levels to Remote Compose: building documents, transporting documents, and playing documents on the remote host.

For mobile widgets, `RemoteComposeWidget` encapsulates code to transport documents to the launcher hosts. For Wear Widgets, `GlanceWearWidgetService` transports documents to the watch host. In essence, `RemoteComposeWidget` and `GlanceWearWidgetService` are two distinct Remote Document transport mechanisms. Separating out the transport mechanisms, which will inevitably vary across devices, allows more unified Remote Compose libraries for building and playing documents. This means, while you might swap transport mechanisms, the libraries you use to build the UI will mostly remain the same.

## Manage Widget State

When building Remote Compose widgets, you can manage state (like incrementing a counter) in two ways. The state can live locally inside the Remote Document on the host, or persist in your app's storage to be shared with your app. Use host-local state for ephemeral session state (like Flappy Droid's score) that can reset when a new document is emitted or when the launcher restarts. Use app-side persistence when the state must survive across document updates.

Android does not notify your app when the launcher restarts in the background. Instead, the system replays the last cached Remote Document, so you must use app-side persistence for any state that should not reset while the user is away.

Flappy Droid contains state entirely in the Remote Document, as seen by the incrementing score count. Android Pet shares state with the app: the user can collect gold coins from the widget by interacting with the pet, which they can spend in the app's store to buy new accessories for the pet.
![FlappyDroid (1).gif](https://developer.android.com/static/blog/assets/Flappy_Droid_1_11cc3c34e2_1Ey2Qa.webp) Flappy Droid contains state within the Remote Document

## Storing state in the Remote Document

This example shows managing state within the Remote Document. A counter increments every time the user taps on the widget.
![simplestate.gif](https://developer.android.com/static/blog/assets/simplestate_092697ceb0_rhHWf.webp) Note: The widget doesn't reset from 5 back to 0 as seen here -- the GIF is looping back to the beginning.

With Remote Compose, the host (in this case, the launcher) uses **expression graphs** with **dynamic references** to manage and update state in Remote Documents. An expression graph is essentially a mathematical formula represented as a series of connected nodes. Some nodes contain variables called dynamic references. The player (*not* the app) directly updates these dynamic references which means the app's process can sleep even while the widget UI updates. When working with Remote Compose, we indirectly create expression graphs and dynamic references.

For this example, every time the user taps:

1. The touch triggers `valueChange`: the player evaluates the `tapCountPlusOne` expression graph `(tapCount + 1.ri)` and writes the result into `tapCount`.
2. The player updates `RemoteText` with the new `tapCount` value.

```kotlin
@SuppressLint("RestrictedApi")
@RemoteComposable
@Composable
override fun Content(context: Context, widgetId: Int) {

    val tapCount = remember { MutableRemoteInt(0) }
    val tapCountPlusOne = tapCount + 1.ri // Always one more than tapCount

    RemoteBox(
        modifier = RemoteModifier
            .fillMaxSize()
            .background(Color.White.rc)
            // Update tapCount to tapCountPlusOne
            .onTouchDown(valueChange(tapCount, tapCountPlusOne)),
        contentAlignment = RemoteAlignment.Center
    ) {
        RemoteCanvas(modifier = RemoteModifier.fillMaxSize()) {
            val paint = RemotePaint().apply { color = Color(0xFF34A853).rc }
            drawCircle(paint = paint, radius = size.minDimension * 0.2f)
        }
        RemoteText(
            text = tapCount.toRemoteString(), // Display the tap count
            color = Color.White.rc,
            fontSize = 48.rsp,
            fontWeight = FontWeight.Bold
        )
    }
}
```

If you see these types, they are Remote Compose dynamic references:

- `MutableRemoteInt`
- `MutableRemoteEnum`
- `MutableRemoteLong`
- `MutableRemoteFloat`
- `MutableRemoteState`
- `MutableRemoteBoolean`
- `MutableRemoteImageBitmap`
- `MutableRemoteString`
- `MutableRemoteFloat`

As a rule of thumb, any time you create a dynamic reference and use that reference to evaluate some other value, the host is using an expression graph.

Expression graphs are the magic behind Remote Compose because they allow hosts to update state (on every device frame if required) without unnecessary app process wakeups. The next two posts talk more about animating with expression graphs.

## Sharing state with the app

This example shows how to persist the tap count to the app's storage so it can be shared with the app.
![complexstate.gif](https://developer.android.com/static/blog/assets/complexstate_37de66cf76_Z1AlyWo.webp) Note: The widget doesn't reset from 5 back to 0 as seen here -- the GIF is looping back to the beginning.

In this example, `RemoteComposeWidget` registers a `PendingIntent` broadcast for each `onClick` lambda, so your app doesn't stay running to wait for taps. When the user taps an element with an `onClick` lambda, the player sends this broadcast asynchronously and Android wakes up `RemoteComposeWidget` in your app process:

- The first `onClick` lambda updates `SharedPreferences` in the background. Afterward, `RemoteComposeWidget` automatically runs `Content()` again to read the new count and emit an updated Remote Document.
- The second `onClick` lambda (on the *Launch app* button) starts `MainActivity` in the foreground.

Notes: Unlike an `onClick` lambda, `onClick(Action)` runs an internal action in the player. Also, `onClick` functionality will likely move to another Remote Compose library in the future.

```kotlin
 import android.annotation.SuppressLint
import android.app.ActivityOptions
import android.appwidget.AppWidgetManager
import android.content.Context
import android.content.Intent
import androidx.compose.remote.creation.compose.layout.RemoteAlignment
import androidx.compose.remote.creation.compose.layout.RemoteBox
import androidx.compose.remote.creation.compose.layout.RemoteCanvas
import androidx.compose.remote.creation.compose.layout.RemoteComposable
import androidx.compose.remote.creation.compose.layout.RemoteText
import androidx.compose.remote.creation.compose.modifier.RemoteModifier
import androidx.compose.remote.creation.compose.modifier.background
import androidx.compose.remote.creation.compose.modifier.border
import androidx.compose.remote.creation.compose.modifier.clip
import androidx.compose.remote.creation.compose.modifier.fillMaxSize
import androidx.compose.remote.creation.compose.modifier.padding
import androidx.compose.remote.creation.compose.shapes.RemoteRoundedCornerShape
import androidx.compose.remote.creation.compose.state.MutableRemoteInt
import androidx.compose.remote.creation.compose.state.RemotePaint
import androidx.compose.remote.creation.compose.state.rc
import androidx.compose.remote.creation.compose.state.rdp
import androidx.compose.remote.creation.compose.state.ri
import androidx.compose.remote.creation.compose.state.rs
import androidx.compose.remote.creation.compose.state.rsp
import androidx.compose.remote.creation.compose.widgets.RemoteComposeWidget
import androidx.compose.remote.creation.compose.widgets.onClick
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.core.content.edit
import com.example.rcgamingwidgetblog.MainActivity

@SuppressLint("RestrictedApi")
class MyGamingWidget : RemoteComposeWidget() {

    override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray
    ) {
        super.onUpdate(context, appWidgetManager, appWidgetIds)
        appWidgetIds.forEach { id ->
            widget.updateRemoteView(context, appWidgetManager, this, id, -1)
        }
    }

    @SuppressLint("RestrictedApi")
    @RemoteComposable
    @Composable
    override fun Content(context: Context, widgetId: Int) {

        val buttonShape = RemoteRoundedCornerShape(12.rdp)

        RemoteBox(
            modifier = RemoteModifier
                .fillMaxSize()
                .background(Color.White.rc)
                // Persist tap count in SharedPreferences
                .onClick {
                    val currentCount = WidgetPreferences.getTapCount(context, widgetId)
                    WidgetPreferences.saveTapCount(context, widgetId, currentCount + 1) },
            contentAlignment = RemoteAlignment.Center
        ) {
            RemoteCanvas(modifier = RemoteModifier.fillMaxSize()) {
                val paint = RemotePaint().apply { color = Color(0xFF34A853).rc }
                drawCircle(paint = paint, radius = size.minDimension * 0.2f)
            }
            RemoteText(
                text = "${WidgetPreferences.getTapCount(context, widgetId)}".rs,
                color = Color.White.rc,
                fontSize = 48.rsp,
                fontWeight = FontWeight.Bold
            )
        }
        // Button to launch app
        RemoteBox(
            modifier = RemoteModifier.fillMaxSize().padding(8.rdp),
            contentAlignment = RemoteAlignment.BottomCenter
        ) {
            RemoteText(
                text = "Launch app".rs,
                color = Color.White.rc,
                fontSize = 14.rsp,
                fontWeight = FontWeight.Bold,
                modifier = RemoteModifier
                    .border(2.rdp, Color.Black.rc, buttonShape)
                    .clip(buttonShape)
                    .background(Color(0xFF34A853).rc)
                    .padding(8.rdp)
                    .onClick {
                        val intent = Intent(context, MainActivity::class.java).apply {
                            putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, widgetId)
                            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
                        }

                        val options = ActivityOptions.makeBasic()
                            .setPendingIntentBackgroundActivityStartMode(
                                ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOW_ALWAYS
                            )
                            .toBundle()
                        context.startActivity(intent, options)
                    },
            )
        }
    }
}

object WidgetPreferences {
    private const val PREFS_NAME = "gaming_widget_prefs"
    private const val KEY_PREFIX_TAP_COUNT = "tap_count_widget_"

    fun getTapCount(context: Context, widgetId: Int): Int {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        return prefs.getInt("$KEY_PREFIX_TAP_COUNT$widgetId", 0)
    }

    fun saveTapCount(context: Context, widgetId: Int, count: Int) {
        context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
            .edit {
                putInt("$KEY_PREFIX_TAP_COUNT$widgetId", count)
            }
    }
}
```

In `MainActivity`, the user can also increment the tap count in `SharedPreferences`. Because this change happens outside `RemoteComposeWidget`, `MainActivity` must send `ACTION_APPWIDGET_UPDATE` to emit a new Remote Document:

```kotlin
// THIS IS NOT REMOTE COMPOSE CODE. THIS IS APP CODE TO EMIT A NEW REMOTE DOCUMENT.
import android.appwidget.AppWidgetManager
import android.content.Context
import android.content.Intent
import androidx.compose.foundation.layout.Column
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import com.example.rcgamingwidgetblog.widget.MyGamingWidget
import com.example.rcgamingwidgetblog.widget.WidgetPreferences

@Composable
fun UpdateCount(
    widgetId: Int,
    modifier: Modifier = Modifier,
    context: Context = LocalContext.current
) {
    var currentCount by remember(widgetId) {
        mutableIntStateOf(WidgetPreferences.getTapCount(context, widgetId))
    }

    val onIncrement = remember(widgetId, context) {
        {
            currentCount += 1
            WidgetPreferences.saveTapCount(context, widgetId, currentCount)

            if (widgetId != AppWidgetManager.INVALID_APPWIDGET_ID) {
                val intent = Intent(context, MyGamingWidget::class.java).apply {
                    action = AppWidgetManager.ACTION_APPWIDGET_UPDATE
                    putExtra(AppWidgetManager.EXTRA_APPWIDGET_IDS, intArrayOf(widgetId))
                }
                context.sendBroadcast(intent)
            }
        }
    }

    Column(modifier = modifier) {
        Button(onClick = onIncrement) {
            Text("Count: $currentCount")
        }
    }
}
```

### Choosing between touch modifiers and click actions

Use `clickable(Action)` or `onTouchDown(Action)` for player-evaluated interactions, like updating tap counters via `valueChange` or triggering animations. `clickable` adds ripple feedback, whereas `onTouchDown` fires immediately without feedback.

Use `onClick { }` to run code in your app process, like launching an Activity or persisting data. Because host-side state (like `valueChange` and expression graphs seen in the next post) is isolated from your app and not directly queryable, use `onClick { }` instead to sync state with SharedPreferences or a database.

### How frequently can I update a Remote Document?

You can update a Remote Document immediately or periodically depending on what mutates the state.

- **The player can immediately update** counters, run animations, or conditionally swap layouts instantly. Because the host drives these operations, your app process never needs to wake up.
- If your app mutates shared widget state, you must emit a new Remote Document. Similar to Jetpack Glance, **your app can push updates immediately** via in-app interactions, push notifications, or broadcasts.
- If you must emit a Remote Document **periodically** while the app is asleep, you can use standard widget methods to wake up the app to update the widget, e.g. once every 30 minutes.

## **Does Remote Compose replace Jetpack Glance?**

No, Remote Compose doesn't replace Jetpack Glance. We recommend building most production widgets with Jetpack Glance, because it is backwards compatible whereas Remote Compose widgets work best on Android 17 and higher devices. Prior to Android 16, Remote Compose widgets won't work at all. Jetpack Glance also has developer tooling like Canonical Layouts that make it easier to build high quality widgets for multiple form factors.

## **What else can I use Remote Compose for?**

Today, Remote Compose is supported for building [Wear Widgets](https://developer.android.com/training/wearables/widgets) and bespoke widgets like gaming widgets. However, we expect more supported use cases to open in the future.

## **Next Steps**

The next two blog posts explore creating animations with Remote Compose. You can get started with animations using the samples in the second and third post in this series or exploring to the [AndroidX Remote Compose Repository](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/remote/) which has numerous [samples](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/remote/integration-tests/player-view-demos/src/main/java/androidx/compose/remote/integration/view/demos/) (also great context for your coding agents).

Here are the posts in this series:

- Part 2: Basic animations (to be released soon)
- Part 3: Particle animations (to be released soon)

## **Other resources**

- Remote Compose documentation (to be released soon)
- [Remote Compose Release Notes](https://developer.android.com/jetpack/androidx/releases/compose-remote)
- [Pet Android Code Sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/appwidgets) (to be fully released soon)
- [AndroidX Remote Compose Repository](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/remote/) and [samples](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/remote/integration-tests/player-view-demos/src/main/java/androidx/compose/remote/integration/view/demos/)
- John's [RemoteCompose Examples](https://hoford.github.io/RemoteCompose-Examples/index.html)
- [Remote Compose GitHub Experiments](https://github.com/camaelon/remotecompose-experiments) from Nicolas and John
- Remote Compose Talks
  - [DroidKaigi](https://2026.droidkaigi.jp/en/timetable/1235872/)
  - [Android Makers Paris](https://www.youtube.com/watch?v=2O-uClv9R3o)
  - Android Developer Summit (to be released soon)
  - [The Android Show Developers Cut](https://www.youtube.com/watch?v=g5T7Sgdgd9s)
- [#Remote Compose](https://developer.android.com/blog/topics/remote-compose)
Written by:

-

  ## [Ash Nohe](https://developer.android.com/blog/authors/ash-nohe)

  ###### Sr. Android Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ash-nohe) ![View Ash Nohe's profile](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_1SuI5e.webp) ![View Ash Nohe's profile](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_1SuI5e.webp)
-

  ## [John Hoford](https://developer.android.com/blog/authors/john-hoford)

  ###### Senior Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/john-hoford) ![View John Hoford's profile](https://developer.android.com/static/blog/assets/John_Hoford_05d5049764_xGa8q.webp) ![View John Hoford's profile](https://developer.android.com/static/blog/assets/John_Hoford_05d5049764_xGa8q.webp)
-

  ## [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight)

  ###### Senior Design Advocate

  [read_more
  View profile](https://developer.android.com/blog/authors/ivy-knight) ![View Ivy Knight's profile](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_1s13kN.webp) ![View Ivy Knight's profile](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_1s13kN.webp)
Continue reading
- [![View Thomas Ezan's profile](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_Z14J7zk.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![View Ivy Knight's profile](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_1s13kN.webp)](https://developer.android.com/blog/authors/ivy-knight) 02 Dec 2025 02 Dec 2025 ![](https://developer.android.com/static/blog/assets/sample_readme_bazel_9348d9f325_Z1WTT09.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow_forward](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app) We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.
  [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) • 2 min read
- [![View Toni Heidenreich's profile](https://developer.android.com/static/blog/assets/profile_picture_6cdbf09ec9_Z1i2yxW.webp)](https://developer.android.com/blog/authors/toni-heidenreich) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/AFD_ABL_101_Media3_1_11_is_out_Strapi_bebd1c9efc_Zpob7z.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Media3 1.11 - What's new?](https://developer.android.com/blog/posts/media3-1-11-whats-new)

  [arrow_forward](https://developer.android.com/blog/posts/media3-1-11-whats-new) Media3 1.11 is out. Powering the vast majority of top Android media apps, this release brings new features, bug fixes, and improvements across playback, editing, and UI components.
  [Toni Heidenreich](https://developer.android.com/blog/authors/toni-heidenreich) • 3 min read
  - [#Media3](https://developer.android.com/blog/topics/media3)
  - [#Jetpack](https://developer.android.com/blog/topics/jetpack)
  - [#ExoPlayer](https://developer.android.com/blog/topics/exo-player)
  - +1 ↩
- [![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_Z7OUJq.webp)](https://developer.android.com/blog/authors/caren-chang) 21 Jul 2026 21 Jul 2026 ![](https://developer.android.com/static/blog/assets/0625_Building_Jet_Packer_with_Intelligent_On_Device_features_Strapi_v02_3f5a8b17b0_1hYFMP.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: On-device inference](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our previous post we introduced Jetpacker, the demo app we'll use throughout this series.
  [Caren Chang](https://developer.android.com/blog/authors/caren-chang) • 6 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)
---
title: Toggle buttons in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/toggle-buttons
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Toggle buttons in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Display Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, a [`ToggleButton`](/reference/kotlin/androidx/xr/glimmer/ToggleButton.composable) is an interactive component
that changes its appearance based on a checked state. Toggle buttons are
optimized for display glasses to provide clear visual transitions in shape and
color. These transitions indicate when an action or setting is active.

Use toggle buttons to expose actions that can be switched on or off. Unlike
icon-only toggles, a toggle button primarily displays text content, though it
supports optional icon slots for additional context.

For other use cases, there are also [standard buttons](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons) and [icon buttons](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icon-buttons).

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_toggle_do.png)


**Figure 1.** An example of a toggle button in Jetpack Compose Glimmer used for the play and pause actions in a UI layout.

## Anatomy

A toggle button consists of a container that morphs between states and a label
with optional icons.

| Part | Description |
| --- | --- |
| Container | Animates between a circular shape (unchecked) and a rounded rectangle (checked). |
| Label | Typically a [`Text`](/reference/kotlin/androidx/xr/glimmer/Text.composable) composable. |
| Icons (optional) | Leading or trailing slots that can vary based on state. |

## Sizes

Like [standard buttons](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons), toggle buttons support two size variants:

| Size | Minimum height | Default usage |
| --- | --- | --- |
| Medium | 48.dp | Default interactive size. |
| Large | 72.dp | Primary or high-emphasis toggles. |

## Toggle button defaults

By default, toggle buttons use `ToggleButtonDefaults.animateShape`. This creates
a smooth transition between the following states:

* **Unchecked**: [`GlimmerTheme.shapes.large`](/reference/kotlin/androidx/xr/glimmer/Shapes#large()) (typically a
  [`CircleShape`](/reference/kotlin/androidx/compose/foundation/shape/package-summary#CircleShape())).
* **Checked**: `ToggleButtonDefaults.CheckedShape` (a
  [`RoundedCornerShape`](/reference/kotlin/androidx/compose/foundation/shape/package-summary#RoundedCornerShape(androidx.compose.ui.unit.Dp)) with `20.dp` corners).

The `ToggleButtonColors` class manages color resolution for the following
states:

* **Unchecked**: Defaults to [`GlimmerTheme.colors.surface`](/reference/kotlin/androidx/xr/glimmer/Colors#surface()).
* **Checked**: Defaults to [`GlimmerTheme.colors.surface`](/reference/kotlin/androidx/xr/glimmer/Colors#outline()).

### Animation

Toggle buttons use the following defaults for animation:

* `animateShape`: Provides a `Shape` that interpolates corner sizes using a
  spring animation spec (`stiffness = 600f`).
* `colors`: A factory function to customize the background and content colors
  for both states.
* `CheckedShape`: A static `RoundedCornerShape(20.dp)` used for the checked
  state.
* `contentPadding`: Inherits from [`ButtonDefaults.contentPadding`](/reference/kotlin/androidx/xr/glimmer/ButtonDefaults#contentPadding(androidx.xr.glimmer.ButtonSize)).

## Example: Toggle button

The following code creates a basic toggle button:

```
@Composable
fun ToggleButtonSample() {
    var checked by remember { mutableStateOf(false) }
    val text = if (checked) "Toggle on" else "Toggle off"

    ToggleButton(
        checked = checked,
        onCheckedChange = { checked = it }
    ) {
        Text(text)
    }
}

ToggleButtonSamples.kt
```

## Example: Toggle button with leading icon

The following code creates a toggle button with a leading icon:

```
@Composable
fun ToggleButtonWithLeadingIconSample() {
    var checked by remember { mutableStateOf(false) }

    ToggleButton(
        checked = checked,
        leadingIcon = {
            Icon(
                if (checked) FavoriteIcon else OutlinedFavoriteIcon,
                contentDescription = "Toggle favorite"
            )
        },
        onCheckedChange = { checked = it }
    ) {
        Text(if (checked) "On" else "Off")
    }
}

ToggleButtonSamples.kt
```
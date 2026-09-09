---
title: Icons in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icons
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Icons in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Display Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, the [`Icon`](/reference/kotlin/androidx/xr/glimmer/Icon.composable) component is a UI element for
rendering single-color icons. Icons intelligently handle tinting and scaling so
that they remain legible and visually consistent with the [`GlimmerTheme`](/reference/kotlin/androidx/xr/glimmer/GlimmerTheme.composable).

## Sizes

While icons default to the size provided by [`LocalIconSize`](/reference/kotlin/androidx/xr/glimmer/package-summary#LocalIconSize()), you can also
use the three icon sizes provided to set an specific size. These sizes are also
used by default for the following contexts:

| Size token | Default usage |
| --- | --- |
| `small` | For standard list items or small chips. |
| `medium` | For standalone icons and title chips. |
| `large` | For high-emphasis components like cards. |

## Icon sources

Icons can accept [`ImageVector`](/reference/kotlin/androidx/compose/ui/graphics/vector/ImageVector), [`ImageBitmap`](/reference/kotlin/androidx/compose/ui/graphics/ImageBitmap), or [`Painter`](/reference/kotlin/androidx/compose/ui/graphics/painter/Painter) as
their source. When defining your own icons, use `ImageVector` where possible to
promote sharp rendering at any scale on display glasses.

## Color and Tinting

* **Automatic tint**: The icon resolves its color based on the
  `LocalContentColor` provided by the parent surface `LocalContentColor`
  provided by the parent surface, such as a [`surface`](/reference/kotlin/androidx/xr/glimmer/surface.composable) or [`Button`](/reference/kotlin/androidx/xr/glimmer/Button.composable).
* **Manual Tinting**: Use the `tint` parameter to apply a specific color.
* **Multicolored Assets**: For icons that should not be tinted (like
  multicolored brand logos), set `tint = Color.Unspecified`.
* **Generic Images**: For photographs or generic images that don't follow icon
  sizing and tinting rules, use the standard
  [`androidx.compose.foundation.Image`](/reference/kotlin/androidx/compose/foundation/Image.composable) instead.

## Example: Basic icon

The following code creates a basic icon:

```
@Composable
fun IconSample() {
    Icon(FavoriteIcon, contentDescription = "Localized description")
}

IconSamples.kt
```

## Example: Icons with color

The following code creates a colored icon using the theme's primary color:

```
@Composable
fun ColoredIconSample() {
    Icon(
        FavoriteIcon,
        tint = GlimmerTheme.colors.primary,
        contentDescription = "Localized description",
    )
}

IconSamples.kt
```

## Example: Icons with different sizes

The following code creates a icon that is modified to be a specific size:

```
@Composable
fun SizedIconSample() {
    Icon(
        FavoriteIcon,
        contentDescription = "Localized description",
        modifier = Modifier.size(GlimmerTheme.iconSizes.large),
    )
}

IconSamples.kt
```

### Key points about the code

* The icon's size is customized using [`GlimmerTheme.iconSizes`](/reference/kotlin/androidx/xr/glimmer/IconSizes) with a
  modifier. For icons, the default value is
  [`GlimmerTheme.iconSizes.medium`](/reference/kotlin/androidx/xr/glimmer/IconSizes#medium()). Use these sizes instead of
  hard-coding values to maintain consistency across your UI.
* Provides a localized `contentDescription` for the icon. Always provide
  these descriptions unless the icon is purely decorative.
---
title: Move and clear focus  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/focus/move-focus
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Move and clear focus Stay organized with collections Save and categorize content based on your preferences.





[`FocusManager`](/reference/kotlin/androidx/compose/ui/focus/FocusManager) lets you move focus directionally or clear it entirely.
Use [`FocusRequester`](/reference/kotlin/androidx/compose/ui/focus/FocusRequester) for direct component targeting (see [Programmatically request focus](/develop/ui/compose/touch-input/focus/request-focus)).

## Directional focus movement with FocusManager

To move focus programmatically in a relative direction:

1. Obtain the `FocusManager` instance using [`LocalFocusManager.current`](/reference/kotlin/androidx/compose/ui/platform/package-summary#LocalFocusManager()).
2. Call [`moveFocus()`](/reference/kotlin/androidx/compose/ui/focus/FocusManager#moveFocus(androidx.compose.ui.focus.FocusDirection)) with a [`FocusDirection`](/reference/kotlin/androidx/compose/ui/focus/FocusDirection) value (`Next`, `Previous`,
   `Up`, `Down`, `Left`, `Right`, `Enter`, or `Exit`).

```
val focusManager = LocalFocusManager.current

Button(
    onClick = {
        focusManager.moveFocus(FocusDirection.Next)
    }
) {
    Text("Next Field")
}

MoveFocus.kt
```

## Clear focus

To remove focus from whichever element currently holds it
(for example, when the user presses the `Esc` key),
call [`clearFocus()`](/reference/kotlin/androidx/compose/ui/focus/FocusManager#clearFocus(kotlin.Boolean)):

```
val focusManager = LocalFocusManager.current

Box(
    modifier = Modifier.onPreviewKeyEvent { keyEvent ->
        if (keyEvent.key == Key.Escape && keyEvent.type == KeyEventType.KeyUp) {
            focusManager.clearFocus()
            true
        } else {
            false
        }
    }
)

MoveFocus.kt
```

The `clearFocus()` function accepts an optional `force: Boolean = false`
parameter:

* **`force = false` (default)**: Respects focus locks and will not clear focus
  if the active component has [captured focus](/develop/ui/compose/touch-input/focus/capture-and-release-focus).
* **`force = true`**: Unconditionally clears focus even if a component has
  captured focus.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Focus targets](/develop/ui/compose/touch-input/focus/focus-target)
* [Focus traversal order](/develop/ui/compose/touch-input/focus/focus-traversal)
* [Programmatically request focus](/develop/ui/compose/touch-input/focus/request-focus)

[Previous

arrow\_back

Programmatically request focus](/develop/ui/compose/touch-input/focus/request-focus)

[Next

Capture and release focus

arrow\_forward](/develop/ui/compose/touch-input/focus/capture-and-release-focus)
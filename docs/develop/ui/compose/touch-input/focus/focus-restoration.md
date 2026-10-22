---
title: Restore focus  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-restoration
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Restore focus Stay organized with collections Save and categorize content based on your preferences.





When users navigate complex user interfaces using a hardware keyboard or D-pad,
they frequently move between different sections of the screen—such as
jumping from a side navigation rail to a content list,
interacting with an item, and then jumping back.
*Focus restoration* lets containers remember
the previously focused child element and restore focus to it
when focus re-enters the container.

**Note:** This guide focuses on runtime navigation focus restoration across UI
components and containers. Preserving focus across configuration changes or
process recreation is handled through Compose's state restoration mechanisms.

## Restore focus in scrollable containers

In Jetpack Compose, scrollable containers such as [`LazyColumn`](/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)), [`LazyRow`](/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyRow(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)),
and [`LazyVerticalGrid`](/reference/kotlin/androidx/compose/foundation/lazy/grid/package-summary#LazyVerticalGrid(androidx.compose.foundation.lazy.grid.GridCells,androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.grid.LazyGridState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) automatically act as focus groups. To enable focus
restoration on a lazy list or grid, attach the [`focusRestorer`](/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).focusRestorer(kotlin.Function0)) modifier:

```
LazyColumn(
    modifier = Modifier.focusRestorer()
) {
    items(items) { item ->
        Button(onClick = { /* Handle click */ }) {
            Text(item)
        }
    }
}

FocusRestoration.kt
```

When focus exits the `LazyColumn`, the container records which item was active.
When the user navigates back into the list, focus is restored to that item
instead of restarting at the top.

## Restore focus in Row and Column

Unlike lazy layout containers, standard non-scrollable layout containers such
as [`Row`](/reference/kotlin/androidx/compose/foundation/layout/package-summary#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)) and [`Column`](/reference/kotlin/androidx/compose/foundation/layout/package-summary#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)) don't establish a focus boundary by default.
Because they don't intercept focus entry events on their own,
applying the `focusRestorer` modifier alone is not sufficient.

To enable focus restoration on `Row` or `Column`, combine [`focusGroup`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).focusGroup()) with
`focusRestorer`:

```
Row(
    modifier = Modifier
        .focusGroup()
        .focusRestorer()
) {
    Button(onClick = { /* Action 1 */ }) {
        Text("First item")
    }
    Button(onClick = { /* Action 2 */ }) {
        Text("Second item")
    }
    Button(onClick = { /* Action 3 */ }) {
        Text("Third item")
    }
}

FocusRestoration.kt
```

## Specify a fallback focus target

When focus enters a container for the first time,
no previously focused child exists.
Compose follows the default focus order to determine which child to focuses.

You can customize which child receives focus on the first entry by passing a
fallback [`FocusRequester`](/reference/kotlin/androidx/compose/ui/focus/FocusRequester) to `focusRestorer` (or a lambda returning a
`FocusRequester` on earlier Compose versions):

```
val firstItemRequester = remember { FocusRequester() }

LazyColumn(
    modifier = Modifier.focusRestorer(firstItemRequester)
) {
    itemsIndexed(items) { index, item ->
        val itemModifier = if (index == 0) {
            Modifier.focusRequester(firstItemRequester)
        } else {
            Modifier
        }
        Button(
            onClick = { /* Handle click */ },
            modifier = itemModifier
        ) {
            Text(item)
        }
    }
}

FocusRestoration.kt
```

If no child has been previously focused (or if focus restoration fails),
Compose moves focus to the associated fallback target.

## Direct focus to the selected item in navigation components

In navigation components such as [`NavigationRail`](/reference/kotlin/androidx/compose/material3/package-summary#NavigationRail(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)), [`NavigationBar`](/reference/kotlin/androidx/compose/material3/package-summary#NavigationBar(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)),
[`NavigationDrawer`](/reference/kotlin/androidx/compose/material3/package-summary#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0)), or [`TabRow`](/reference/kotlin/androidx/compose/material3/package-summary#TabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,kotlin.Function0,kotlin.Function0)), users expect focus to land on the
currently selected destination when entering the component from the content
area.

You can direct focus to the active destination by combining
`Modifier.focusGroup()` with [`focusProperties`](/reference/kotlin/androidx/compose/ui/focus/FocusProperties) and setting the [`onEnter`](/reference/kotlin/androidx/compose/ui/focus/FocusProperties#onEnter())
property (or `enter` on earlier Compose versions):

```
val (homeRequester, searchRequester, settingsRequester) = remember { FocusRequester.createRefs() }

val selectedRequester = when (currentDestination) {
    "home" -> homeRequester
    "search" -> searchRequester
    "settings" -> settingsRequester
    else -> homeRequester
}

NavigationRail(
    modifier = modifier
        .focusProperties {
            // Redirect focus to the selected item when focus enters the navigation rail
            onEnter = { selectedRequester.requestFocus() }
        }
        .focusGroup()
) {
    NavigationRailItem(
        selected = currentDestination == "home",
        onClick = { onNavigate("home") },
        icon = { Icon(Icons.Default.Home, contentDescription = "Home") },
        label = { Text("Home") },
        modifier = Modifier.focusRequester(homeRequester)
    )
    NavigationRailItem(
        selected = currentDestination == "search",
        onClick = { onNavigate("search") },
        icon = { Icon(Icons.Default.Search, contentDescription = "Search") },
        label = { Text("Search") },
        modifier = Modifier.focusRequester(searchRequester)
    )
    NavigationRailItem(
        selected = currentDestination == "settings",
        onClick = { onNavigate("settings") },
        icon = { Icon(Icons.Default.Settings, contentDescription = "Settings") },
        label = { Text("Settings") },
        modifier = Modifier.focusRequester(settingsRequester)
    )
}

FocusRestoration.kt
```

## Restore focus across screen transitions

When a user clicks an item to navigate to a detail screen and subsequently
returns using the Back button or gesture, you can restore focus to the item
they clicked.

To preserve and restore focus across screen transitions:

1. Associate the container with a `FocusRequester`.
2. Before triggering the navigation event, call [`saveFocusedChild()`](/reference/kotlin/androidx/compose/ui/focus/FocusRequester#saveFocusedChild()) on the
   container's `FocusRequester`.
3. When the user navigates back to the screen, request initial focus on the
   container or call [`restoreFocusedChild()`](/reference/kotlin/androidx/compose/ui/focus/FocusRequester#restoreFocusedChild()).

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Focus targets](/develop/ui/compose/touch-input/focus/focus-target)
* [Focus traversal order](/develop/ui/compose/touch-input/focus/focus-traversal)
* [Group focus targets](/develop/ui/compose/touch-input/focus/focus-group)
* [Programmatically request focus](/develop/ui/compose/touch-input/focus/request-focus)
* [Move and clear focus](/develop/ui/compose/touch-input/focus/move-focus)

[Previous

arrow\_back

Group focus targets](/develop/ui/compose/touch-input/focus/focus-group)

[Next

Indicate focus state

arrow\_forward](/develop/ui/compose/touch-input/focus/focused-state)
---
title: List of KTX extensions  |  Kotlin  |  Android Developers
url: https://developer.android.com/kotlin/ktx/extensions-list
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Get started](https://developer.android.com/get-started/overview)
* [Kotlin](https://developer.android.com/kotlin)
* [Guides](https://developer.android.com/kotlin/first)

# List of KTX extensions Stay organized with collections Save and categorize content based on your preferences.





## androidx.activity

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.activity:activity-ktx:1.13.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.activity:activity-ktx:1.13.0")
}
```

#### Extension functions

##### For [OnBackPressedDispatcher](/reference/kotlin/androidx/activity/OnBackPressedDispatcher)

|  |  |
| --- | --- |
| [OnBackPressedCallback](/reference/kotlin/androidx/activity/OnBackPressedCallback) | `OnBackPressedDispatcher.addCallback(owner: LifecycleOwner? = null, enabled: Boolean = true, onBackPressed: OnBackPressedCallback.() -> Unit)` Create and add a new [OnBackPressedCallback](/reference/kotlin/androidx/activity/OnBackPressedCallback) that calls [onBackPressed](#androidx.activity$addCallback(androidx.activity.OnBackPressedDispatcher, androidx.lifecycle.LifecycleOwner, kotlin.Boolean, kotlin.Function1((androidx.activity.OnBackPressedCallback, kotlin.Unit)))/onBackPressed) in [OnBackPressedCallback.handleOnBackPressed](/reference/kotlin/androidx/activity/OnBackPressedCallback#handleOnBackPressed()). |

##### For [ComponentActivity](/reference/kotlin/androidx/activity/ComponentActivity)

|  |  |
| --- | --- |
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> | `ComponentActivity.viewModels(noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the ComponentActivity's ViewModel, if [factoryProducer](#androidx.activity$viewModels(androidx.activity.ComponentActivity, kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) first time. |

## androidx.benchmark

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.5.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.5.0")
}
```

#### Top-level functions

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `beginTraceSection(sectionName: String)` |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `endTraceSection()` |

## androidx.benchmark.junit4

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.5.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.5.0")
}
```

#### Extension functions

##### For [BenchmarkRule](/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `BenchmarkRule.measureRepeated(crossinline block: BenchmarkRule.Scope.() -> Unit)` Benchmark a block of code. |

## androidx.collection

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.collection:collection-ktx:1.7.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.collection:collection-ktx:1.7.0")
}
```

#### Extension functions

##### For [LongSparseArray](/reference/kotlin/androidx/collection/LongSparseArray)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.contains(key: Long)` Returns true if the collection contains [key](#androidx.collection$contains(androidx.collection.LongSparseArray((androidx.collection.contains.T)), kotlin.Long)/key). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.forEach(action: (key: Long, value: T) -> Unit)` Performs the given [action](#androidx.collection$forEach(androidx.collection.LongSparseArray((androidx.collection.forEach.T)), kotlin.Function2((kotlin.Long, androidx.collection.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `LongSparseArray<T>.getOrDefault(key: Long, defaultValue: T)` Return the value corresponding to [key](#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)), kotlin.Long, androidx.collection.getOrDefault.T)/key), or [defaultValue](#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)), kotlin.Long, androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `LongSparseArray<T>.getOrElse(key: Long, defaultValue: () -> T)` Return the value corresponding to [key](#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) | `LongSparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](/reference/kotlin/androidx/collection/LongSparseArray)<T> | `LongSparseArray<T>.plus(other: LongSparseArray<T>)` Creates a new collection by adding or replacing entries from [other](#androidx.collection$plus(androidx.collection.LongSparseArray((androidx.collection.plus.T)), androidx.collection.LongSparseArray((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.remove(key: Long, value: T)` Removes the entry for [key](#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)), kotlin.Long, androidx.collection.remove.T)/key) only if it is mapped to [value](#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)), kotlin.Long, androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.set(key: Long, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> | `LongSparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [SparseArrayCompat](/reference/kotlin/androidx/collection/SparseArrayCompat)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArrayCompat<T>.contains(key: Int)` Returns true if the collection contains [key](#androidx.collection$contains(androidx.collection.SparseArrayCompat((androidx.collection.contains.T)), kotlin.Int)/key). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArrayCompat<T>.forEach(action: (key: Int, value: T) -> Unit)` Performs the given [action](#androidx.collection$forEach(androidx.collection.SparseArrayCompat((androidx.collection.forEach.T)), kotlin.Function2((kotlin.Int, androidx.collection.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `SparseArrayCompat<T>.getOrDefault(key: Int, defaultValue: T)` Return the value corresponding to [key](#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)), kotlin.Int, androidx.collection.getOrDefault.T)/key), or [defaultValue](#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)), kotlin.Int, androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `SparseArrayCompat<T>.getOrElse(key: Int, defaultValue: () -> T)` Return the value corresponding to [key](#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArrayCompat<T>.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseArrayCompat<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseArrayCompat](/reference/kotlin/androidx/collection/SparseArrayCompat)<T> | `SparseArrayCompat<T>.plus(other: SparseArrayCompat<T>)` Creates a new collection by adding or replacing entries from [other](#androidx.collection$plus(androidx.collection.SparseArrayCompat((androidx.collection.plus.T)), androidx.collection.SparseArrayCompat((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArrayCompat<T>.remove(key: Int, value: T)` Removes the entry for [key](#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)), kotlin.Int, androidx.collection.remove.T)/key) only if it is mapped to [value](#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)), kotlin.Int, androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArrayCompat<T>.set(key: Int, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> | `SparseArrayCompat<T>.valueIterator()` Return an iterator over the collection's values. |

#### Extension properties

##### For [LongSparseArray](/reference/kotlin/androidx/collection/LongSparseArray)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `LongSparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [SparseArrayCompat](/reference/kotlin/androidx/collection/SparseArrayCompat)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseArrayCompat<T>.size()` Returns the number of key/value pairs in the collection. |

#### Top-level functions

|  |  |
| --- | --- |
| [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap)<K, V> | `arrayMapOf()` Returns an empty new [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap). |
| [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap)<K, V> | `arrayMapOf(vararg pairs: Pair<K, V>)` Returns a new [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap) with the specified contents, given as a list of pairs where the first component is the key and the second component is the value. |
| [ArraySet](/reference/kotlin/androidx/collection/ArraySet)<T> | `arraySetOf()` Returns an empty new [ArraySet](/reference/kotlin/androidx/collection/ArraySet). |
| [ArraySet](/reference/kotlin/androidx/collection/ArraySet)<T> | `arraySetOf(vararg values: T)` Returns a new [ArraySet](/reference/kotlin/androidx/collection/ArraySet) with the specified contents. |
| [LruCache](/reference/kotlin/androidx/collection/LruCache)<K, V> | `lruCache(maxSize: Int, crossinline sizeOf: (key: K, value: V) -> Int = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: Boolean, key: K, oldValue: V, newValue: V?) -> Unit = { _, _, _, _ -> })` Creates an [LruCache](/reference/kotlin/androidx/collection/LruCache) with the given parameters. |

## androidx.core.animation

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.animation.Animator](/reference/android/animation/Animator)

|  |  |
| --- | --- |
| [AnimatorListener](/reference/android/animation/Animator.AnimatorListener) | `Animator.addListener(crossinline onEnd: (animator: Animator) -> Unit = {}, crossinline onStart: (animator: Animator) -> Unit = {}, crossinline onCancel: (animator: Animator) -> Unit = {}, crossinline onRepeat: (animator: Animator) -> Unit = {})` Add a listener to this Animator using the provided actions. |
| [AnimatorPauseListener](/reference/android/animation/Animator.AnimatorPauseListener) | `Animator.addPauseListener(crossinline onResume: (animator: Animator) -> Unit = {}, crossinline onPause: (animator: Animator) -> Unit = {})` Add a pause and resume listener to this Animator using the provided actions. |
| [AnimatorListener](/reference/android/animation/Animator.AnimatorListener) | `Animator.doOnCancel(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has been cancelled. |
| [AnimatorListener](/reference/android/animation/Animator.AnimatorListener) | `Animator.doOnEnd(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has ended. |
| [AnimatorPauseListener](/reference/android/animation/Animator.AnimatorPauseListener) | `Animator.doOnPause(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has been paused. |
| [AnimatorListener](/reference/android/animation/Animator.AnimatorListener) | `Animator.doOnRepeat(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has repeated. |
| [AnimatorPauseListener](/reference/android/animation/Animator.AnimatorPauseListener) | `Animator.doOnResume(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has resumed after a pause. |
| [AnimatorListener](/reference/android/animation/Animator.AnimatorListener) | `Animator.doOnStart(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has started. |

## androidx.core.content

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.content.Context](/reference/android/content/Context)

|  |  |
| --- | --- |
| T? | `Context.getSystemService()` Return the handle to a system-level service by class. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Context.withStyledAttributes(set: AttributeSet? = null, attrs: IntArray, @AttrRes defStyleAttr: Int = 0, @StyleRes defStyleRes: Int = 0, block: TypedArray.() -> Unit)` Executes [block](#androidx.core.content$withStyledAttributes(android.content.Context, android.util.AttributeSet, kotlin.IntArray, kotlin.Int, kotlin.Int, kotlin.Function1((android.content.res.TypedArray, kotlin.Unit)))/block) on a [TypedArray](/reference/android/content/res/TypedArray) receiver. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Context.withStyledAttributes(@StyleRes resourceId: Int, attrs: IntArray, block: TypedArray.() -> Unit)` Executes [block](#androidx.core.content$withStyledAttributes(android.content.Context, kotlin.Int, kotlin.IntArray, kotlin.Function1((android.content.res.TypedArray, kotlin.Unit)))/block) on a [TypedArray](/reference/android/content/res/TypedArray) receiver. |

##### For [android.content.SharedPreferences](/reference/android/content/SharedPreferences)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SharedPreferences.edit(commit: Boolean = false, action: Editor.() -> Unit)` Allows editing of this preference instance with a call to [apply](/reference/android/content/SharedPreferences.Editor#apply()) or [commit](/reference/android/content/SharedPreferences.Editor#commit()) to persist the changes. |

#### Top-level functions

|  |  |
| --- | --- |
| [ContentValues](/reference/android/content/ContentValues) | `contentValuesOf(vararg pairs: Pair<String, Any?>)` Returns a new [ContentValues](/reference/android/content/ContentValues) with the given key/value pairs as elements. |

## androidx.core.content.res

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.content.res.TypedArray](/reference/android/content/res/TypedArray)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `TypedArray.getBooleanOrThrow(@StyleableRes index: Int)` Retrieve the boolean value for the attribute at [index](#androidx.core.content.res$getBooleanOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getColorOrThrow(@StyleableRes index: Int)` Retrieve the color value for the attribute at [index](#androidx.core.content.res$getColorOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [ColorStateList](/reference/android/content/res/ColorStateList) | `TypedArray.getColorStateListOrThrow(@StyleableRes index: Int)` Retrieve the color state list value for the attribute at [index](#androidx.core.content.res$getColorStateListOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `TypedArray.getDimensionOrThrow(@StyleableRes index: Int)` Retrieve the dimension value for the attribute at [index](#androidx.core.content.res$getDimensionOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getDimensionPixelOffsetOrThrow(@StyleableRes index: Int)` Retrieve the dimension pixel offset value for the attribute at [index](#androidx.core.content.res$getDimensionPixelOffsetOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getDimensionPixelSizeOrThrow(@StyleableRes index: Int)` Retrieve the dimension pixel size value for the attribute at [index](#androidx.core.content.res$getDimensionPixelSizeOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Drawable](/reference/android/graphics/drawable/Drawable) | `TypedArray.getDrawableOrThrow(@StyleableRes index: Int)` Retrieve the drawable value for the attribute at [index](#androidx.core.content.res$getDrawableOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `TypedArray.getFloatOrThrow(@StyleableRes index: Int)` Retrieve the float value for the attribute at [index](#androidx.core.content.res$getFloatOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Typeface](/reference/android/graphics/Typeface) | `TypedArray.getFontOrThrow(@StyleableRes index: Int)` Retrieve the font value for the attribute at [index](#androidx.core.content.res$getFontOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getIntOrThrow(@StyleableRes index: Int)` Retrieve the integer value for the attribute at [index](#androidx.core.content.res$getIntOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getIntegerOrThrow(@StyleableRes index: Int)` Retrieve the integer value for the attribute at [index](#androidx.core.content.res$getIntegerOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getResourceIdOrThrow(@StyleableRes index: Int)` Retrieves the resource identifier for the attribute at [index](#androidx.core.content.res$getResourceIdOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `TypedArray.getStringOrThrow(@StyleableRes index: Int)` Retrieve the string value for the attribute at [index](#androidx.core.content.res$getStringOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/)<[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)> | `TypedArray.getTextArrayOrThrow(@StyleableRes index: Int)` Retrieve the text array value for the attribute at [index](#androidx.core.content.res$getTextArrayOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) | `TypedArray.getTextOrThrow(@StyleableRes index: Int)` Retrieve the text value for the attribute at [index](#androidx.core.content.res$getTextOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| R | `TypedArray.use(block: (TypedArray) -> R)` Executes the given [block](#androidx.core.content.res$use(android.content.res.TypedArray, kotlin.Function1((android.content.res.TypedArray, androidx.core.content.res.use.R)))/block) function on this TypedArray and then recycles it. |

## androidx.core.database

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.database.Cursor](/reference/android/database/Cursor)

|  |  |
| --- | --- |
| [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/)? | `Cursor.getBlobOrNull(index: Int)` Returns the value of the requested column as a nullable byte array. |
| [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/)? | `Cursor.getDoubleOrNull(index: Int)` Returns the value of the requested column as a nullable double. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)? | `Cursor.getFloatOrNull(index: Int)` Returns the value of the requested column as a nullable float. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)? | `Cursor.getIntOrNull(index: Int)` Returns the value of the requested column as a nullable integer. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)? | `Cursor.getLongOrNull(index: Int)` Returns the value of the requested column as a nullable long. |
| [Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/)? | `Cursor.getShortOrNull(index: Int)` Returns the value of the requested column as a nullable short. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)? | `Cursor.getStringOrNull(index: Int)` Returns the value of the requested column as a nullable string. |

## androidx.core.database.sqlite

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.database.sqlite.SQLiteDatabase](/reference/android/database/sqlite/SQLiteDatabase)

|  |  |
| --- | --- |
| T | `SQLiteDatabase.transaction(exclusive: Boolean = true, body: SQLiteDatabase.() -> T)` Run [body](#androidx.core.database.sqlite$transaction(android.database.sqlite.SQLiteDatabase, kotlin.Boolean, kotlin.Function1((android.database.sqlite.SQLiteDatabase, androidx.core.database.sqlite.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.core.graphics

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](/reference/android/graphics/Bitmap)

|  |  |
| --- | --- |
| [Bitmap](/reference/android/graphics/Bitmap) | `Bitmap.applyCanvas(block: Canvas.() -> Unit)` Creates a new [Canvas](/reference/android/graphics/Canvas) to draw on this bitmap and executes the specified [block](#androidx.core.graphics$applyCanvas(android.graphics.Bitmap, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) on the newly created canvas. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Bitmap.contains(p: Point)` Returns true if the specified point is inside the bitmap. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Bitmap.contains(p: PointF)` Returns true if the specified point is inside the bitmap. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Bitmap.get(x: Int, y: Int)` Returns the value of the pixel at the specified location. |
| [Bitmap](/reference/android/graphics/Bitmap) | `Bitmap.scale(width: Int, height: Int, filter: Boolean = true)` Creates a new bitmap, scaled from this bitmap, when possible. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Bitmap.set(x: Int, y: Int, color: Int)` Writes the specified [color int](/reference/android/graphics/Color) into the bitmap (assuming it is mutable) at the specified `(x, y)` coordinate. |

##### For [android.graphics.Canvas](/reference/android/graphics/Canvas)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(clipRect: Rect, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withClip(android.graphics.Canvas, android.graphics.Rect, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.clipRect](/reference/android/graphics/Canvas#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(clipRect: RectF, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withClip(android.graphics.Canvas, android.graphics.RectF, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.clipRect](/reference/android/graphics/Canvas#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(left: Int, top: Int, right: Int, bottom: Int, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withClip(android.graphics.Canvas, kotlin.Int, kotlin.Int, kotlin.Int, kotlin.Int, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.clipRect](/reference/android/graphics/Canvas#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(left: Float, top: Float, right: Float, bottom: Float, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withClip(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.clipRect](/reference/android/graphics/Canvas#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(clipPath: Path, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withClip(android.graphics.Canvas, android.graphics.Path, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.clipPath](/reference/android/graphics/Canvas#clipPath(android.graphics.Path,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withMatrix(matrix: Matrix = Matrix(), block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withMatrix(android.graphics.Canvas, android.graphics.Matrix, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.concat](/reference/android/graphics/Canvas#concat(android.graphics.Matrix)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withRotation(degrees: Float = 0.0f, pivotX: Float = 0.0f, pivotY: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withRotation(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.rotate](/reference/android/graphics/Canvas#rotate(float)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withSave(block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withSave(android.graphics.Canvas, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save()) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withScale(x: Float = 1.0f, y: Float = 1.0f, pivotX: Float = 0.0f, pivotY: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withScale(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.scale](/reference/android/graphics/Canvas#scale(float,%20float)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withSkew(x: Float = 0.0f, y: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withSkew(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.skew](/reference/android/graphics/Canvas#skew(float,%20float)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withTranslation(x: Float = 0.0f, y: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$withTranslation(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](/reference/android/graphics/Canvas#save())/[Canvas.translate](/reference/android/graphics/Canvas#translate(float,%20float)) and [Canvas.restoreToCount](/reference/android/graphics/Canvas#restoreToCount(int)). |

##### For [android.graphics.Color](/reference/android/graphics/Color)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component1()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component2()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component3()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component4()` Returns the fourth component of the color. |
| infix [Color](/reference/android/graphics/Color)! | `Color.convertTo(colorSpace: Named)` Converts the color receiver to a color in the specified color space. |
| infix [Color](/reference/android/graphics/Color)! | `Color.convertTo(colorSpace: ColorSpace)` Converts the color receiver to a color in the specified color space. |
| operator [Color](/reference/android/graphics/Color) | `Color.plus(c: Color)` Composites two translucent colors together. |

##### For [android.graphics.ImageDecoder.Source](/reference/android/graphics/ImageDecoder.Source)

|  |  |
| --- | --- |
| [Bitmap](/reference/android/graphics/Bitmap) | `Source.decodeBitmap(crossinline action: ImageDecoder.(info: ImageInfo, source: Source) -> Unit)` Create a Bitmap from a Source |
| [Drawable](/reference/android/graphics/drawable/Drawable) | `Source.decodeDrawable(crossinline action: ImageDecoder.(info: ImageInfo, source: Source) -> Unit)` Create a Drawable from a Source |

##### For [android.graphics.Matrix](/reference/android/graphics/Matrix)

|  |  |
| --- | --- |
| operator [Matrix](/reference/android/graphics/Matrix) | `Matrix.times(m: Matrix)` Multiplies this [Matrix](/reference/android/graphics/Matrix) by another matrix and returns the result as a new matrix. |
| [FloatArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array/) | `Matrix.values()` Returns the 9 values of this [Matrix](/reference/android/graphics/Matrix) as a new array of floats. |

##### For [android.graphics.Paint](/reference/android/graphics/Paint)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Paint.setBlendMode(blendModeCompat: BlendModeCompat?)` Convenience method to configure the BlendMode of a Paint in a backward compatible way. |

##### For [android.graphics.Path](/reference/android/graphics/Path)

|  |  |
| --- | --- |
| infix [Path](/reference/android/graphics/Path) | `Path.and(p: Path)` Returns the intersection of two paths as a new [Path](/reference/android/graphics/Path). |
| [Iterable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/)<[PathSegment](/reference/kotlin/androidx/core/graphics/PathSegment)> | `Path.flatten(error: Float = 0.5f)` Flattens (or approximate) the [Path](/reference/android/graphics/Path) with a series of line segments. |
| operator [Path](/reference/android/graphics/Path) | `Path.minus(p: Path)` Returns the difference of two paths as a new [Path](/reference/android/graphics/Path). |
| infix [Path](/reference/android/graphics/Path) | `Path.or(p: Path)` Returns the union of two paths as a new [Path](/reference/android/graphics/Path). |
| operator [Path](/reference/android/graphics/Path) | `Path.plus(p: Path)` Returns the union of two paths as a new [Path](/reference/android/graphics/Path). |
| infix [Path](/reference/android/graphics/Path) | `Path.xor(p: Path)` Returns the union minus the intersection of two paths as a new [Path](/reference/android/graphics/Path). |

##### For [android.graphics.Picture](/reference/android/graphics/Picture)

|  |  |
| --- | --- |
| [Picture](/reference/android/graphics/Picture) | `Picture.record(width: Int, height: Int, block: Canvas.() -> Unit)` Creates a new [Canvas](/reference/android/graphics/Canvas) to record commands in this [Picture](/reference/android/graphics/Picture), executes the specified [block](#androidx.core.graphics$record(android.graphics.Picture, kotlin.Int, kotlin.Int, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) on the newly created canvas and returns this [Picture](/reference/android/graphics/Picture). |

##### For [android.graphics.Point](/reference/android/graphics/Point)

|  |  |
| --- | --- |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Point.component1()` Returns the x coordinate of this point. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Point.component2()` Returns the y coordinate of this point. |
| operator [Point](/reference/android/graphics/Point) | `Point.minus(p: Point)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [Point](/reference/android/graphics/Point) | `Point.minus(xy: Int)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [Point](/reference/android/graphics/Point) | `Point.plus(p: Point)` Offsets this point by the specified point and returns the result as a new point. |
| operator [Point](/reference/android/graphics/Point) | `Point.plus(xy: Int)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [PointF](/reference/android/graphics/PointF) | `Point.toPointF()` Returns a [PointF](/reference/android/graphics/PointF) representation of this point. |
| operator [Point](/reference/android/graphics/Point) | `Point.unaryMinus()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PointF](/reference/android/graphics/PointF)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `PointF.component1()` Returns the x coordinate of this point. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `PointF.component2()` Returns the y coordinate of this point. |
| operator [PointF](/reference/android/graphics/PointF) | `PointF.minus(p: PointF)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [PointF](/reference/android/graphics/PointF) | `PointF.minus(xy: Float)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [PointF](/reference/android/graphics/PointF) | `PointF.plus(p: PointF)` Offsets this point by the specified point and returns the result as a new point. |
| operator [PointF](/reference/android/graphics/PointF) | `PointF.plus(xy: Float)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [Point](/reference/android/graphics/Point) | `PointF.toPoint()` Returns a [Point](/reference/android/graphics/Point) representation of this point. |
| operator [PointF](/reference/android/graphics/PointF) | `PointF.unaryMinus()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PorterDuff.Mode](/reference/android/graphics/PorterDuff.Mode)

|  |  |
| --- | --- |
| [PorterDuffColorFilter](/reference/android/graphics/PorterDuffColorFilter) | `Mode.toColorFilter(color: Int)` Creates a new [PorterDuffColorFilter](/reference/android/graphics/PorterDuffColorFilter) that uses this [PorterDuff.Mode](/reference/android/graphics/PorterDuff.Mode) as the alpha compositing or blending mode, and the specified [color](#androidx.core.graphics$toColorFilter(android.graphics.PorterDuff.Mode, kotlin.Int)/color). |
| [PorterDuffXfermode](/reference/android/graphics/PorterDuffXfermode) | `Mode.toXfermode()` Creates a new [PorterDuffXfermode](/reference/android/graphics/PorterDuffXfermode) that uses this [PorterDuff.Mode](/reference/android/graphics/PorterDuff.Mode) as the alpha compositing or blending mode. |

##### For [android.graphics.Rect](/reference/android/graphics/Rect)

|  |  |
| --- | --- |
| infix [Rect](/reference/android/graphics/Rect) | `Rect.and(r: Rect)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component1()` Returns "left", the first component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component2()` Returns "top", the second component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component3()` Returns "right", the third component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component4()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Rect.contains(p: Point)` Returns true if the specified point is inside the rectangle. |
| operator [Region](/reference/android/graphics/Region) | `Rect.minus(r: Rect)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [Rect](/reference/android/graphics/Rect) | `Rect.minus(xy: Int)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [Rect](/reference/android/graphics/Rect) | `Rect.minus(xy: Point)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [Rect](/reference/android/graphics/Rect) | `Rect.or(r: Rect)` Returns the union of two rectangles as a new rectangle. |
| operator [Rect](/reference/android/graphics/Rect) | `Rect.plus(r: Rect)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [Rect](/reference/android/graphics/Rect) | `Rect.plus(xy: Int)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [Rect](/reference/android/graphics/Rect) | `Rect.plus(xy: Point)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [Rect](/reference/android/graphics/Rect) | `Rect.times(factor: Int)` Returns a new rectangle representing this rectangle's components each scaled by [factor](#androidx.core.graphics$times(android.graphics.Rect, kotlin.Int)/factor). |
| [RectF](/reference/android/graphics/RectF) | `Rect.toRectF()` Returns a [RectF](/reference/android/graphics/RectF) representation of this rectangle. |
| [Region](/reference/android/graphics/Region) | `Rect.toRegion()` Returns a [Region](/reference/android/graphics/Region) representation of this rectangle. |
| infix [Region](/reference/android/graphics/Region) | `Rect.xor(r: Rect)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.RectF](/reference/android/graphics/RectF)

|  |  |
| --- | --- |
| infix [RectF](/reference/android/graphics/RectF) | `RectF.and(r: RectF)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component1()` Returns "left", the first component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component2()` Returns "top", the second component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component3()` Returns "right", the third component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component4()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `RectF.contains(p: PointF)` Returns true if the specified point is inside the rectangle. |
| operator [Region](/reference/android/graphics/Region) | `RectF.minus(r: RectF)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [RectF](/reference/android/graphics/RectF) | `RectF.minus(xy: Float)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [RectF](/reference/android/graphics/RectF) | `RectF.minus(xy: PointF)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [RectF](/reference/android/graphics/RectF) | `RectF.or(r: RectF)` Returns the union of two rectangles as a new rectangle. |
| operator [RectF](/reference/android/graphics/RectF) | `RectF.plus(r: RectF)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [RectF](/reference/android/graphics/RectF) | `RectF.plus(xy: Float)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [RectF](/reference/android/graphics/RectF) | `RectF.plus(xy: PointF)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [RectF](/reference/android/graphics/RectF) | `RectF.times(factor: Int)` Returns a new rectangle representing this rectangle's components each scaled by [factor](#androidx.core.graphics$times(android.graphics.RectF, kotlin.Int)/factor). |
| operator [RectF](/reference/android/graphics/RectF) | `RectF.times(factor: Float)` Returns a new rectangle representing this rectangle's components each scaled by [factor](#androidx.core.graphics$times(android.graphics.RectF, kotlin.Float)/factor). |
| [Rect](/reference/android/graphics/Rect) | `RectF.toRect()` Returns a [Rect](/reference/android/graphics/Rect) representation of this rectangle. |
| [Region](/reference/android/graphics/Region) | `RectF.toRegion()` Returns a [Region](/reference/android/graphics/Region) representation of this rectangle. |
| [RectF](/reference/android/graphics/RectF) | `RectF.transform(m: Matrix)` Transform this rectangle in place using the supplied [Matrix](/reference/android/graphics/Matrix) and returns this rectangle. |
| infix [Region](/reference/android/graphics/Region) | `RectF.xor(r: RectF)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.Region](/reference/android/graphics/Region)

|  |  |
| --- | --- |
| infix [Region](/reference/android/graphics/Region) | `Region.and(r: Rect)` Return the intersection of this region and the specified [Rect](/reference/android/graphics/Rect) as a new region. |
| infix [Region](/reference/android/graphics/Region) | `Region.and(r: Region)` Return the intersection of this region and the specified region as a new region. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Region.contains(p: Point)` Return true if the region contains the specified [Point](/reference/android/graphics/Point). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Region.forEach(action: (rect: Rect) -> Unit)` Performs the given action on each rect in this region. |
| operator [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<[Rect](/reference/android/graphics/Rect)> | `Region.iterator()` Returns an [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/) over the rects in this region. |
| operator [Region](/reference/android/graphics/Region) | `Region.minus(r: Rect)` Return the difference of this region and the specified [Rect](/reference/android/graphics/Rect) as a new region. |
| operator [Region](/reference/android/graphics/Region) | `Region.minus(r: Region)` Return the difference of this region and the specified region as a new region. |
| operator [Region](/reference/android/graphics/Region) | `Region.not()` Returns the negation of this region as a new region. |
| infix [Region](/reference/android/graphics/Region) | `Region.or(r: Rect)` Return the union of this region and the specified [Rect](/reference/android/graphics/Rect) as a new region. |
| infix [Region](/reference/android/graphics/Region) | `Region.or(r: Region)` Return the union of this region and the specified region as a new region. |
| operator [Region](/reference/android/graphics/Region) | `Region.plus(r: Rect)` Return the union of this region and the specified [Rect](/reference/android/graphics/Rect) as a new region. |
| operator [Region](/reference/android/graphics/Region) | `Region.plus(r: Region)` Return the union of this region and the specified region as a new region. |
| operator [Region](/reference/android/graphics/Region) | `Region.unaryMinus()` Returns the negation of this region as a new region. |
| infix [Region](/reference/android/graphics/Region) | `Region.xor(r: Rect)` Return the union minus the intersection of this region and the specified [Rect](/reference/android/graphics/Rect) as a new region. |
| infix [Region](/reference/android/graphics/Region) | `Region.xor(r: Region)` Return the union minus the intersection of this region and the specified region as a new region. |

##### For [android.graphics.Shader](/reference/android/graphics/Shader)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Shader.transform(block: Matrix.() -> Unit)` Wrap the specified [block](#androidx.core.graphics$transform(android.graphics.Shader, kotlin.Function1((android.graphics.Matrix, kotlin.Unit)))/block) in calls to [Shader.getLocalMatrix](/reference/android/graphics/Shader#getLocalMatrix(android.graphics.Matrix)) and [Shader.setLocalMatrix](/reference/android/graphics/Shader#setLocalMatrix(android.graphics.Matrix)). |

##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

|  |  |
| --- | --- |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component1()` Return the alpha component of a color int. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component2()` Return the red component of a color int. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component3()` Return the green component of a color int. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component4()` Return the blue component of a color int. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Int.convertTo(colorSpace: Named)` Converts the color int receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Int.convertTo(colorSpace: ColorSpace)` Converts the color int receiver to a color long in the specified color space. |
| [Color](/reference/android/graphics/Color) | `Int.toColor()` Creates a new [Color](/reference/android/graphics/Color) instance from a color int. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Int.toColorLong()` Converts the specified ARGB [color int](/reference/android/graphics/Color) to an RGBA [color long](/reference/android/graphics/Color) in the [sRGB](/reference/android/graphics/ColorSpace.Named#SRGB) color space. |

##### For [kotlin.Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component1()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component2()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component3()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component4()` Returns the fourth component of the color. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Long.convertTo(colorSpace: Named)` Converts the color long receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Long.convertTo(colorSpace: ColorSpace)` Converts the color long receiver to a color long in the specified color space. |
| [Color](/reference/android/graphics/Color) | `Long.toColor()` Creates a new [Color](/reference/android/graphics/Color) instance from a [color long](/reference/android/graphics/Color). |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Long.toColorInt()` Converts the specified [color long](/reference/android/graphics/Color) to an ARGB [color int](/reference/android/graphics/Color). |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `String.toColorInt()` Return a corresponding [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) color of this [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/). |

#### Extension properties

##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.alpha()` Return the alpha component of a color int. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.blue()` Return the blue component of a color int. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.green()` Return the green component of a color int. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Int.luminance()` Returns the relative luminance of a color int, assuming sRGB encoding. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.red()` Return the red component of a color int. |

##### For [kotlin.Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)

|  |  |
| --- | --- |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.alpha()` Return the alpha component of a color long. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.blue()` Return the blue component of a color long. |
| [ColorSpace](/reference/android/graphics/ColorSpace) | `Long.colorSpace()` Returns the color space encoded in the specified color long. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.green()` Return the green component of a color long. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Long.isSrgb()` Indicates whether the color is in the [sRGB](/reference/android/graphics/ColorSpace.Named#SRGB) color space. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Long.isWideGamut()` Indicates whether the color is in a [wide-gamut](/reference/android/graphics/ColorSpace) color space. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.luminance()` Returns the relative luminance of a color. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.red()` Return the red component of a color long. |

#### Top-level functions

|  |  |
| --- | --- |
| [Bitmap](/reference/android/graphics/Bitmap) | `createBitmap(width: Int, height: Int, config: Config = Bitmap.Config.ARGB_8888)` Returns a mutable bitmap with the specified [width](#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config)/width) and [height](#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config)/height). |
| [Bitmap](/reference/android/graphics/Bitmap) | `createBitmap(width: Int, height: Int, config: Config = Bitmap.Config.ARGB_8888, hasAlpha: Boolean = true, colorSpace: ColorSpace = ColorSpace.get(ColorSpace.Named.SRGB))` Returns a mutable bitmap with the specified [width](#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config, kotlin.Boolean, android.graphics.ColorSpace)/width) and [height](#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config, kotlin.Boolean, android.graphics.ColorSpace)/height). |
| [Matrix](/reference/android/graphics/Matrix) | `rotationMatrix(degrees: Float, px: Float = 0.0f, py: Float = 0.0f)` Creates a rotation matrix, defined by a rotation angle in degrees around the pivot point located at the coordinates ([px](#androidx.core.graphics$rotationMatrix(kotlin.Float, kotlin.Float, kotlin.Float)/px), [py](#androidx.core.graphics$rotationMatrix(kotlin.Float, kotlin.Float, kotlin.Float)/py)). |
| [Matrix](/reference/android/graphics/Matrix) | `scaleMatrix(sx: Float = 1.0f, sy: Float = 1.0f)` Creates a scale matrix with the scale factor [sx](#androidx.core.graphics$scaleMatrix(kotlin.Float, kotlin.Float)/sx) and [sy](#androidx.core.graphics$scaleMatrix(kotlin.Float, kotlin.Float)/sy) respectively on the `x` and `y` axis. |
| [Matrix](/reference/android/graphics/Matrix) | `translationMatrix(tx: Float = 0.0f, ty: Float = 0.0f)` Creates a translation matrix with the translation amounts [tx](#androidx.core.graphics$translationMatrix(kotlin.Float, kotlin.Float)/tx) and [ty](#androidx.core.graphics$translationMatrix(kotlin.Float, kotlin.Float)/ty) respectively on the `x` and `y` axis. |

## androidx.core.graphics.drawable

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](/reference/android/graphics/Bitmap)

|  |  |
| --- | --- |
| [Icon](/reference/android/graphics/drawable/Icon) | `Bitmap.toAdaptiveIcon()` Create an [Icon](/reference/android/graphics/drawable/Icon) from this adaptive [Bitmap](/reference/android/graphics/Bitmap). |
| [BitmapDrawable](/reference/android/graphics/drawable/BitmapDrawable) | `Bitmap.toDrawable(resources: Resources)` Create a [BitmapDrawable](/reference/android/graphics/drawable/BitmapDrawable) from this [Bitmap](/reference/android/graphics/Bitmap). |
| [Icon](/reference/android/graphics/drawable/Icon) | `Bitmap.toIcon()` Create an [Icon](/reference/android/graphics/drawable/Icon) from this [Bitmap](/reference/android/graphics/Bitmap). |

##### For [android.graphics.Color](/reference/android/graphics/Color)

|  |  |
| --- | --- |
| [ColorDrawable](/reference/android/graphics/drawable/ColorDrawable) | `Color.toDrawable()` Create a [ColorDrawable](/reference/android/graphics/drawable/ColorDrawable) from this [Color](/reference/android/graphics/Color) (via [Color.toArgb](/reference/android/graphics/Color#toArgb())). |

##### For [android.graphics.drawable.Drawable](/reference/android/graphics/drawable/Drawable)

|  |  |
| --- | --- |
| [Bitmap](/reference/android/graphics/Bitmap) | `Drawable.toBitmap(@Px width: Int = intrinsicWidth, @Px height: Int = intrinsicHeight, config: Config? = null)` Return a [Bitmap](/reference/android/graphics/Bitmap) representation of this [Drawable](/reference/android/graphics/drawable/Drawable). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Drawable.updateBounds(@Px left: Int = bounds.left, @Px top: Int = bounds.top, @Px right: Int = bounds.right, @Px bottom: Int = bounds.bottom)` Updates this drawable's bounds. |

##### For [android.net.Uri](/reference/android/net/Uri)

|  |  |
| --- | --- |
| [Icon](/reference/android/graphics/drawable/Icon) | `Uri.toIcon()` Create an [Icon](/reference/android/graphics/drawable/Icon) from this [Uri](/reference/android/net/Uri). |

##### For [kotlin.ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/)

|  |  |
| --- | --- |
| [Icon](/reference/android/graphics/drawable/Icon) | `ByteArray.toIcon()` Create an [Icon](/reference/android/graphics/drawable/Icon) from this [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/). |

##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

|  |  |
| --- | --- |
| [ColorDrawable](/reference/android/graphics/drawable/ColorDrawable) | `Int.toDrawable()` Create a [ColorDrawable](/reference/android/graphics/drawable/ColorDrawable) from this color value. |

## androidx.core.location

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.location.Location](/reference/android/location/Location)

|  |  |
| --- | --- |
| operator [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/) | `Location.component1()` Returns the latitude of this [Location](/reference/android/location/Location). |
| operator [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/) | `Location.component2()` Returns the longitude of this [Location](/reference/android/location/Location). |

## androidx.core.net

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.net.Uri](/reference/android/net/Uri)

|  |  |
| --- | --- |
| [File](/reference/java/io/File) | `Uri.toFile()` Creates a [File](/reference/java/io/File) from the given [Uri](/reference/android/net/Uri). |

##### For [java.io.File](/reference/java/io/File)

|  |  |
| --- | --- |
| [Uri](/reference/android/net/Uri) | `File.toUri()` Creates a Uri from the given file. |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|  |  |
| --- | --- |
| [Uri](/reference/android/net/Uri) | `String.toUri()` Creates a Uri from the given encoded URI string. |

## androidx.core.os

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.os.Handler](/reference/android/os/Handler)

|  |  |
| --- | --- |
| [Runnable](/reference/java/lang/Runnable) | `Handler.postAtTime(uptimeMillis: Long, token: Any? = null, crossinline action: () -> Unit)` Version of [Handler.postAtTime](/reference/android/os/Handler#postAtTime(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](/reference/java/lang/Runnable) | `Handler.postDelayed(delayInMillis: Long, token: Any? = null, crossinline action: () -> Unit)` Version of [Handler.postDelayed](/reference/android/os/Handler#postDelayed(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |

#### Top-level functions

|  |  |
| --- | --- |
| [Bundle](/reference/android/os/Bundle) | `bundleOf(vararg pairs: Pair<String, Any?>)` Returns a new [Bundle](/reference/android/os/Bundle) with the given key/value pairs as elements. |
| [PersistableBundle](/reference/android/os/PersistableBundle) | `persistableBundleOf(vararg pairs: Pair<String, Any?>)` Returns a new [PersistableBundle](/reference/android/os/PersistableBundle) with the given key/value pairs as elements. |
| T | `trace(sectionName: String, block: () -> T)` Wrap the specified [block](#androidx.core.os$trace(kotlin.String, kotlin.Function0((androidx.core.os.trace.T)))/block) in calls to [Trace.beginSection](/reference/android/os/Trace#beginSection(java.lang.String)) (with the supplied [sectionName](#androidx.core.os$trace(kotlin.String, kotlin.Function0((androidx.core.os.trace.T)))/sectionName)) and [Trace.endSection](/reference/android/os/Trace#endSection()). |

## androidx.core.text

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.text.Spannable](/reference/android/text/Spannable)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Spannable.clearSpans()` Clear all spans from this text. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Spannable.set(start: Int, end: Int, span: Any)` Add [span](#androidx.core.text$set(android.text.Spannable, kotlin.Int, kotlin.Int, kotlin.Any)/span) to the range [start](#androidx.core.text$set(android.text.Spannable, kotlin.Int, kotlin.Int, kotlin.Any)/start)&hellip;[end](#androidx.core.text$set(android.text.Spannable, kotlin.Int, kotlin.Int, kotlin.Any)/end) of the text. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Spannable.set(range: IntRange, span: Any)` Add [span](#androidx.core.text$set(android.text.Spannable, kotlin.ranges.IntRange, kotlin.Any)/span) to the [range](#androidx.core.text$set(android.text.Spannable, kotlin.ranges.IntRange, kotlin.Any)/range) of the text. |

##### For [android.text.SpannableStringBuilder](/reference/android/text/SpannableStringBuilder)

|  |  |
| --- | --- |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.backgroundColor(color: Int, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$backgroundColor(android.text.SpannableStringBuilder, kotlin.Int, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [BackgroundColorSpan](/reference/android/text/style/BackgroundColorSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.bold(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$bold(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a bold [StyleSpan](/reference/android/text/style/StyleSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.color(color: Int, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$color(android.text.SpannableStringBuilder, kotlin.Int, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [ForegroundColorSpan](/reference/android/text/style/ForegroundColorSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.inSpans(vararg spans: Any, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Array((kotlin.Any)), kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in [spans](#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Array((kotlin.Any)), kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/spans). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.inSpans(span: Any, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Any, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in [span](#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Any, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/span). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.italic(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$italic(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in an italic [StyleSpan](/reference/android/text/style/StyleSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.scale(proportion: Float, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$scale(android.text.SpannableStringBuilder, kotlin.Float, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [RelativeSizeSpan](/reference/android/text/style/RelativeSizeSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.strikeThrough(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$strikeThrough(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [StrikethroughSpan](/reference/android/text/style/StrikethroughSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.subscript(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$subscript(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [SubscriptSpan](/reference/android/text/style/SubscriptSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.superscript(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$superscript(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [SuperscriptSpan](/reference/android/text/style/SuperscriptSpan). |
| [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) | `SpannableStringBuilder.underline(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](#androidx.core.text$underline(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in an [UnderlineSpan](/reference/android/text/style/UnderlineSpan). |

##### For [android.text.Spanned](/reference/android/text/Spanned)

|  |  |
| --- | --- |
| [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/)<out T> | `Spanned.getSpans(start: Int = 0, end: Int = length)` Get all spans that are instance of T. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `Spanned.toHtml(option: Int = TO_HTML_PARAGRAPH_LINES_CONSECUTIVE)` Returns a string of HTML from the spans in this [Spanned](/reference/android/text/Spanned). |

##### For [kotlin.CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `CharSequence.isDigitsOnly()` Returns whether the given [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) contains only digits. |
| [Spannable](/reference/android/text/Spannable) | `CharSequence.toSpannable()` Returns a new [Spannable](/reference/android/text/Spannable) from [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/), or the source itself if it is already an instance of [SpannableString](/reference/android/text/SpannableString). |
| [Spanned](/reference/android/text/Spanned) | `CharSequence.toSpanned()` Returns a new [Spanned](/reference/android/text/Spanned) from [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/), or the source itself if it is already an instance of [SpannedString](/reference/android/text/SpannedString). |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `CharSequence.trimmedLength()` Returns the length that the specified [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) would have if spaces and ASCII control characters were trimmed from the start and end, as by [String.trim](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim.html). |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|  |  |
| --- | --- |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `String.htmlEncode()` Html-encode the string. |
| [Spanned](/reference/android/text/Spanned) | `String.parseAsHtml(flags: Int = FROM_HTML_MODE_LEGACY, imageGetter: ImageGetter? = null, tagHandler: TagHandler? = null)` Returns a [Spanned](/reference/android/text/Spanned) from parsing this string as HTML. |

#### Extension properties

##### For [java.util.Locale](/reference/java/util/Locale)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Locale.layoutDirection()` Returns layout direction for a given locale. |

#### Top-level functions

|  |  |
| --- | --- |
| [SpannedString](/reference/android/text/SpannedString) | `buildSpannedString(builderAction: SpannableStringBuilder.() -> Unit)` Builds new string by populating a newly created [SpannableStringBuilder](/reference/android/text/SpannableStringBuilder) using the provided [builderAction](#androidx.core.text$buildSpannedString(kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) and then converting it to [SpannedString](/reference/android/text/SpannedString). |

## androidx.core.transition

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.transition.Transition](/reference/android/transition/Transition)

|  |  |
| --- | --- |
| [TransitionListener](/reference/android/transition/Transition.TransitionListener) | `Transition.addListener(crossinline onEnd: (transition: Transition) -> Unit = {}, crossinline onStart: (transition: Transition) -> Unit = {}, crossinline onCancel: (transition: Transition) -> Unit = {}, crossinline onResume: (transition: Transition) -> Unit = {}, crossinline onPause: (transition: Transition) -> Unit = {})` Add a listener to this Transition using the provided actions. |
| [TransitionListener](/reference/android/transition/Transition.TransitionListener) | `Transition.doOnCancel(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has been cancelled. |
| [TransitionListener](/reference/android/transition/Transition.TransitionListener) | `Transition.doOnEnd(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has ended. |
| [TransitionListener](/reference/android/transition/Transition.TransitionListener) | `Transition.doOnPause(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has been paused. |
| [TransitionListener](/reference/android/transition/Transition.TransitionListener) | `Transition.doOnResume(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has resumed after a pause. |
| [TransitionListener](/reference/android/transition/Transition.TransitionListener) | `Transition.doOnStart(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has started. |

## androidx.core.util

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.util.AtomicFile](/reference/android/util/AtomicFile)

|  |  |
| --- | --- |
| [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/) | `AtomicFile.readBytes()` Gets the entire content of this file as a byte array. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `AtomicFile.readText(charset: Charset = Charsets.UTF_8)` Gets the entire content of this file as a String using UTF-8 or specified [charset](#androidx.core.util$readText(android.util.AtomicFile, java.nio.charset.Charset)/charset). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AtomicFile.tryWrite(block: (out: FileOutputStream) -> Unit)` Perform the write operations inside [block](#androidx.core.util$tryWrite(android.util.AtomicFile, kotlin.Function1((java.io.FileOutputStream, kotlin.Unit)))/block) on this file. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AtomicFile.writeBytes(array: ByteArray)` Sets the content of this file as an [array](#androidx.core.util$writeBytes(android.util.AtomicFile, kotlin.ByteArray)/array) of bytes. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AtomicFile.writeText(text: String, charset: Charset = Charsets.UTF_8)` Sets the content of this file as [text](#androidx.core.util$writeText(android.util.AtomicFile, kotlin.String, java.nio.charset.Charset)/text) encoded using UTF-8 or specified [charset](#androidx.core.util$writeText(android.util.AtomicFile, kotlin.String, java.nio.charset.Charset)/charset). |

##### For [android.util.LongSparseArray](/reference/android/util/LongSparseArray)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.contains(key: Long)` Returns true if the collection contains [key](#androidx.core.util$contains(android.util.LongSparseArray((androidx.core.util.contains.T)), kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.containsKey(key: Long)` Returns true if the collection contains [key](#androidx.core.util$containsKey(android.util.LongSparseArray((androidx.core.util.containsKey.T)), kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.containsValue(value: T)` Returns true if the collection contains [value](#androidx.core.util$containsValue(android.util.LongSparseArray((androidx.core.util.containsValue.T)), androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.forEach(action: (key: Long, value: T) -> Unit)` Performs the given [action](#androidx.core.util$forEach(android.util.LongSparseArray((androidx.core.util.forEach.T)), kotlin.Function2((kotlin.Long, androidx.core.util.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `LongSparseArray<T>.getOrDefault(key: Long, defaultValue: T)` Return the value corresponding to [key](#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)), kotlin.Long, androidx.core.util.getOrDefault.T)/key), or [defaultValue](#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)), kotlin.Long, androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `LongSparseArray<T>.getOrElse(key: Long, defaultValue: () -> T)` Return the value corresponding to [key](#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) | `LongSparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](/reference/android/util/LongSparseArray)<T> | `LongSparseArray<T>.plus(other: LongSparseArray<T>)` Creates a new collection by adding or replacing entries from [other](#androidx.core.util$plus(android.util.LongSparseArray((androidx.core.util.plus.T)), android.util.LongSparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.putAll(other: LongSparseArray<T>)` Update this collection by adding or replacing entries from [other](#androidx.core.util$putAll(android.util.LongSparseArray((androidx.core.util.putAll.T)), android.util.LongSparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.remove(key: Long, value: T)` Removes the entry for [key](#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)), kotlin.Long, androidx.core.util.remove.T)/key) only if it is mapped to [value](#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)), kotlin.Long, androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.set(key: Long, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> | `LongSparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.Pair](/reference/android/util/Pair)

|  |  |
| --- | --- |
| operator F | `Pair<F, S>.component1()` Returns the first component of the pair. |
| operator S | `Pair<F, S>.component2()` Returns the second component of the pair. |
| [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)<F, S> | `Pair<F, S>.toKotlinPair()` Returns this [Pair](/reference/android/util/Pair) as a [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/). |

##### For [android.util.Range](/reference/android/util/Range)

|  |  |
| --- | --- |
| infix [Range](/reference/android/util/Range)<T> | `Range<T>.and(other: Range<T>)` Return the intersection of this range and [other](#androidx.core.util$and(android.util.Range((androidx.core.util.and.T)), android.util.Range((androidx.core.util.and.T)))/other). |
| operator [Range](/reference/android/util/Range)<T> | `Range<T>.plus(value: T)` Return the smallest range that includes this and [value](#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)), androidx.core.util.plus.T)/value). |
| operator [Range](/reference/android/util/Range)<T> | `Range<T>.plus(other: Range<T>)` Return the smallest range that includes this and [other](#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)), android.util.Range((androidx.core.util.plus.T)))/other). |
| [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/)<T> | `Range<T>.toClosedRange()` Returns this [Range](/reference/android/util/Range) as a [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/). |

##### For [android.util.Size](/reference/android/util/Size)

|  |  |
| --- | --- |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Size.component1()` Returns "width", the first component of this [Size](/reference/android/util/Size). |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Size.component2()` Returns "height", the second component of this [Size](/reference/android/util/Size). |

##### For [android.util.SizeF](/reference/android/util/SizeF)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `SizeF.component1()` Returns "width", the first component of this [SizeF](/reference/android/util/SizeF). |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `SizeF.component2()` Returns "height", the second component of this [SizeF](/reference/android/util/SizeF). |

##### For [android.util.SparseArray](/reference/android/util/SparseArray)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.contains(key: Int)` Returns true if the collection contains [key](#androidx.core.util$contains(android.util.SparseArray((androidx.core.util.contains.T)), kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.containsKey(key: Int)` Returns true if the collection contains [key](#androidx.core.util$containsKey(android.util.SparseArray((androidx.core.util.containsKey.T)), kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.containsValue(value: T)` Returns true if the collection contains [value](#androidx.core.util$containsValue(android.util.SparseArray((androidx.core.util.containsValue.T)), androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArray<T>.forEach(action: (key: Int, value: T) -> Unit)` Performs the given [action](#androidx.core.util$forEach(android.util.SparseArray((androidx.core.util.forEach.T)), kotlin.Function2((kotlin.Int, androidx.core.util.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `SparseArray<T>.getOrDefault(key: Int, defaultValue: T)` Return the value corresponding to [key](#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)), kotlin.Int, androidx.core.util.getOrDefault.T)/key), or [defaultValue](#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)), kotlin.Int, androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `SparseArray<T>.getOrElse(key: Int, defaultValue: () -> T)` Return the value corresponding to [key](#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseArray](/reference/android/util/SparseArray)<T> | `SparseArray<T>.plus(other: SparseArray<T>)` Creates a new collection by adding or replacing entries from [other](#androidx.core.util$plus(android.util.SparseArray((androidx.core.util.plus.T)), android.util.SparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArray<T>.putAll(other: SparseArray<T>)` Update this collection by adding or replacing entries from [other](#androidx.core.util$putAll(android.util.SparseArray((androidx.core.util.putAll.T)), android.util.SparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.remove(key: Int, value: T)` Removes the entry for [key](#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)), kotlin.Int, androidx.core.util.remove.T)/key) only if it is mapped to [value](#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)), kotlin.Int, androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArray<T>.set(key: Int, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)<T> | `SparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseBooleanArray](/reference/android/util/SparseBooleanArray)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.contains(key: Int)` Returns true if the collection contains [key](#androidx.core.util$contains(android.util.SparseBooleanArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.containsKey(key: Int)` Returns true if the collection contains [key](#androidx.core.util$containsKey(android.util.SparseBooleanArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.containsValue(value: Boolean)` Returns true if the collection contains [value](#androidx.core.util$containsValue(android.util.SparseBooleanArray, kotlin.Boolean)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseBooleanArray.forEach(action: (key: Int, value: Boolean) -> Unit)` Performs the given [action](#androidx.core.util$forEach(android.util.SparseBooleanArray, kotlin.Function2((kotlin.Int, kotlin.Boolean, kotlin.Unit)))/action) for each key/value entry. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.getOrDefault(key: Int, defaultValue: Boolean)` Return the value corresponding to [key](#androidx.core.util$getOrDefault(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/key), or [defaultValue](#androidx.core.util$getOrDefault(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.getOrElse(key: Int, defaultValue: () -> Boolean)` Return the value corresponding to [key](#androidx.core.util$getOrElse(android.util.SparseBooleanArray, kotlin.Int, kotlin.Function0((kotlin.Boolean)))/key), or from [defaultValue](#androidx.core.util$getOrElse(android.util.SparseBooleanArray, kotlin.Int, kotlin.Function0((kotlin.Boolean)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseBooleanArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseBooleanArray](/reference/android/util/SparseBooleanArray) | `SparseBooleanArray.plus(other: SparseBooleanArray)` Creates a new collection by adding or replacing entries from [other](#androidx.core.util$plus(android.util.SparseBooleanArray, android.util.SparseBooleanArray)/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseBooleanArray.putAll(other: SparseBooleanArray)` Update this collection by adding or replacing entries from [other](#androidx.core.util$putAll(android.util.SparseBooleanArray, android.util.SparseBooleanArray)/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.remove(key: Int, value: Boolean)` Removes the entry for [key](#androidx.core.util$remove(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/key) only if it is mapped to [value](#androidx.core.util$remove(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseBooleanArray.set(key: Int, value: Boolean)` Allows the use of the index operator for storing values in the collection. |
| [BooleanIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-boolean-iterator/) | `SparseBooleanArray.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseIntArray](/reference/android/util/SparseIntArray)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.contains(key: Int)` Returns true if the collection contains [key](#androidx.core.util$contains(android.util.SparseIntArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.containsKey(key: Int)` Returns true if the collection contains [key](#androidx.core.util$containsKey(android.util.SparseIntArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.containsValue(value: Int)` Returns true if the collection contains [value](#androidx.core.util$containsValue(android.util.SparseIntArray, kotlin.Int)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseIntArray.forEach(action: (key: Int, value: Int) -> Unit)` Performs the given [action](#androidx.core.util$forEach(android.util.SparseIntArray, kotlin.Function2((kotlin.Int, , kotlin.Unit)))/action) for each key/value entry. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseIntArray.getOrDefault(key: Int, defaultValue: Int)` Return the value corresponding to [key](#androidx.core.util$getOrDefault(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/key), or [defaultValue](#androidx.core.util$getOrDefault(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/defaultValue) when not present. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseIntArray.getOrElse(key: Int, defaultValue: () -> Int)` Return the value corresponding to [key](#androidx.core.util$getOrElse(android.util.SparseIntArray, kotlin.Int, kotlin.Function0((kotlin.Int)))/key), or from [defaultValue](#androidx.core.util$getOrElse(android.util.SparseIntArray, kotlin.Int, kotlin.Function0((kotlin.Int)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseIntArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseIntArray](/reference/android/util/SparseIntArray) | `SparseIntArray.plus(other: SparseIntArray)` Creates a new collection by adding or replacing entries from [other](#androidx.core.util$plus(android.util.SparseIntArray, android.util.SparseIntArray)/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseIntArray.putAll(other: SparseIntArray)` Update this collection by adding or replacing entries from [other](#androidx.core.util$putAll(android.util.SparseIntArray, android.util.SparseIntArray)/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.remove(key: Int, value: Int)` Removes the entry for [key](#androidx.core.util$remove(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/key) only if it is mapped to [value](#androidx.core.util$remove(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseIntArray.set(key: Int, value: Int)` Allows the use of the index operator for storing values in the collection. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseIntArray.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseLongArray](/reference/android/util/SparseLongArray)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.contains(key: Int)` Returns true if the collection contains [key](#androidx.core.util$contains(android.util.SparseLongArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.containsKey(key: Int)` Returns true if the collection contains [key](#androidx.core.util$containsKey(android.util.SparseLongArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.containsValue(value: Long)` Returns true if the collection contains [value](#androidx.core.util$containsValue(android.util.SparseLongArray, kotlin.Long)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseLongArray.forEach(action: (key: Int, value: Long) -> Unit)` Performs the given [action](#androidx.core.util$forEach(android.util.SparseLongArray, kotlin.Function2((kotlin.Int, kotlin.Long, kotlin.Unit)))/action) for each key/value entry. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SparseLongArray.getOrDefault(key: Int, defaultValue: Long)` Return the value corresponding to [key](#androidx.core.util$getOrDefault(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/key), or [defaultValue](#androidx.core.util$getOrDefault(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/defaultValue) when not present. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SparseLongArray.getOrElse(key: Int, defaultValue: () -> Long)` Return the value corresponding to [key](#androidx.core.util$getOrElse(android.util.SparseLongArray, kotlin.Int, kotlin.Function0((kotlin.Long)))/key), or from [defaultValue](#androidx.core.util$getOrElse(android.util.SparseLongArray, kotlin.Int, kotlin.Function0((kotlin.Long)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseLongArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseLongArray](/reference/android/util/SparseLongArray) | `SparseLongArray.plus(other: SparseLongArray)` Creates a new collection by adding or replacing entries from [other](#androidx.core.util$plus(android.util.SparseLongArray, android.util.SparseLongArray)/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseLongArray.putAll(other: SparseLongArray)` Update this collection by adding or replacing entries from [other](#androidx.core.util$putAll(android.util.SparseLongArray, android.util.SparseLongArray)/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.remove(key: Int, value: Long)` Removes the entry for [key](#androidx.core.util$remove(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/key) only if it is set to [value](#androidx.core.util$remove(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseLongArray.set(key: Int, value: Long)` Allows the use of the index operator for storing values in the collection. |
| [LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) | `SparseLongArray.valueIterator()` Return an iterator over the collection's values. |

##### For [kotlin.Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/)

|  |  |
| --- | --- |
| [Half](/reference/android/util/Half) | `Double.toHalf()` Returns a [Half](/reference/android/util/Half) instance representing given [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/). |

##### For [kotlin.Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)

|  |  |
| --- | --- |
| [Half](/reference/android/util/Half) | `Float.toHalf()` Returns a [Half](/reference/android/util/Half) instance representing given [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/). |

##### For [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)

|  |  |
| --- | --- |
| [Pair](/reference/android/util/Pair)<F, S> | `Pair<F, S>.toAndroidPair()` Returns this [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/) as an Android [Pair](/reference/android/util/Pair). |

##### For [kotlin.Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/)

|  |  |
| --- | --- |
| [Half](/reference/android/util/Half) | `Short.toHalf()` Returns a [Half](/reference/android/util/Half) instance representing given [Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/). |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|  |  |
| --- | --- |
| [Half](/reference/android/util/Half) | `String.toHalf()` Returns a [Half](/reference/android/util/Half) instance representing given [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/). |

##### For [kotlin.ranges.ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/)

|  |  |
| --- | --- |
| [Range](/reference/android/util/Range)<T> | `ClosedRange<T>.toRange()` Returns this [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/) as a [Range](/reference/android/util/Range). |

#### Extension properties

##### For [android.util.LongSparseArray](/reference/android/util/LongSparseArray)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `LongSparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseArray](/reference/android/util/SparseArray)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseBooleanArray](/reference/android/util/SparseBooleanArray)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseBooleanArray.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseIntArray](/reference/android/util/SparseIntArray)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseIntArray.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseLongArray](/reference/android/util/SparseLongArray)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseLongArray.size()` Returns the number of key/value entries in the collection. |

#### Top-level functions

|  |  |
| --- | --- |
| [LruCache](/reference/android/util/LruCache)<K, V> | `lruCache(maxSize: Int, crossinline sizeOf: (key: K, value: V) -> Int = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: Boolean, key: K, oldValue: V, newValue: V?) -> Unit = { _, _, _, _ -> })` Creates an [LruCache](/reference/android/util/LruCache) with the given parameters. |
| infix [Range](/reference/android/util/Range)<T> | `T.rangeTo(that: T)` Creates a range from this [Comparable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-comparable/) value to [that](#androidx.core.util$rangeTo(androidx.core.util.rangeTo.T, androidx.core.util.rangeTo.T)/that). |

## androidx.core.view

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.view.Menu](/reference/android/view/Menu)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Menu.contains(item: MenuItem)` Returns `true` if [item](#androidx.core.view$contains(android.view.Menu, android.view.MenuItem)/item) is found in this menu. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Menu.forEach(action: (item: MenuItem) -> Unit)` Performs the given action on each item in this menu. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Menu.forEachIndexed(action: (index: Int, item: MenuItem) -> Unit)` Performs the given action on each item in this menu, providing its sequential index. |
| operator [MenuItem](/reference/android/view/MenuItem) | `Menu.get(index: Int)` Returns the menu at [index](#androidx.core.view$get(android.view.Menu, kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Menu.isEmpty()` Returns true if this menu contains no items. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Menu.isNotEmpty()` Returns true if this menu contains one or more items. |
| operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)<[MenuItem](/reference/android/view/MenuItem)> | `Menu.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the items in this menu. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Menu.minusAssign(item: MenuItem)` Removes [item](#androidx.core.view$minusAssign(android.view.Menu, android.view.MenuItem)/item) from this menu. |

##### For [android.view.View](/reference/android/view/View)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnAttach(crossinline action: (view: View) -> Unit)` Performs the given action when this view is attached to a window. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnDetach(crossinline action: (view: View) -> Unit)` Performs the given action when this view is detached from a window. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnLayout(crossinline action: (view: View) -> Unit)` Performs the given action when this view is laid out. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnNextLayout(crossinline action: (view: View) -> Unit)` Performs the given action when this view is next laid out. |
| [OneShotPreDrawListener](/reference/kotlin/androidx/core/view/OneShotPreDrawListener) | `View.doOnPreDraw(crossinline action: (view: View) -> Unit)` Performs the given action when the view tree is about to be drawn. |
| [Bitmap](/reference/android/graphics/Bitmap) | `View.drawToBitmap(config: Config = Bitmap.Config.ARGB_8888)` Return a [Bitmap](/reference/android/graphics/Bitmap) representation of this [View](/reference/android/view/View). |
| [Runnable](/reference/java/lang/Runnable) | `View.postDelayed(delayInMillis: Long, crossinline action: () -> Unit)` Version of [View.postDelayed](/reference/android/view/View#postDelayed(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](/reference/java/lang/Runnable) | `View.postOnAnimationDelayed(delayInMillis: Long, crossinline action: () -> Unit)` Version of [View.postOnAnimationDelayed](/reference/android/view/View#postOnAnimationDelayed(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.setPadding(@Px size: Int)` Sets the view's padding. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updateLayoutParams(block: LayoutParams.() -> Unit)` Executes [block](#androidx.core.view$updateLayoutParams(android.view.View, kotlin.Function1((android.view.ViewGroup.LayoutParams, kotlin.Unit)))/block) with the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updateLayoutParams(block: T.() -> Unit)` Executes [block](#androidx.core.view$updateLayoutParams(android.view.View, kotlin.Function1((androidx.core.view.updateLayoutParams.T, kotlin.Unit)))/block) with a typed version of the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updatePadding(@Px left: Int = paddingLeft, @Px top: Int = paddingTop, @Px right: Int = paddingRight, @Px bottom: Int = paddingBottom)` Updates this view's padding. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updatePaddingRelative(@Px start: Int = paddingStart, @Px top: Int = paddingTop, @Px end: Int = paddingEnd, @Px bottom: Int = paddingBottom)` Updates this view's relative padding. |

##### For [android.view.ViewGroup](/reference/android/view/ViewGroup)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `ViewGroup.contains(view: View)` Returns `true` if [view](#androidx.core.view$contains(android.view.ViewGroup, android.view.View)/view) is found in this view group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.forEach(action: (view: View) -> Unit)` Performs the given action on each view in this view group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.forEachIndexed(action: (index: Int, view: View) -> Unit)` Performs the given action on each view in this view group, providing its sequential index. |
| operator [View](/reference/android/view/View) | `ViewGroup.get(index: Int)` Returns the view at [index](#androidx.core.view$get(android.view.ViewGroup, kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `ViewGroup.isEmpty()` Returns true if this view group contains no views. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `ViewGroup.isNotEmpty()` Returns true if this view group contains one or more views. |
| operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)<[View](/reference/android/view/View)> | `ViewGroup.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the views in this view group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.minusAssign(view: View)` Removes [view](#androidx.core.view$minusAssign(android.view.ViewGroup, android.view.View)/view) from this view group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.plusAssign(view: View)` Adds [view](#androidx.core.view$plusAssign(android.view.ViewGroup, android.view.View)/view) to this view group. |

##### For [android.view.ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `MarginLayoutParams.setMargins(@Px size: Int)` Sets the margins in the ViewGroup's MarginLayoutParams. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `MarginLayoutParams.updateMargins(@Px left: Int = leftMargin, @Px top: Int = topMargin, @Px right: Int = rightMargin, @Px bottom: Int = bottomMargin)` Updates the margins in the [ViewGroup](/reference/android/view/ViewGroup)'s [ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `MarginLayoutParams.updateMarginsRelative(@Px start: Int = marginStart, @Px top: Int = topMargin, @Px end: Int = marginEnd, @Px bottom: Int = bottomMargin)` Updates the relative margins in the ViewGroup's MarginLayoutParams. |

#### Extension properties

##### For [android.view.Menu](/reference/android/view/Menu)

|  |  |
| --- | --- |
| [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)<[MenuItem](/reference/android/view/MenuItem)> | `Menu.children()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the items in this menu. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Menu.size()` Returns the number of items in this menu. |

##### For [android.view.View](/reference/android/view/View)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `View.isGone()` Returns true when this view's visibility is [View.GONE](/reference/android/view/View#GONE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `View.isInvisible()` Returns true when this view's visibility is [View.INVISIBLE](/reference/android/view/View#INVISIBLE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `View.isVisible()` Returns true when this view's visibility is [View.VISIBLE](/reference/android/view/View#VISIBLE), false otherwise. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginBottom()` Returns the bottom margin if this view's [LayoutParams](/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginEnd()` Returns the end margin if this view's [LayoutParams](/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginLeft()` Returns the left margin if this view's [LayoutParams](/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginRight()` Returns the right margin if this view's [LayoutParams](/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginStart()` Returns the start margin if this view's [LayoutParams](/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginTop()` Returns the top margin if this view's [LayoutParams](/reference/android/view/ViewGroup.LayoutParams) is a [ViewGroup.MarginLayoutParams](/reference/android/view/ViewGroup.MarginLayoutParams), otherwise 0. |

##### For [android.view.ViewGroup](/reference/android/view/ViewGroup)

|  |  |
| --- | --- |
| [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)<[View](/reference/android/view/View)> | `ViewGroup.children()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the child views in this view group. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `ViewGroup.size()` Returns the number of views in this view group. |

## androidx.core.widget

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.widget.TextView](/reference/android/widget/TextView)

|  |  |
| --- | --- |
| [TextWatcher](/reference/android/text/TextWatcher) | `TextView.addTextChangedListener(crossinline beforeTextChanged: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit = { _, _, _, _ -> }, crossinline onTextChanged: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit = { _, _, _, _ -> }, crossinline afterTextChanged: (text: Editable?) -> Unit = {})` Add a text changed listener to this TextView using the provided actions |
| [TextWatcher](/reference/android/text/TextWatcher) | `TextView.doAfterTextChanged(crossinline action: (text: Editable?) -> Unit)` Add an action which will be invoked after the text changed. |
| [TextWatcher](/reference/android/text/TextWatcher) | `TextView.doBeforeTextChanged(crossinline action: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit)` Add an action which will be invoked before the text changed. |
| [TextWatcher](/reference/android/text/TextWatcher) | `TextView.doOnTextChanged(crossinline action: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit)` Add an action which will be invoked when the text is changing. |

## androidx.dynamicanimation.animation

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.dynamicanimation:dynamicanimation-ktx:"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.dynamicanimation:dynamicanimation-ktx:")
}
```

#### Extension functions

##### For [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation)

|  |  |
| --- | --- |
| [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) | `SpringAnimation.withSpringForceProperties(func: SpringForce.() -> Unit)` Updates or applies spring force properties like [SpringForce.mDampingRatio](/reference/kotlin/androidx/dynamicanimation/animation/SpringForce#getDampingRatio()), [SpringForce.mFinalPosition](/reference/kotlin/androidx/dynamicanimation/animation/SpringForce#getFinalPosition()) and stiffness on SpringAnimation. |

#### Top-level functions

|  |  |
| --- | --- |
| [FlingAnimation](/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) | `flingAnimationOf(setter: (Float) -> Unit, getter: () -> Float)` Creates [FlingAnimation](/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) for a property that can be accessed via the provided setter and getter. |
| [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) | `springAnimationOf(setter: (Float) -> Unit, getter: () -> Float, finalPosition: Float = Float.NaN)` Creates [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) for a property that can be accessed via the provided setter and getter. |

## androidx.fragment.app

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.fragment:fragment-ktx:1.9.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.fragment:fragment-ktx:1.9.1")
}
```

#### Extension functions

##### For [android.view.View](/reference/android/view/View)

|  |  |
| --- | --- |
| F | `View.findFragment()` Find a [Fragment](/reference/kotlin/androidx/fragment/app/Fragment) associated with a [View](/reference/android/view/View). |

##### For [Fragment](/reference/kotlin/androidx/fragment/app/Fragment)

|  |  |
| --- | --- |
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> | `Fragment.activityViewModels(noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access parent activity's [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel), if [factoryProducer](#androidx.fragment.app$activityViewModels(androidx.fragment.app.Fragment, kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) first time. |
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> | `Fragment.createViewModelLazy(viewModelClass: KClass<VM>, storeProducer: () -> ViewModelStore, factoryProducer: () -> ViewModelProvider.Factory = null)` Helper method for creation of [ViewModelLazy](/reference/kotlin/androidx/lifecycle/ViewModelLazy), that resolves `null` passed as [factoryProducer](#androidx.fragment.app$createViewModelLazy(androidx.fragment.app.Fragment, kotlin.reflect.KClass((androidx.fragment.app.createViewModelLazy.VM)), kotlin.Function0((androidx.lifecycle.ViewModelStore)), kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) to default factory. |
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> | `Fragment.viewModels(noinline ownerProducer: () -> ViewModelStoreOwner = { this }, noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) by **default** scoped to this [Fragment](/reference/kotlin/androidx/fragment/app/Fragment): |

##### For [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction)

|  |  |
| --- | --- |
| [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `FragmentTransaction.add(@IdRes containerViewId: Int, tag: String? = null, args: Bundle? = null)` Add a fragment to the associated [FragmentManager](/reference/kotlin/androidx/fragment/app/FragmentManager), inflating the Fragment's view into the container view specified by [containerViewId](#androidx.fragment.app$add(androidx.fragment.app.FragmentTransaction, kotlin.Int, kotlin.String, android.os.Bundle)/containerViewId), to later retrieve via [FragmentManager.findFragmentById](/reference/kotlin/androidx/fragment/app/FragmentManager#findFragmentById(int)). |
| [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `FragmentTransaction.add(tag: String, args: Bundle? = null)` Add a fragment to the associated [FragmentManager](/reference/kotlin/androidx/fragment/app/FragmentManager) without adding the Fragment to any container view. |
| [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `FragmentTransaction.replace(@IdRes containerViewId: Int, tag: String? = null, args: Bundle? = null)` Replace an existing fragment that was added to a container. |

##### For [FragmentManager](/reference/kotlin/androidx/fragment/app/FragmentManager)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `FragmentManager.commit(allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](#androidx.fragment.app$commit(androidx.fragment.app.FragmentManager, kotlin.Boolean, kotlin.Function1((androidx.fragment.app.FragmentTransaction, kotlin.Unit)))/body) in a [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `FragmentManager.commitNow(allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](#androidx.fragment.app$commitNow(androidx.fragment.app.FragmentManager, kotlin.Boolean, kotlin.Function1((androidx.fragment.app.FragmentTransaction, kotlin.Unit)))/body) in a [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `FragmentManager.transaction(now: Boolean = false, allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](#androidx.fragment.app$transaction(androidx.fragment.app.FragmentManager, kotlin.Boolean, kotlin.Boolean, kotlin.Function1((androidx.fragment.app.FragmentTransaction, kotlin.Unit)))/body) in a [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |

## androidx.fragment.app.testing

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.fragment:fragment-testing:1.9.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.fragment:fragment-testing:1.9.1")
}
```

#### Top-level functions

|  |  |
| --- | --- |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragment(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: FragmentFactory? = null)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) using given [FragmentFactory](/reference/kotlin/androidx/fragment/app/FragmentFactory) and waits for it to reach a resumed state. |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragment(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) using [instantiate](#androidx.fragment.app.testing$launchFragment(android.os.Bundle, kotlin.Int, kotlin.Function0((androidx.fragment.app.testing.launchFragment.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragmentInContainer(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: FragmentFactory? = null)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) and waits for it to reach a resumed state. |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragmentInContainer(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) using [instantiate](#androidx.fragment.app.testing$launchFragmentInContainer(android.os.Bundle, kotlin.Int, kotlin.Function0((androidx.fragment.app.testing.launchFragmentInContainer.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |

## androidx.lifecycle

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.lifecycle:lifecycle-livedata-core-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.11.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.lifecycle:lifecycle-livedata-core-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-livedata-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-reactivestreams-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.11.0")
}
```

#### Extension functions

##### For [kotlinx.coroutines.flow.Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)

|  |  |
| --- | --- |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `Flow<T>.asLiveData(context: CoroutineContext = EmptyCoroutineContext, timeoutInMs: Long = DEFAULT_TIMEOUT)` Creates a LiveData that has values collected from the origin [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `Flow<T>.asLiveData(context: CoroutineContext = EmptyCoroutineContext, timeout: Duration)` Creates a LiveData that has values collected from the origin [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/). |

##### For [org.reactivestreams.Publisher](/reference/kotlin/androidx/lifecycle/package-summary#(org.reactivestreams.Publisher).toLiveData())

|  |  |
| --- | --- |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `Publisher<T>.toLiveData()` Creates an observable [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) stream from a ReactiveStreams [Publisher](/reference/kotlin/androidx/lifecycle/package-summary#(org.reactivestreams.Publisher).toLiveData()). |

##### For [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)

|  |  |
| --- | --- |
| [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)<T> | `LiveData<T>.asFlow()` Creates a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) containing values dispatched by originating [LiveData](/reference/kotlin/androidx/lifecycle/LiveData): at the start a flow collector receives the latest value held by LiveData and then observes LiveData updates. |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<X> | `LiveData<X>.distinctUntilChanged()` Creates a new [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) object does not emit a value until the source `this` LiveData value has been changed. |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<Y> | `LiveData<X>.map(crossinline transform: (X) -> Y)` Returns a [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) mapped from `this` LiveData by applying [transform](#androidx.lifecycle$map(androidx.lifecycle.LiveData((androidx.lifecycle.map.X)), kotlin.Function1((androidx.lifecycle.map.X, androidx.lifecycle.map.Y)))/transform) to each value set on `this` LiveData. |
| [Observer](/reference/kotlin/androidx/lifecycle/Observer)<T> | `LiveData<T>.observe(owner: LifecycleOwner, crossinline onChanged: (T) -> Unit)` Adds the given [onChanged](#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)), androidx.lifecycle.LifecycleOwner, kotlin.Function1((androidx.lifecycle.observe.T, kotlin.Unit)))/onChanged) lambda as an observer within the lifespan of the given [owner](#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)), androidx.lifecycle.LifecycleOwner, kotlin.Function1((androidx.lifecycle.observe.T, kotlin.Unit)))/owner) and returns a reference to observer. |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<Y> | `LiveData<X>.switchMap(crossinline transform: (X) -> LiveData<Y>)` Returns a [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) mapped from the input `this` `LiveData` by applying [transform](#androidx.lifecycle$switchMap(androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.X)), kotlin.Function1((androidx.lifecycle.switchMap.X, androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.Y)))))/transform) to each value set on `this`. |
| Publisher<T> | `LiveData<T>.toPublisher(lifecycle: LifecycleOwner)` Adapts the given [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) stream to a ReactiveStreams [Publisher](/reference/kotlin/androidx/lifecycle/package-summary#(org.reactivestreams.Publisher).toLiveData()). |

##### For [ViewModelProvider](/reference/kotlin/androidx/lifecycle/ViewModelProvider)

|  |  |
| --- | --- |
| VM | `ViewModelProvider.get()` Returns an existing ViewModel or creates a new one in the scope (usually, a fragment or an activity), associated with this `ViewModelProvider`. |

##### For [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)

|  |  |
| --- | --- |
| suspend T | `LifecycleOwner.whenCreated(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#CREATED) state. |
| suspend T | `LifecycleOwner.whenResumed(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#RESUMED) state. |
| suspend T | `LifecycleOwner.whenStarted(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#STARTED) state. |

##### For [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle)

|  |  |
| --- | --- |
| suspend T | `Lifecycle.whenCreated(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#CREATED) state. |
| suspend T | `Lifecycle.whenResumed(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#RESUMED) state. |
| suspend T | `Lifecycle.whenStarted(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#STARTED) state. |
| suspend T | `Lifecycle.whenStateAtLeast(minState: Lifecycle.State, block: suspend CoroutineScope.() -> T)` Runs the given [block](#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle, androidx.lifecycle.Lifecycle.State, kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope, androidx.lifecycle.whenStateAtLeast.T)))/block) on a [CoroutineDispatcher](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/) that executes the [block](#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle, androidx.lifecycle.Lifecycle.State, kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope, androidx.lifecycle.whenStateAtLeast.T)))/block) on the main thread and suspends the execution unless the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle)'s state is at least [minState](#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle, androidx.lifecycle.Lifecycle.State, kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope, androidx.lifecycle.whenStateAtLeast.T)))/minState). |

#### Extension properties

##### For [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle)

|  |  |
| --- | --- |
| [LifecycleCoroutineScope](/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) | `Lifecycle.coroutineScope()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle). |

##### For [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)

|  |  |
| --- | --- |
| [LifecycleCoroutineScope](/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) | `LifecycleOwner.lifecycleScope()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle). |

##### For [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel)

|  |  |
| --- | --- |
| [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) | `ViewModel.viewModelScope()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel). |

#### Top-level functions

|  |  |
| --- | --- |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `liveData(context: CoroutineContext = EmptyCoroutineContext, timeoutInMs: Long = DEFAULT_TIMEOUT, block: suspend LiveDataScope<T>.() -> Unit)` Builds a LiveData that has values yielded from the given [block](#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext, kotlin.Long, kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)), kotlin.Unit)))/block) that executes on a [LiveDataScope](/reference/kotlin/androidx/lifecycle/LiveDataScope). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `liveData(context: CoroutineContext = EmptyCoroutineContext, timeout: Duration, block: suspend LiveDataScope<T>.() -> Unit)` Builds a LiveData that has values yielded from the given [block](#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext, java.time.Duration, kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)), kotlin.Unit)))/block) that executes on a [LiveDataScope](/reference/kotlin/androidx/lifecycle/LiveDataScope). |

## androidx.navigation

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.navigation:navigation-runtime-ktx:2.10.2"
    implementation "androidx.navigation:navigation-fragment-ktx:2.10.2"
    implementation "androidx.navigation:navigation-ui-ktx:2.10.2"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.navigation:navigation-runtime-ktx:2.10.2")
    implementation("androidx.navigation:navigation-fragment-ktx:2.10.2")
    implementation("androidx.navigation:navigation-ui-ktx:2.10.2")
}
```

#### Extension functions

##### For [android.app.Activity](/reference/android/app/Activity)

|  |  |
| --- | --- |
| [NavController](/reference/kotlin/androidx/navigation/NavController) | `Activity.findNavController(@IdRes viewId: Int)` Find a [NavController](/reference/kotlin/androidx/navigation/NavController) given the id of a View and its containing [Activity](/reference/android/app/Activity). |
| [NavArgsLazy](/reference/kotlin/androidx/navigation/NavArgsLazy)<Args> | `Activity.navArgs()` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the Activity's extras as an Args instance. |

##### For [android.view.View](/reference/android/view/View)

|  |  |
| --- | --- |
| [NavController](/reference/kotlin/androidx/navigation/NavController) | `View.findNavController()` Find a [NavController](/reference/kotlin/androidx/navigation/NavController) associated with a [View](/reference/android/view/View). |

##### For [NavGraphBuilder](/reference/kotlin/androidx/navigation/NavGraphBuilder)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.activity(@IdRes id: Int, builder: ActivityNavigatorDestinationBuilder.() -> Unit)` Construct a new [ActivityNavigator.Destination](/reference/kotlin/androidx/navigation/ActivityNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.navigation(@IdRes id: Int, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a nested [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavGraph](/reference/kotlin/androidx/navigation/NavGraph)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `NavGraph.contains(@IdRes id: Int)` Returns `true` if a destination with `id` is found in this navigation graph. |
| operator [NavDestination](/reference/kotlin/androidx/navigation/NavDestination) | `NavGraph.get(@IdRes id: Int)` Returns the destination with `id`. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraph.minusAssign(node: NavDestination)` Removes `node` from this navigation graph. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraph.plusAssign(node: NavDestination)` Adds a destination to this NavGraph. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraph.plusAssign(other: NavGraph)` Add all destinations from another collection to this one. |

##### For [NavController](/reference/kotlin/androidx/navigation/NavController)

|  |  |
| --- | --- |
| [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) | `NavController.createGraph(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavHost](/reference/kotlin/androidx/navigation/NavHost)

|  |  |
| --- | --- |
| [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) | `NavHost.createGraph(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavigatorProvider](/reference/kotlin/androidx/navigation/NavigatorProvider)

|  |  |
| --- | --- |
| operator T | `NavigatorProvider.get(name: String)` Retrieves a registered [Navigator](/reference/kotlin/androidx/navigation/Navigator) by name. |
| operator T | `NavigatorProvider.get(clazz: KClass<T>)` Retrieves a registered [Navigator](/reference/kotlin/androidx/navigation/Navigator) using the name provided by the [Navigator.Name annotation](/reference/kotlin/androidx/navigation/Navigator.Name). |
| [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) | `NavigatorProvider.navigation(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavigatorProvider.plusAssign(navigator: Navigator<out NavDestination>)` Register a navigator using the name provided by the [Navigator.Name annotation](/reference/kotlin/androidx/navigation/Navigator.Name). |
| operator [Navigator](/reference/kotlin/androidx/navigation/Navigator)<out [NavDestination](/reference/kotlin/androidx/navigation/NavDestination)!>? | `NavigatorProvider.set(name: String, navigator: Navigator<out NavDestination>)` Register a [Navigator](/reference/kotlin/androidx/navigation/Navigator) by name. |

##### For [Fragment](/reference/kotlin/androidx/fragment/app/Fragment)

|  |  |
| --- | --- |
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)<VM> | `Fragment.navGraphViewModels(@IdRes navGraphId: Int, noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access a [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) scoped to a navigation graph present on the {@link NavController} back stack: |

#### Top-level functions

|  |  |
| --- | --- |
| [ActivityNavigator.Extras](/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) | `ActivityNavigatorExtras(activityOptions: ActivityOptionsCompat? = null, flags: Int = 0)` Create a new [ActivityNavigator.Extras](/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) instance with a specific [ActivityOptionsCompat](/reference/kotlin/androidx/core/app/ActivityOptionsCompat) instance and/or any `Intent.FLAG_ACTIVITY_` flags. |
| [NavOptions](/reference/kotlin/androidx/navigation/NavOptions) | `navOptions(optionsBuilder: NavOptionsBuilder.() -> Unit)` Construct a new [NavOptions](/reference/kotlin/androidx/navigation/NavOptions) |

## androidx.navigation.fragment

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.navigation:navigation-fragment-ktx:2.10.2"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.navigation:navigation-fragment-ktx:2.10.2")
}
```

#### Extension functions

##### For [NavGraphBuilder](/reference/kotlin/androidx/navigation/NavGraphBuilder)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.dialog(@IdRes id: Int)` Construct a new [DialogFragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.dialog(@IdRes id: Int, builder: DialogFragmentNavigatorDestinationBuilder.() -> Unit)` Construct a new [DialogFragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.fragment(@IdRes id: Int)` Construct a new [FragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.fragment(@IdRes id: Int, builder: FragmentNavigatorDestinationBuilder.() -> Unit)` Construct a new [FragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination) |

##### For [Fragment](/reference/kotlin/androidx/fragment/app/Fragment)

|  |  |
| --- | --- |
| [NavController](/reference/kotlin/androidx/navigation/NavController) | `Fragment.findNavController()` Find a [NavController](/reference/kotlin/androidx/navigation/NavController) given a [Fragment](/reference/kotlin/androidx/fragment/app/Fragment) |
| [NavArgsLazy](/reference/kotlin/androidx/navigation/NavArgsLazy)<Args> | `Fragment.navArgs()` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the Fragment's arguments as an Args instance. |

#### Top-level functions

|  |  |
| --- | --- |
| [FragmentNavigator.Extras](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) | `FragmentNavigatorExtras(vararg sharedElements: Pair<View, String>)` Create a new [FragmentNavigator.Extras](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) instance with the given shared elements |

## androidx.navigation.ui

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.navigation:navigation-ui-ktx:2.10.2"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.navigation:navigation-ui-ktx:2.10.2")
}
```

#### Extension functions

##### For [android.view.MenuItem](/reference/android/view/MenuItem)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `MenuItem.onNavDestinationSelected(navController: NavController)` Attempt to navigate to the [NavDestination](/reference/kotlin/androidx/navigation/NavDestination) associated with this [MenuItem](/reference/android/view/MenuItem). |

##### For [androidx.appcompat.app.AppCompatActivity](/reference/kotlin/androidx/appcompat/app/AppCompatActivity)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AppCompatActivity.setupActionBarWithNavController(navController: NavController, drawerLayout: DrawerLayout?)` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar()) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AppCompatActivity.setupActionBarWithNavController(navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar()) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [androidx.appcompat.widget.Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Toolbar.setupWithNavController(navController: NavController, drawerLayout: DrawerLayout?)` Sets up a [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Toolbar.setupWithNavController(navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.appbar.CollapsingToolbarLayout](/reference/com/google/android/material/appbar/CollapsingToolbarLayout)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `CollapsingToolbarLayout.setupWithNavController(toolbar: Toolbar, navController: NavController, drawerLayout: DrawerLayout?)` Sets up a [CollapsingToolbarLayout](/reference/com/google/android/material/appbar/CollapsingToolbarLayout) and [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `CollapsingToolbarLayout.setupWithNavController(toolbar: Toolbar, navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [CollapsingToolbarLayout](/reference/com/google/android/material/appbar/CollapsingToolbarLayout) and [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.bottomnavigation.BottomNavigationView](/reference/com/google/android/material/bottomnavigation/BottomNavigationView)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `BottomNavigationView.setupWithNavController(navController: NavController)` Sets up a [BottomNavigationView](/reference/com/google/android/material/bottomnavigation/BottomNavigationView) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.navigation.NavigationView](/reference/com/google/android/material/navigation/NavigationView)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavigationView.setupWithNavController(navController: NavController)` Sets up a [NavigationView](/reference/com/google/android/material/navigation/NavigationView) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [NavController](/reference/kotlin/androidx/navigation/NavController)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `NavController.navigateUp(drawerLayout: DrawerLayout?)` Handles the Up button by delegating its behavior to the given [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `NavController.navigateUp(appBarConfiguration: AppBarConfiguration)` Handles the Up button by delegating its behavior to the given [NavController](/reference/kotlin/androidx/navigation/NavController). |

#### Top-level functions

|  |  |
| --- | --- |
| [AppBarConfiguration](/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `AppBarConfiguration(navGraph: NavGraph, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar), [android.support.design.widget.CollapsingToolbarLayout](/reference/com/google/android/material/appbar/CollapsingToolbarLayout), and [android.support.v7.app.ActionBar](/reference/kotlin/androidx/appcompat/app/ActionBar). |
| [AppBarConfiguration](/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `AppBarConfiguration(topLevelMenu: Menu, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar), [android.support.design.widget.CollapsingToolbarLayout](/reference/com/google/android/material/appbar/CollapsingToolbarLayout), and [android.support.v7.app.ActionBar](/reference/kotlin/androidx/appcompat/app/ActionBar). |
| [AppBarConfiguration](/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `AppBarConfiguration(topLevelDestinationIds: Set<Int>, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar), [android.support.design.widget.CollapsingToolbarLayout](/reference/com/google/android/material/appbar/CollapsingToolbarLayout), and [android.support.v7.app.ActionBar](/reference/kotlin/androidx/appcompat/app/ActionBar). |

## androidx.paging

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.paging:paging-common-ktx:2.1.2"
    implementation "androidx.paging:paging-runtime-ktx:2.1.2"
    implementation "androidx.paging:paging-rxjava2-ktx:2.1.2"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.paging:paging-common-ktx:2.1.2")
    implementation("androidx.paging:paging-runtime-ktx:2.1.2")
    implementation("androidx.paging:paging-rxjava2-ktx:2.1.2")
}
```

#### Extension functions

##### For [Factory](/reference/kotlin/androidx/paging/DataSource.Factory)

|  |  |
| --- | --- |
| Flowable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toFlowable(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| Flowable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toFlowable(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toLiveData(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchExecutor: Executor = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](/reference/kotlin/androidx/paging/LivePagedListBuilder). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toLiveData(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchExecutor: Executor = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](/reference/kotlin/androidx/paging/LivePagedListBuilder). |
| Observable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toObservable(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| Observable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toObservable(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |

#### Top-level functions

|  |  |
| --- | --- |
| [PagedList.Config](/reference/kotlin/androidx/paging/PagedList.Config) | `Config(pageSize: Int, prefetchDistance: Int = pageSize, enablePlaceholders: Boolean = true, initialLoadSizeHint: Int = pageSize * PagedList.Config.Builder.DEFAULT_INITIAL_PAGE_MULTIPLIER, maxSize: Int = PagedList.Config.MAX_SIZE_UNBOUNDED)` Constructs a [PagedList.Config](/reference/kotlin/androidx/paging/PagedList.Config), convenience for [PagedList.Config.Builder](/reference/kotlin/androidx/paging/PagedList.Config.Builder). |
| [PagedList](/reference/kotlin/androidx/paging/PagedList)<Value> | `PagedList(dataSource: DataSource<Key, Value>, config: PagedList.Config, notifyExecutor: Executor, fetchExecutor: Executor, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, initialKey: Key? = null)` Constructs a [PagedList](/reference/kotlin/androidx/paging/PagedList), convenience for [PagedList.Builder](/reference/kotlin/androidx/paging/PagedList.Builder). |

## androidx.palette.graphics

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.palette:palette-ktx:1.1.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.palette:palette-ktx:1.1.0")
}
```

#### Extension functions

##### For [Palette](/reference/kotlin/androidx/palette/graphics/Palette)

|  |  |
| --- | --- |
| operator [Palette.Swatch](/reference/kotlin/androidx/palette/graphics/Palette.Swatch)? | `Palette.get(target: Target)` Returns the selected swatch for the given target from the palette, or `null` if one could not be found. |

## androidx.preference

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.preference:preference-ktx:1.2.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.preference:preference-ktx:1.2.1")
}
```

#### Extension functions

##### For [PreferenceGroup](/reference/kotlin/androidx/preference/PreferenceGroup)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `PreferenceGroup.contains(preference: Preference)` Returns `true` if `preference` is found in this preference group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.forEach(action: (preference: Preference) -> Unit)` Performs the given action on each preference in this preference group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.forEachIndexed(action: (index: Int, preference: Preference) -> Unit)` Performs the given action on each preference in this preference group, providing its sequential index. |
| operator T? | `PreferenceGroup.get(key: CharSequence)` Returns the preference with `key`, or `null` if no preference with `key` is found. |
| operator [Preference](/reference/kotlin/androidx/preference/Preference) | `PreferenceGroup.get(index: Int)` Returns the preference at `index`. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `PreferenceGroup.isEmpty()` Returns true if this preference group contains no preferences. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `PreferenceGroup.isNotEmpty()` Returns true if this preference group contains one or more preferences. |
| operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)<[Preference](/reference/kotlin/androidx/preference/Preference)> | `PreferenceGroup.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the preferences in this preference group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.minusAssign(preference: Preference)` Removes `preference` from this preference group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.plusAssign(preference: Preference)` Adds `preference` to this preference group. |

#### Extension properties

##### For [PreferenceGroup](/reference/kotlin/androidx/preference/PreferenceGroup)

|  |  |
| --- | --- |
| [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)<[Preference](/reference/kotlin/androidx/preference/Preference)> | `PreferenceGroup.children()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the preferences in this preference group. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `PreferenceGroup.size()` Returns the number of preferences in this preference group. |

## androidx.room

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.room:room-ktx:2.8.5"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.room:room-ktx:2.8.5")
}
```

#### Extension functions

##### For [RoomDatabase](/reference/kotlin/androidx/room/RoomDatabase)

|  |  |
| --- | --- |
| suspend R | `RoomDatabase.withTransaction(block: suspend () -> R)` Calls the specified suspending [block](#androidx.room$withTransaction(androidx.room.RoomDatabase, kotlin.coroutines.SuspendFunction0((androidx.room.withTransaction.R)))/block) in a database transaction. |

## androidx.slice.builders

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.slice:slice-builders-ktx:1.0.0-alpha08"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.slice:slice-builders-ktx:1.0.0-alpha08")
}
```

#### Extension functions

##### For [GridRowBuilderDsl](/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl)

|  |  |
| --- | --- |
| [GridRowBuilder](/reference/kotlin/androidx/slice/builders/GridRowBuilder) | `GridRowBuilderDsl.cell(buildCell: CellBuilderDsl.() -> Unit)` |
| [GridRowBuilder](/reference/kotlin/androidx/slice/builders/GridRowBuilder) | `GridRowBuilderDsl.seeMoreCell(buildCell: CellBuilderDsl.() -> Unit)` |

##### For [ListBuilderDsl](/reference/kotlin/androidx/slice/builders/ListBuilderDsl)

|  |  |
| --- | --- |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.gridRow(buildGrid: GridRowBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.header(buildHeader: HeaderBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.inputRange(buildInputRange: InputRangeBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.range(buildRange: RangeBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.row(buildRow: RowBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.seeMoreRow(buildRow: RowBuilderDsl.() -> Unit)` |

#### Top-level functions

|  |  |
| --- | --- |
| [Slice](/reference/kotlin/androidx/slice/Slice) | `list(context: Context, uri: Uri, ttl: Long, addRows: ListBuilderDsl.() -> Unit)` Reduces verbosity required to build a Slice in Kotlin. |
| [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction) | `tapSliceAction(pendingIntent: PendingIntent, icon: IconCompat, imageMode: Int = ICON_IMAGE, title: CharSequence)` Factory method to build a tappable [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction). |
| [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction) | `toggleSliceAction(pendingIntent: PendingIntent, icon: IconCompat? = null, title: CharSequence, isChecked: Boolean)` Factory method to build a toggleable [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction). |

## androidx.sqlite.db

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.sqlite:sqlite-ktx:2.7.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.sqlite:sqlite-ktx:2.7.1")
}
```

#### Extension functions

##### For [SupportSQLiteDatabase](/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase)

|  |  |
| --- | --- |
| T | `SupportSQLiteDatabase.transaction(exclusive: Boolean = true, body: SupportSQLiteDatabase.() -> T)` Run [body](#androidx.sqlite.db$transaction(androidx.sqlite.db.SupportSQLiteDatabase, kotlin.Boolean, kotlin.Function1((androidx.sqlite.db.SupportSQLiteDatabase, androidx.sqlite.db.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.work

#### Dependency

#### Extension functions

##### For [com.google.common.util.concurrent.ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html)

|  |  |
| --- | --- |
| suspend R | `ListenableFuture<R>.await()` Awaits for the completion of the [ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html) without blocking a thread. |

##### For [Operation](/reference/kotlin/androidx/work/Operation)

|  |  |
| --- | --- |
| suspend [Operation.State.SUCCESS](/reference/kotlin/androidx/work/Operation.State.SUCCESS)! | `Operation.await()` Awaits an [Operation](/reference/kotlin/androidx/work/Operation) without blocking a thread. |

##### For [Data](/reference/kotlin/androidx/work/Data)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Data.hasKeyWithValueOfType(key: String)` Returns true if the instance of [Data](/reference/kotlin/androidx/work/Data) has a value corresponding to the given [key](#androidx.work$hasKeyWithValueOfType(androidx.work.Data, kotlin.String)/key) with an expected type T. |

##### For [Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder)

|  |  |
| --- | --- |
| [OneTimeWorkRequest.Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) | `OneTimeWorkRequest.Builder.setInputMerger(@NonNull inputMerger: KClass<out InputMerger>)` Sets an [InputMerger](/reference/kotlin/androidx/work/InputMerger) on the [OneTimeWorkRequest.Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder). |

#### Top-level functions

|  |  |
| --- | --- |
| [OneTimeWorkRequest.Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) | `OneTimeWorkRequestBuilder()` Creates a [OneTimeWorkRequest](/reference/kotlin/androidx/work/OneTimeWorkRequest) with the given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Long, repeatIntervalTimeUnit: TimeUnit)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Duration)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Long, repeatIntervalTimeUnit: TimeUnit, flexTimeInterval: Long, flexTimeIntervalUnit: TimeUnit)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Duration, flexTimeInterval: Duration)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [Data](/reference/kotlin/androidx/work/Data) | `workDataOf(vararg pairs: Pair<String, Any?>)` Converts a list of pairs to a [Data](/reference/kotlin/androidx/work/Data) object. |

## androidx.work.testing

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.work:work-testing:2.12.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.work:work-testing:2.12.0")
}
```

#### Top-level functions

|  |  |
| --- | --- |
| [TestListenableWorkerBuilder](/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder)<W> | `TestListenableWorkerBuilder(context: Context, inputData: Data = Data.EMPTY, tags: List<String> = emptyList(), runAttemptCount: Int = 1, triggeredContentUris: List<Uri> = emptyList(), triggeredContentAuthorities: List<String> = emptyList())` Builds an instance of [TestListenableWorkerBuilder](/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder). |
| [TestWorkerBuilder](/reference/kotlin/androidx/work/testing/TestWorkerBuilder)<W> | `TestWorkerBuilder(context: Context, executor: Executor, inputData: Data = Data.EMPTY, tags: List<String> = emptyList(), runAttemptCount: Int = 1, triggeredContentUris: List<Uri> = emptyList(), triggeredContentAuthorities: List<String> = emptyList())` Builds an instance of [TestWorkerBuilder](/reference/kotlin/androidx/work/testing/TestWorkerBuilder). |

## com.google.android.play.core.ktx

#### Dependency

### Groovy

```
dependencies {
    implementation "com.google.android.play:core-ktx:1.8.1"
}
```

### Kotlin

```
dependencies {
    implementation("com.google.android.play:core-ktx:1.8.1")
}
```

#### Extension functions

##### For [com.google.android.play.core.appupdate.AppUpdateManager](/reference/com/google/android/play/core/appupdate/AppUpdateManager)

|  |  |
| --- | --- |
| suspend [AppUpdateInfo](/reference/com/google/android/play/core/appupdate/AppUpdateInfo) | `AppUpdateManager.requestAppUpdateInfo()` Requests the update availability for the current app |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AppUpdateManager.requestCompleteUpdate()` For a flexible update flow, triggers the completion of the update. |
| Flow<[AppUpdateResult](/reference/com/google/android/play/core/ktx/AppUpdateResult)> | `AppUpdateManager.requestUpdateFlow()` Entry point for monitoring the availability and progress of updates. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `AppUpdateManager.startUpdateFlowForResult(appUpdateInfo: AppUpdateInfo, appUpdateType: Int, fragment: Fragment, requestCode: Int)` A version of [AppUpdateManager.startUpdateFlowForResult](/reference/com/google/android/play/core/appupdate/AppUpdateManager#startUpdateFlowForResult(com.google.android.play.core.appupdate.AppUpdateInfo,%20int,%20android.app.Activity,%20int)) that accepts an AndroidX Fragment for returning the result. |

##### For [com.google.android.play.core.splitinstall.SplitInstallManager](/reference/com/google/android/play/core/splitinstall/SplitInstallManager)

|  |  |
| --- | --- |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestCancelInstall(sessionId: Int)` Suspend version of [SplitInstallManager.cancelInstall](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#cancelInstall(int)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredInstall(moduleNames: List<String>)` Suspend version of [SplitInstallManager.deferredInstall](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredInstall(java.util.List<java.lang.String>)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredLanguageInstall(languages: List<Locale>)` Suspend version of [SplitInstallManager.deferredLanguageInstall](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredLanguageInstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredLanguageUninstall(languages: List<Locale>)` Suspend version of [SplitInstallManager.deferredLanguageUninstall](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredLanguageUninstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredUninstall(moduleNames: List<String>)` Suspend version of [SplitInstallManager.deferredUninstall](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredUninstall(java.util.List<java.lang.String>)) |
| suspend [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallManager.requestInstall(modules: List<String> = listOf(), languages: List<String> = listOf())` Initiates installation of the requested modules/languages. |
| Flow<[SplitInstallSessionState](/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)> | `SplitInstallManager.requestProgressFlow()` Creates and returns a buffered [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) that will deliver all progress events for ongoing split installations. |
| suspend [SplitInstallSessionState](/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState) | `SplitInstallManager.requestSessionState(sessionId: Int)` Suspend version of [SplitInstallManager.getSessionState](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getSessionState(int)) |
| suspend [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[SplitInstallSessionState](/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)> | `SplitInstallManager.requestSessionStates()` Suspend version of [SplitInstallManager.getSessionStates](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getSessionStates()) |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SplitInstallManager.startConfirmationDialogForResult(sessionState: SplitInstallSessionState, fragment: Fragment, requestCode: Int)` A version of [SplitInstallManager.startConfirmationDialogForResult](/reference/com/google/android/play/core/splitinstall/SplitInstallManager#startConfirmationDialogForResult(com.google.android.play.core.splitinstall.SplitInstallSessionState,%20android.app.Activity,%20int)) that accepts an AndroidX Fragment for returning the result. |

#### Extension properties

##### For [com.google.android.play.core.appupdate.AppUpdateInfo](/reference/com/google/android/play/core/appupdate/AppUpdateInfo)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `AppUpdateInfo.installStatus()` Returns the progress status of the update. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `AppUpdateInfo.isFlexibleUpdateAllowed()` Returns `true` if flexible update is allowed. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `AppUpdateInfo.isImmediateUpdateAllowed()` Returns `true` if immediate update is allowed. |

##### For [com.google.android.play.core.install.InstallState](/reference/com/google/android/play/core/install/InstallState)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `InstallState.hasTerminalStatus()` This signifies that this is a terminal status (there will be no more updates) and should be handled accordingly (success, cancellation or failure). |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `InstallState.installErrorCode()` Returns the error code for an install, or {@link InstallErrorCode#NO\_ERROR}. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `InstallState.installStatus()` Returns the status of an install. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)! | `InstallState.packageName()` Returns the package name for the app being installed. |

##### For [com.google.android.play.core.splitinstall.SplitInstallSessionState](/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)

|  |  |
| --- | --- |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SplitInstallSessionState.bytesDownloaded()` The bytes downloaded by this update. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallSessionState.errorCode()` The error code of this update. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SplitInstallSessionState.hasTerminalStatus()` Signifies that this update is terminal, meaning there will be no more updates for this session. |
| [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> | `SplitInstallSessionState.languages()` The languages included by this update. |
| [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)> | `SplitInstallSessionState.moduleNames()` The modules included by this update. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallSessionState.sessionId()` The session id of this update. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallSessionState.status()` The status code of this update. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SplitInstallSessionState.totalBytesToDownload()` The total bytes to download by this update. |

#### Top-level functions

|  |  |
| --- | --- |
| [SplitInstallStateUpdatedListener](/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener) | `SplitInstallStateUpdatedListener(onRequiresConfirmation: (SplitInstallSessionState) -> Unit, onInstalled: (SplitInstallSessionState) -> Unit, onFailed: (SplitInstallSessionState) -> Unit = {}, onPending: (SplitInstallSessionState) -> Unit = {}, onDownloaded: (SplitInstallSessionState) -> Unit = {}, onDownloading: (SplitInstallSessionState) -> Unit = {}, onInstalling: (SplitInstallSessionState) -> Unit = {}, onCanceling: (SplitInstallSessionState) -> Unit = {}, onCanceled: (SplitInstallSessionState) -> Unit = {}, onNonTerminalStatus: (SplitInstallSessionState) -> Unit = {}, onTerminalStatus: (SplitInstallSessionState) -> Unit = {})` A convenience function for creating a [SplitInstallStateUpdatedListener](/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener). |
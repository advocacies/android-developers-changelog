---
title: Create ViewModels with dependencies  |  App architecture  |  Android Developers
url: https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-factories
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

Stay organized with collections

Save and categorize content based on your preferences.





# Create ViewModels with dependencies   Part of [Android Jetpack](/jetpack).

Following [dependency injection's](/dependency-injection) best practices, ViewModels can
take dependencies as parameters in their constructor. These are mostly of types
from the [domain](/topic/architecture/domain-layer) or [data](/topic/architecture/data-layer) layers. Because the framework provides the
ViewModels, a special mechanism is required to create instances of them. That
mechanism is the `ViewModelProvider.Factory` interface. Only **implementations
of this interface can instantiate ViewModels in the right scope**.

**Note:** If the `ViewModel` takes no dependencies or just the [SavedStateHandle
type as a dependency](/topic/libraries/architecture/viewmodel-savedstate), you don't need to provide a factory for the framework
to instantiate instances of that `ViewModel` type.**Note:** When [injecting ViewModels using Hilt](/training/dependency-injection/hilt-jetpack#viewmodels) as a dependency injection
solution, you don't have to define a `ViewModel` factory manually. Hilt
generates a factory that knows how to create all ViewModels annotated with
`@HiltViewModel` for you at compile time. Classes annotated with
`@AndroidEntryPoint` can directly access the Hilt generated factory when calling
the regular `ViewModel` APIs.

## ViewModels with CreationExtras

If a `ViewModel` class receives dependencies in its constructor, provide a
factory that implements the [`ViewModelProvider.Factory`](/reference/androidx/lifecycle/ViewModelProvider.Factory) interface.
Override the [`create(Class<T>, CreationExtras)`](/reference/androidx/lifecycle/ViewModelProvider.Factory#create(java.lang.Class,androidx.lifecycle.viewmodel.CreationExtras)) function to provide a
new instance of the ViewModel.

[`CreationExtras`](/reference/androidx/lifecycle/viewmodel/CreationExtras) allows you to access relevant information that helps
instantiate a ViewModel. Here's a list of keys that can be accessed from extras:

| Key | Functionality |
| --- | --- |
| [`ViewModelProvider.NewInstanceFactory.VIEW_MODEL_KEY`](/reference/kotlin/androidx/lifecycle/ViewModelProvider#VIEW_MODEL_KEY()) | Provides access to the custom key you passed to `ViewModelProvider.get()`. |
| [`ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY`](/reference/kotlin/androidx/lifecycle/ViewModelProvider.AndroidViewModelFactory#APPLICATION_KEY()) | Provides access to the instance of the `Application` class. |
| [`SavedStateHandleSupport.DEFAULT_ARGS_KEY`](/reference/kotlin/androidx/lifecycle/package-summary#DEFAULT_ARGS_KEY()) | Provides access to the Bundle of arguments you should use to construct `SavedStateHandle`. |
| [`SavedStateHandleSupport.SAVED_STATE_REGISTRY_OWNER_KEY`](/reference/kotlin/androidx/lifecycle/package-summary#SAVED_STATE_REGISTRY_OWNER_KEY()) | Provides access to the `SavedStateRegistryOwner` that is being used to construct the `ViewModel`. |
| [`SavedStateHandleSupport.VIEW_MODEL_STORE_OWNER_KEY`](/reference/kotlin/androidx/lifecycle/package-summary#VIEW_MODEL_STORE_OWNER_KEY()) | Provides access to the `ViewModelStoreOwner` that is being used to construct the `ViewModel`. |

To create a new instance of [`SavedStateHandle`](/topic/libraries/architecture/viewmodel-savedstate), use the
[`CreationExtras.createSavedStateHandle()`](/reference/androidx/lifecycle/SavedStateHandleSupport#(androidx.lifecycle.viewmodel.CreationExtras)
function and pass it to the ViewModel.

### CreationExtras with APPLICATION\_KEY

The following is an example of how to provide an instance of a `ViewModel` that
takes a [repository](/topic/architecture/data-layer#architecture) scoped to the `Application` class and
`SavedStateHandle` as dependencies:

```
    import androidx.lifecycle.SavedStateHandle
    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.ViewModelProvider
    import androidx.lifecycle.ViewModelProvider.AndroidViewModelFactory.Companion.APPLICATION_KEY
    import androidx.lifecycle.createSavedStateHandle
    import androidx.lifecycle.viewmodel.initializer
    import androidx.lifecycle.viewmodel.viewModelFactory

    class MyViewModel(
        private val myRepository: MyRepository,
        private val savedStateHandle: SavedStateHandle
    ) : ViewModel() {

        // ViewModel logic
        // ...

        // Define ViewModel factory in a companion object
        companion object {

            val Factory: ViewModelProvider.Factory = viewModelFactory {
                initializer {
                    val savedStateHandle = createSavedStateHandle()
                    val myRepository = (this[APPLICATION_KEY] as MyApplication).myRepository
                    MyViewModel(
                        myRepository = myRepository,
                        savedStateHandle = savedStateHandle
                    )
                }
            }
        }
    }
```

**Note:** It's a good practice to place `ViewModel` factories in their ViewModel
file for better context, readability, and easier discovery. The same ViewModel
factory can be used for multiple ViewModels when they share dependencies, as
it's the case for the [Architecture Blueprints](https://github.com/android/architecture-samples/blob/32cd12f7838c5a2df93546ec3e699376b2b6b37a/app/src/main/java/com/example/android/architecture/blueprints/todoapp/ViewModelFactory.kt#L34) sample.

Then, you can use this factory when retrieving an instance of the ViewModel:

```
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun MyScreen(
    modifier: Modifier = Modifier,
    viewModel: MyViewModel = viewModel(factory = MyViewModel.Factory)
) {
    // ...
}
```

### Pass custom parameters as CreationExtras

You can pass dependencies to your `ViewModel` through `CreationExtras` by
creating a custom key.
This can be useful if your `ViewModel` depends on objects which are not
accessible through the `Application` class and `APPLICATION_KEY`. An example of
this is when your `ViewModel` is created inside a Kotlin
Multiplatform module and therefore does not have access to Android dependencies.

In this example, the `ViewModel` defines a custom key and uses it in the
`ViewModelProvider.Factory`.

```
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.viewmodel.CreationExtras
import androidx.lifecycle.viewmodel.initializer
import androidx.lifecycle.viewmodel.viewModelFactory

class MyViewModel(
    private val myRepository: MyRepository,
) : ViewModel() {
    // ViewModel logic

    // Define ViewModel factory in a companion object
    companion object {

        // Define a custom key using the factory function
        val MY_REPOSITORY_KEY = CreationExtras.Key<MyRepository>()

        val Factory: ViewModelProvider.Factory = viewModelFactory {
            initializer {
                // Get the dependency in your factory
                val myRepository = this[MY_REPOSITORY_KEY] as MyRepository
                MyViewModel(
                    myRepository = myRepository,
                )
            }
        }
    }
}
```

You can instantiate a `ViewModel` with a `CreationExtras.Key` directly in your
composables.

```
import androidx.lifecycle.viewmodel.MutableCreationExtras
import androidx.lifecycle.viewmodel.compose.viewModel
// ...
@Composable
fun MyApp(myRepository: MyRepository) {
    val extras = MutableCreationExtras().apply {
        set(MyViewModel.MY_REPOSITORY_KEY, myRepository)
    }
    val viewModel: MyViewModel = viewModel(
        factory = MyViewModel.Factory,
        extras = extras,
    )
}
```

## Additional resources

To learn more about ViewModels and dependencies, see the following additional
resources:

### Documentation

* [Dependency injection in Android](/training/dependency-injection)

### Views content

* [Create ViewModels with dependencies (Views)](/topic/libraries/architecture/views/viewmodel/viewmodel-factories-views)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Saved State module for ViewModel](/topic/libraries/architecture/viewmodel/viewmodel-savedstate)
* [Save UI states](/topic/libraries/architecture/saving-states)
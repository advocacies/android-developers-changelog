---
title: Play Age Signals API error code reference  |  Android Developers
url: https://developer.android.com/google/play/age-signals/handle-errors
source: html-scrape
---

On March 17, 2026, the Play Age Signals API started returning age signals for users in Brazil for [requirements under Digital ECA](https://support.google.com/googleplay/android-developer/answer/6223646#digital_eca_requirements). The API has started returning age signals for eligible users in Texas who created their accounts after May 28, 2026 as part of our compliance efforts for Texas SB2420. Ongoing updates will be provided in advance of [age verification bills](http://support.google.com/googleplay/android-developer/answer/16569691) in other US states.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Age Signals](https://developer.android.com/google/play/age-signals)

# Play Age Signals API error code reference Stay organized with collections Save and categorize content based on your preferences.





If your app makes a Play Age Signals API request and the call fails, your app
receives an error code. These errors can happen for various reasons, such as the
Play Store app being out of date.

**Retry strategy**: In situations where the user is in session, we recommend
implementing a retry strategy with a maximum number of attempts as an exit
condition so that the error disrupts the user experience as little as possible.

The following table lists error codes for the Play Age Signals API.

Code | Constant | Description | Retryable || -1 | API\_NOT\_AVAILABLE | The Play Age Signals API is not available. The Play Store app version installed on the device might be old. Ask the user to update the Play Store. | Yes |
| -2 | PLAY\_STORE\_NOT\_FOUND | No Play Store app is found on the device. Ask the user to install or enable the Play Store. | Yes |
| -3 | NETWORK\_ERROR | No available network is found. Ask the user to check for a connection. | Yes |
| -4 | PLAY\_SERVICES\_NOT\_FOUND | Play Services is not available or its version is too old. Ask the user to install, update, or enable Play Services. | Yes |
| -5 | CANNOT\_BIND\_TO\_SERVICE | Binding to the service in the Play Store has failed. This can be due to having an old Play Store version installed on the device or device memory is overloaded. Ask the user to update the Play Store app. Retry with an exponential backoff. | Yes |
| -6 | PLAY\_STORE\_VERSION\_OUTDATED | The Play Store app needs to be updated. Ask the user to update the Play Store app. | Yes |
| -7 | PLAY\_SERVICES\_VERSION\_OUTDATED | Play Services needs to be updated. Ask the user to update Play Services. | Yes |
| -8 | CLIENT\_TRANSIENT\_ERROR | There was a transient error in the client device. Implement a retry strategy with a maximum number of attempts as an exit condition. If the issue still doesn't resolve, ask the user to try again later. | Yes |
| -9 | APP\_NOT\_OWNED | The app was not installed by Google Play. Ask the user to get your app from Google Play. | No |
| -10 | SDK\_VERSION\_OUTDATED | The Play Age Signals SDK version is no longer supported. Ask the user to update your app to a later version that uses a recent version of the Play Age Signals SDK. | No |
| -100 | INTERNAL\_ERROR | Unknown internal error. Implement a retry strategy with a maximum number of attempts as an exit condition. If the issue still doesn't resolve, ask the user to try again later. If it fails consistently, [contact Google Play Developer support](https://support.google.com/googleplay/android-developer/gethelp), include Play Age Signals API in the subject, and include as much technical detail as possible (such as a bug report). | No |

[Previous

arrow\_back

Test age signals](/google/play/age-signals/test-age-signals-api)

[Next

Notify significant changes

arrow\_forward](/google/play/age-signals/notify-significant-changes)
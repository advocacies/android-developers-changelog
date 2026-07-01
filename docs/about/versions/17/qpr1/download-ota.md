---
title: OTA images for Google Pixel  |  Android Developers
url: https://developer.android.com/about/versions/17/qpr1/download-ota
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# OTA images for Google Pixel Stay organized with collections Save and categorize content based on your preferences.





Applying an OTA image can help you recover a device that received an OTA update
for an Android 17 Beta build but wouldn't start up
after the update was installed. If you are trying to get Android 17 on your
device but you aren't trying to recover from a failed OTA update, see [Get
Android 17](/about/versions/17/get) instead.

Building on the [initial release of Android 17](/about/versions/17), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

To find OTA images for already-released, stable versions of the platform, see
[Full OTA Images for Nexus and Pixel Devices](https://developers.google.com/android/ota).

Applying an OTA image can help you recover a device that received an OTA update
for an Android 17 QPR beta build but wouldn't start up after the update was
installed. If you are trying to get Android 17 QPR1 on your device but
you aren't trying to recover from a failed OTA update, see [Get Android 17 QPR
beta builds](/about/versions/17/get-qpr) instead.

OTA images are available for the following Pixel devices:

* Pixel 6
* Pixel 6 Pro
* Pixel 6a
* Pixel 7
* Pixel 7 Pro
* Pixel 7a
* Pixel Tablet
* Pixel Fold
* Pixel 8
* Pixel 8 Pro
* Pixel 8a
* Pixel 9
* Pixel 9 Pro
* Pixel 9 Pro XL
* Pixel 9 Pro Fold
* Pixel 9a
* Pixel 10
* Pixel 10 Pro
* Pixel 10 Pro XL
* Pixel 10 Pro Fold
* Pixel 10a

After you've installed a beta build to your Pixel device, your device is
automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered
continuous over-the-air (OTA) updates to the latest beta builds (including QPRs)
until you choose to unenroll that device from the program.

We also deliver flashable images at each milestone, so you can choose the
approach that works best for your test environment.

Use the following links and instructions to update your supported device to the
latest build. See [Get Android 17](/about/versions/17/get) for
other ways to get Android 17 for testing and development.

## Apply an OTA image

![](/static/images/lockups/android-stacked.svg)

Download an OTA device image from the following table and apply it by following
the [updating instructions](https://developers.google.com/android/ota#instructions) listed on [Full OTA Images for Nexus and Pixel
Devices](https://developers.google.com/android/ota).

You can choose to [return to the latest public build](#public) at any time.

**Warning:** Before applying an Android 17 OTA image, we strongly recommend that you
[unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader
requires a full device reset that removes all user data on the device, so make
sure to back up your data first.

### Device OTA Images

|  |  |
| --- | --- |
| **Release date** | June 23, 2026 |
| **Builds** | CP31.260608.007 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-06-05 |
| **Google Play services** | 26.18.35 |

| Device | Download Link and SHA-256 Checksum |
| --- | --- |
| Pixel 6a | bluejay\_beta-ota-cp31.260608.007-d419a710.zip  `d419a710a04ed75ddcead5a5aa9ebaac2b2868ec94875d58d1f84feb028b4892` |
| Pixel 7 | panther\_beta-ota-cp31.260608.007-841cd965.zip  `841cd965865ea6e5fcc0d0eb5d068d697c5d916dd340538cf0f1f9a431122246` |
| Pixel 7 Pro | cheetah\_beta-ota-cp31.260608.007-892bc925.zip  `892bc9257e299c62ca428203fce0cc4eaec3b1a2e99abf2cb1b2dec81f2908e7` |
| Pixel 7a | lynx\_beta-ota-cp31.260608.007-b975e270.zip  `b975e270536a5e942bb00c4bd8aa9a94761f6c203e5150e8823804065a032fc0` |
| Pixel Fold | felix\_beta-ota-cp31.260608.007-41e19511.zip  `41e195114042046b0d47b760f6a54feab769dd4edb421f17a8dc260c54164fc6` |
| Pixel Tablet | tangorpro\_beta-ota-cp31.260608.007-b03533c3.zip  `b03533c389ae2fa15d9843d7402eaf024ee24f9349caad3591151bef7b545e47` |
| Pixel 8 | shiba\_beta-ota-cp31.260608.007-899dcc4f.zip  `899dcc4ff7effb3cafb2eb160011c60cb8cdb6816b4eb66f85fb7e21358e2d79` |
| Pixel 8 Pro | husky\_beta-ota-cp31.260608.007-782dfb5b.zip  `782dfb5bf86344a059f4e03ba82dcc9a20034da1b1b6b4ca878cee9e4293052b` |
| Pixel 8a | akita\_beta-ota-cp31.260608.007-3a29ca79.zip  `3a29ca79e8c4256c5823bfe003763e1b13d1fe30d87f3012fef0a8d6efb44608` |
| Pixel 9 | tokay\_beta-ota-cp31.260608.007-5ad2d12b.zip  `5ad2d12bec7823aacb8532bd1368cf1e78a47526371a5d6e1274e4fb7ebeccc7` |
| Pixel 9 Pro | caiman\_beta-ota-cp31.260608.007-442c8a1e.zip  `442c8a1e66af220476677e44596a661f40c2e38463927d24f5e3986a9658f16f` |
| Pixel 9 Pro XL | komodo\_beta-ota-cp31.260608.007-21fd04fb.zip  `21fd04fbcdbecb4e24e701b805c2511ba1fee25e96eab8fa2044d49136197a48` |
| Pixel 9 Pro Fold | comet\_beta-ota-cp31.260608.007-13cc7446.zip  `13cc7446002900976f16520049845268329648850bdbbad8c371407d6df78fcb` |
| Pixel 9a | tegu\_beta-ota-cp31.260608.007-64c2a401.zip  `64c2a4013b2ff05b71eb83921daabc50d2036f402e6e15ae27961ea745b31ed8` |
| Pixel 10 | frankel\_beta-ota-cp31.260608.007-03f0c3f4.zip  `03f0c3f4051cd08f14855db5579e466b0b8ef152d1ba64476298711e0316d60e` |
| Pixel 10 Pro | blazer\_beta-ota-cp31.260608.007-4d90d2fb.zip  `4d90d2fb88cd4b0639ac4cc40dc31a0dcb02d67173132c1d0db7bc17b315d833` |
| Pixel 10 Pro XL | mustang\_beta-ota-cp31.260608.007-83d59c20.zip  `83d59c20ea3cf3ec5abaf3720af761fcafebcc293d31222762a4daf85c649f01` |
| Pixel 10 Pro Fold | rango\_beta-ota-cp31.260608.007-a1c9ad13.zip  `a1c9ad139f71a1d66570aa510c4989506dc706239ed719947e8ccf1c596804d0` |
| Pixel 10a | stallion\_beta-ota-cp31.260608.007-bf5f484f.zip  `bf5f484f1f8cb29bc8ad80cc3a69f07dca2bd633a504afc1fa9027922b275695` |

## Return to a public build

You can either use the Android Flash Tool to
[flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system
image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
page and then manually flash it to the device.

**Warning:** Going back to a public build from a preview build (Developer Preview
or Beta) requires a full device reset that removes all user data on the device.
Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/bluejay_beta-ota-cp31.260608.007-d419a710.zip)

*bluejay\_beta-ota-cp31.260608.007-d419a710.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/panther_beta-ota-cp31.260608.007-841cd965.zip)

*panther\_beta-ota-cp31.260608.007-841cd965.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/cheetah_beta-ota-cp31.260608.007-892bc925.zip)

*cheetah\_beta-ota-cp31.260608.007-892bc925.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/lynx_beta-ota-cp31.260608.007-b975e270.zip)

*lynx\_beta-ota-cp31.260608.007-b975e270.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/felix_beta-ota-cp31.260608.007-41e19511.zip)

*felix\_beta-ota-cp31.260608.007-41e19511.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tangorpro_beta-ota-cp31.260608.007-b03533c3.zip)

*tangorpro\_beta-ota-cp31.260608.007-b03533c3.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/shiba_beta-ota-cp31.260608.007-899dcc4f.zip)

*shiba\_beta-ota-cp31.260608.007-899dcc4f.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/husky_beta-ota-cp31.260608.007-782dfb5b.zip)

*husky\_beta-ota-cp31.260608.007-782dfb5b.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/akita_beta-ota-cp31.260608.007-3a29ca79.zip)

*akita\_beta-ota-cp31.260608.007-3a29ca79.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tokay_beta-ota-cp31.260608.007-5ad2d12b.zip)

*tokay\_beta-ota-cp31.260608.007-5ad2d12b.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/caiman_beta-ota-cp31.260608.007-442c8a1e.zip)

*caiman\_beta-ota-cp31.260608.007-442c8a1e.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/komodo_beta-ota-cp31.260608.007-21fd04fb.zip)

*komodo\_beta-ota-cp31.260608.007-21fd04fb.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/comet_beta-ota-cp31.260608.007-13cc7446.zip)

*comet\_beta-ota-cp31.260608.007-13cc7446.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/tegu_beta-ota-cp31.260608.007-64c2a401.zip)

*tegu\_beta-ota-cp31.260608.007-64c2a401.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/frankel_beta-ota-cp31.260608.007-03f0c3f4.zip)

*frankel\_beta-ota-cp31.260608.007-03f0c3f4.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/blazer_beta-ota-cp31.260608.007-4d90d2fb.zip)

*blazer\_beta-ota-cp31.260608.007-4d90d2fb.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/mustang_beta-ota-cp31.260608.007-83d59c20.zip)

*mustang\_beta-ota-cp31.260608.007-83d59c20.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/rango_beta-ota-cp31.260608.007-a1c9ad13.zip)

*rango\_beta-ota-cp31.260608.007-a1c9ad13.zip*

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software
Development Kit License Agreement (available at
https://developer.android.com/studio/terms and such URL may be updated or
changed by Google from time to time), which will terminate when Google issues a
final release version.  
  
Your testing and feedback are important part of the development process and by
using the SDK, you acknowledge that (i) implementation of some features are
still under development, (ii) you should not rely on the SDK having the full
functionality of a stable release; (iii) you agree not to publicly distribute or
ship any application using this SDK as this SDK will no longer be supported
after the official Android SDK is released; and (iv) you agree that Google may
deliver elements of the SDK to your devices via auto-update (OTA or otherwise,
in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE
AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE
RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN
RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE
OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.

I have read and agree with the above terms and conditions

Download Android 17 OTA system image
[Download Android 17 OTA system image](https://dl.google.com/developers/android/cinnamonbun/images/ota/stallion_beta-ota-cp31.260608.007-bf5f484f.zip)

*stallion\_beta-ota-cp31.260608.007-bf5f484f.zip*
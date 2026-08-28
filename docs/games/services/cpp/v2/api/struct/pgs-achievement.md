---
title: PgsAchievement Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# PgsAchievement

Represents a single achievement.

## Summary

| Public attributes | |
| --- | --- |
| `achievement_id` | `const char *`  The ID of this achievement. |
| `current_steps` | `int32_t`  The number of steps completed if this is an incremental achievement, 0 otherwise. |
| `description` | `const char *`  The description of this achievement. |
| `last_updated_timestamp` | `int64_t`  The timestamp (in milliseconds since epoch) at which this achievement was last updated. |
| `name` | `const char *`  The name of this achievement. |
| `revealed_image_uri` | `const char *`  The URI for the revealed image of this achievement. |
| `state` | `PgsAchievementState`  The state of this achievement. |
| `total_steps` | `int32_t`  The total number of steps if this is an incremental achievement, 0 otherwise. |
| `type` | `PgsAchievementType`  The type of this achievement. |
| `unlocked_image_uri` | `const char *`  The URI for the unlocked image of this achievement. |
| `xp_value` | `int64_t`  The XP value of this achievement. |

## Public attributes

### achievement\_id

```
const char * PgsAchievement::achievement_id
```

The ID of this achievement.

### current\_steps

```
int32_t PgsAchievement::current_steps
```

The number of steps completed if this is an incremental achievement, 0 otherwise.

### description

```
const char * PgsAchievement::description
```

The description of this achievement.

### last\_updated\_timestamp

```
int64_t PgsAchievement::last_updated_timestamp
```

The timestamp (in milliseconds since epoch) at which this achievement was last updated.

### name

```
const char * PgsAchievement::name
```

The name of this achievement.

### revealed\_image\_uri

```
const char * PgsAchievement::revealed_image_uri
```

The URI for the revealed image of this achievement.

### state

```
PgsAchievementState PgsAchievement::state
```

The state of this achievement.

### total\_steps

```
int32_t PgsAchievement::total_steps
```

The total number of steps if this is an incremental achievement, 0 otherwise.

### type

```
PgsAchievementType PgsAchievement::type
```

The type of this achievement.

### unlocked\_image\_uri

```
const char * PgsAchievement::unlocked_image_uri
```

The URI for the unlocked image of this achievement.

### xp\_value

```
int64_t PgsAchievement::xp_value
```

The XP value of this achievement.
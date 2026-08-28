---
title: PgsScoreSubmissionData Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# PgsScoreSubmissionData

Play Games Services score submission data.

## Summary

| Public attributes | |
| --- | --- |
| `all_time_result` | `PgsScoreSubmissionResult *`  Result for all-time timespan. |
| `daily_result` | `PgsScoreSubmissionResult *`  Result for daily timespan. |
| `leaderboard_id` | `char *`  The leaderboard ID that the score was submitted to. |
| `player_id` | `char *`  The player ID submitting the score. |
| `weekly_result` | `PgsScoreSubmissionResult *`  Result for weekly timespan. |

## Public attributes

### all\_time\_result

```
PgsScoreSubmissionResult * PgsScoreSubmissionData::all_time_result
```

Result for all-time timespan.

### daily\_result

```
PgsScoreSubmissionResult * PgsScoreSubmissionData::daily_result
```

Result for daily timespan.

### leaderboard\_id

```
char * PgsScoreSubmissionData::leaderboard_id
```

The leaderboard ID that the score was submitted to.

### player\_id

```
char * PgsScoreSubmissionData::player_id
```

The player ID submitting the score.

### weekly\_result

```
PgsScoreSubmissionResult * PgsScoreSubmissionData::weekly_result
```

Result for weekly timespan.
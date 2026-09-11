---
title: Score Submission Data  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/score-submission-data
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# Score Submission Data

Native API for Play Games Services Score Submission Data.

## Summary

| Typedefs | |
| --- | --- |
| `PgsScoreSubmissionData` | typedef `struct PgsScoreSubmissionData`  Play Games Services score submission data. |
| `PgsScoreSubmissionResult` | typedef `struct PgsScoreSubmissionResult`  A Play Games Services score submission result. |

| Functions | |
| --- | --- |
| `PgsScoreSubmissionData_Release(PgsScoreSubmissionData *data)` | `void`  Releases memory used by score submission data. |

| Structs | |
| --- | --- |
| [PgsScoreSubmissionData](/games/services/cpp/v2/api/struct/pgs-score-submission-data) | Play Games Services score submission data. |
| [PgsScoreSubmissionResult](/games/services/cpp/v2/api/struct/pgs-score-submission-result) | A Play Games Services score submission result. |

## Typedefs

### PgsScoreSubmissionData

```
struct PgsScoreSubmissionData PgsScoreSubmissionData
```

Play Games Services score submission data.

### PgsScoreSubmissionResult

```
struct PgsScoreSubmissionResult PgsScoreSubmissionResult
```

A Play Games Services score submission result.

## Functions

### PgsScoreSubmissionData\_Release

```
void PgsScoreSubmissionData_Release(
  PgsScoreSubmissionData *data
)
```

Releases memory used by score submission data.
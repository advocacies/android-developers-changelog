---
title: Play Games Services Leaderboards  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/leaderboards
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# Play Games Services Leaderboards

Native API for Play Games Services Leaderboards.

## Summary

| Enumerations | |
| --- | --- |
| `PgsLeaderboardCollection{   PGS_LEADERBOARD_COLLECTION_PUBLIC = 0,   PGS_LEADERBOARD_COLLECTION_FRIENDS = 3 }` | enum Represents the collection type for a leaderboard. |
| `PgsLeaderboardTimeSpan{   PGS_LEADERBOARD_TIME_SPAN_DAILY = 0,   PGS_LEADERBOARD_TIME_SPAN_WEEKLY = 1,   PGS_LEADERBOARD_TIME_SPAN_ALL_TIME = 2 }` | enum Represents the time span for a leaderboard. |

| Typedefs | |
| --- | --- |
| `PgsLeaderboardScoreBuffer` | typedef `struct PgsLeaderboardScoreBuffer`  An opaque handle to a leaderboard score buffer. |
| `PgsLeaderboardsClient_LoadCurrentPlayerLeaderboardScoreCallback)(PgsStatusCode status_code, PgsLeaderboardScore *score, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_loadCurrentPlayerLeaderboardScore. |
| `PgsLeaderboardsClient_LoadLeaderboardMetadataCallback)(PgsStatusCode status_code, const PgsLeaderboard *leaderboards, size_t leaderboard_count, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_loadLeaderboardMetadata. |
| `PgsLeaderboardsClient_LoadLeaderboardMetadataWithIdCallback)(PgsStatusCode status_code, const PgsLeaderboard *leaderboard, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_loadLeaderboardMetadataWithId. |
| `PgsLeaderboardsClient_LoadMoreScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_loadMoreScores. |
| `PgsLeaderboardsClient_LoadPlayerCenteredScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_loadPlayerCenteredScores. |
| `PgsLeaderboardsClient_LoadTopScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_loadTopScores. |
| `PgsLeaderboardsClient_ShowAllLeaderboardsUICallback)(PgsStatusCode status_code, bool success, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_showAllLeaderboardsUI. |
| `PgsLeaderboardsClient_ShowLeaderboardUICallback)(PgsStatusCode status_code, bool success, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_showLeaderboardUI. |
| `PgsLeaderboardsClient_SubmitScoreImmediateCallback)(PgsStatusCode status_code, PgsScoreSubmissionData *score_submission_data, void *user_data)` | typedef `void(*`  Callback for PgsLeaderboardsClient\_submitScoreImmediate. |

| Functions | |
| --- | --- |
| `PgsLeaderboardsClient_loadCurrentPlayerLeaderboardScore(PgsLeaderboardsClient *leaderboards_client, const char *leaderboard_id, PgsLeaderboardTimeSpan time_span, PgsLeaderboardCollection collection, PgsLeaderboardsClient_LoadCurrentPlayerLeaderboardScoreCallback callback, void *user_data)` | `void`  Asynchronously loads the current player's score for a specific leaderboard with time span and collection. |
| `PgsLeaderboardsClient_loadLeaderboardMetadata(PgsLeaderboardsClient *leaderboards_client, bool force_reload, PgsLeaderboardsClient_LoadLeaderboardMetadataCallback callback, void *user_data)` | `void`  Asynchronously loads leaderboard metadata. |
| `PgsLeaderboardsClient_loadLeaderboardMetadataWithId(PgsLeaderboardsClient *leaderboards_client, const char *leaderboard_id, bool force_reload, PgsLeaderboardsClient_LoadLeaderboardMetadataWithIdCallback callback, void *user_data)` | `void`  Asynchronously loads metadata for a specific leaderboard. |
| `PgsLeaderboardsClient_loadMoreScores(PgsLeaderboardsClient *leaderboards_client, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, int32_t max_results, int32_t page_direction, PgsLeaderboardsClient_LoadMoreScoresCallback callback, void *user_data)` | `void`  Asynchronously loads more scores for a given leaderboard score buffer. |
| `PgsLeaderboardsClient_loadPlayerCenteredScores(PgsLeaderboardsClient *leaderboards_client, const char *leaderboard_id, int32_t span, int32_t collection, int32_t max_results, bool force_reload, PgsLeaderboardsClient_LoadPlayerCenteredScoresCallback callback, void *user_data)` | `void`  Asynchronously loads player-centered scores for a specific leaderboard. |
| `PgsLeaderboardsClient_loadTopScores(PgsLeaderboardsClient *leaderboards_client, const char *leaderboard_id, PgsLeaderboardTimeSpan time_span, PgsLeaderboardCollection collection, int32_t max_results, bool force_reload, PgsLeaderboardsClient_LoadTopScoresCallback callback, void *user_data)` | `void`  Asynchronously loads top scores for a specific leaderboard. |
| `PgsLeaderboardsClient_showAllLeaderboardsUI(PgsLeaderboardsClient *leaderboards_client, jobject activity, PgsLeaderboardsClient_ShowAllLeaderboardsUICallback callback, void *user_data)` | `void`  Asynchronously loads and displays the standard leaderboards UI. |
| `PgsLeaderboardsClient_showLeaderboardUI(PgsLeaderboardsClient *leaderboards_client, jobject activity, const char *leaderboard_id, PgsLeaderboardTimeSpan time_span, PgsLeaderboardCollection collection, PgsLeaderboardsClient_ShowLeaderboardUICallback callback, void *user_data)` | `void`  Asynchronously loads and displays the UI for a specific leaderboard with time span and collection. |
| `PgsLeaderboardsClient_submitScoreImmediate(PgsLeaderboardsClient *leaderboards_client, const char *leaderboard_id, int64_t score, const char *score_tag, PgsLeaderboardsClient_SubmitScoreImmediateCallback callback, void *user_data)` | `void`  Submits a score to a leaderboard. |

## Enumerations

### PgsLeaderboardCollection

```
 PgsLeaderboardCollection
```

Represents the collection type for a leaderboard.

| Properties | |
| --- | --- |
| `PGS_LEADERBOARD_COLLECTION_FRIENDS` | Friends leaderboards. |
| `PGS_LEADERBOARD_COLLECTION_PUBLIC` | Public leaderboards. |

### PgsLeaderboardTimeSpan

```
 PgsLeaderboardTimeSpan
```

Represents the time span for a leaderboard.

| Properties | |
| --- | --- |
| `PGS_LEADERBOARD_TIME_SPAN_ALL_TIME` | Scores are never reset. |
| `PGS_LEADERBOARD_TIME_SPAN_DAILY` | Scores are reset every day. |
| `PGS_LEADERBOARD_TIME_SPAN_WEEKLY` | Scores are reset once per week. |

## Typedefs

### PgsLeaderboardScoreBuffer

```
struct PgsLeaderboardScoreBuffer PgsLeaderboardScoreBuffer
```

An opaque handle to a leaderboard score buffer.

### PgsLeaderboardsClient\_LoadCurrentPlayerLeaderboardScoreCallback

```
void(* PgsLeaderboardsClient_LoadCurrentPlayerLeaderboardScoreCallback)(PgsStatusCode status_code, PgsLeaderboardScore *score, void *user_data)
```

Callback for PgsLeaderboardsClient\_loadCurrentPlayerLeaderboardScore.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `score` | Pointer to a leaderboard score. This may be NULL if status\_code is not PGS\_STATUS\_SUCCESS, or if the player has no score on this leaderboard. The caller must call PgsLeaderboardScore\_Release on the score when it is no longer needed. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_LoadLeaderboardMetadataCallback

```
void(* PgsLeaderboardsClient_LoadLeaderboardMetadataCallback)(PgsStatusCode status_code, const PgsLeaderboard *leaderboards, size_t leaderboard_count, void *user_data)
```

Callback for PgsLeaderboardsClient\_loadLeaderboardMetadata.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `leaderboards` | Pointer to an array of leaderboards, or NULL if status is not PGS\_STATUS\_SUCCESS. | | `leaderboard_count` | The number of leaderboards in the array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_LoadLeaderboardMetadataWithIdCallback

```
void(* PgsLeaderboardsClient_LoadLeaderboardMetadataWithIdCallback)(PgsStatusCode status_code, const PgsLeaderboard *leaderboard, void *user_data)
```

Callback for PgsLeaderboardsClient\_loadLeaderboardMetadataWithId.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `leaderboard` | Pointer to the leaderboard, or NULL if status is not PGS\_STATUS\_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_LoadMoreScoresCallback

```
void(* PgsLeaderboardsClient_LoadMoreScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)
```

Callback for PgsLeaderboardsClient\_loadMoreScores.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `leaderboard_score_buffer` | The leaderboard score buffer, or NULL if status is not PGS\_STATUS\_SUCCESS. The caller must call PgsLeaderboardScoreBuffer\_Release on this object when it is no longer needed. | | `scores` | The leaderboard scores result, or NULL if status is not PGS\_STATUS\_SUCCESS. | | `scores_count` | The number of scores in the array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_LoadPlayerCenteredScoresCallback

```
void(* PgsLeaderboardsClient_LoadPlayerCenteredScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)
```

Callback for PgsLeaderboardsClient\_loadPlayerCenteredScores.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `leaderboard_score_buffer` | The leaderboard score buffer, or NULL if status is not PGS\_STATUS\_SUCCESS. The caller must call PgsLeaderboardScoreBuffer\_Release on this object when it is no longer needed. | | `scores` | The leaderboard scores result, or NULL if status is not PGS\_STATUS\_SUCCESS. | | `scores_count` | The number of scores in the array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_LoadTopScoresCallback

```
void(* PgsLeaderboardsClient_LoadTopScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)
```

Callback for PgsLeaderboardsClient\_loadTopScores.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `scores` | The leaderboard scores result, or NULL if status is not PGS\_STATUS\_SUCCESS. The caller must call PgsLeaderboardScores\_Release on this object when it is no longer needed. | | `leaderboard_score_buffer` | The leaderboard score buffer, or NULL if status is not PGS\_STATUS\_SUCCESS. The caller must call PgsLeaderboardScoreBuffer\_Release on this object when it is no longer needed. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_ShowAllLeaderboardsUICallback

```
void(* PgsLeaderboardsClient_ShowAllLeaderboardsUICallback)(PgsStatusCode status_code, bool success, void *user_data)
```

Callback for PgsLeaderboardsClient\_showAllLeaderboardsUI.

This is invoked after the attempt to load and display the UI.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `success` | True if the UI was successfully launched, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_ShowLeaderboardUICallback

```
void(* PgsLeaderboardsClient_ShowLeaderboardUICallback)(PgsStatusCode status_code, bool success, void *user_data)
```

Callback for PgsLeaderboardsClient\_showLeaderboardUI.

This is invoked after the attempt to load and display the UI.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `success` | True if the UI was successfully launched, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient\_SubmitScoreImmediateCallback

```
void(* PgsLeaderboardsClient_SubmitScoreImmediateCallback)(PgsStatusCode status_code, PgsScoreSubmissionData *score_submission_data, void *user_data)
```

Callback for PgsLeaderboardsClient\_submitScoreImmediate.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `score_submission_data` | The score submission data, or NULL if status is not PGS\_STATUS\_SUCCESS. The caller must call PgsScoreSubmissionData\_Release on the data when it is no longer needed. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

## Functions

### PgsLeaderboardsClient\_loadCurrentPlayerLeaderboardScore

```
void PgsLeaderboardsClient_loadCurrentPlayerLeaderboardScore(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  PgsLeaderboardTimeSpan time_span,
  PgsLeaderboardCollection collection,
  PgsLeaderboardsClient_LoadCurrentPlayerLeaderboardScoreCallback callback,
  void *user_data
)
```

Asynchronously loads the current player's score for a specific leaderboard with time span and collection.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to load score for. | | `time_span` | The time span for the leaderboard. Valid values are `PGS_LEADERBOARD_TIME_SPAN_DAILY`, `PGS_LEADERBOARD_TIME_SPAN_WEEKLY`, or `PGS_LEADERBOARD_TIME_SPAN_ALL_TIME`. | | `collection` | The collection for the leaderboard. Valid values are `PGS_LEADERBOARD_COLLECTION_PUBLIC` or `PGS_LEADERBOARD_COLLECTION_FRIENDS`. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_loadLeaderboardMetadata

```
void PgsLeaderboardsClient_loadLeaderboardMetadata(
  PgsLeaderboardsClient *leaderboards_client,
  bool force_reload,
  PgsLeaderboardsClient_LoadLeaderboardMetadataCallback callback,
  void *user_data
)
```

Asynchronously loads leaderboard metadata.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_loadLeaderboardMetadataWithId

```
void PgsLeaderboardsClient_loadLeaderboardMetadataWithId(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  bool force_reload,
  PgsLeaderboardsClient_LoadLeaderboardMetadataWithIdCallback callback,
  void *user_data
)
```

Asynchronously loads metadata for a specific leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `leaderboard_id` | ID of the leaderboard to load metadata for. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_loadMoreScores

```
void PgsLeaderboardsClient_loadMoreScores(
  PgsLeaderboardsClient *leaderboards_client,
  PgsLeaderboardScoreBuffer *leaderboard_score_buffer,
  int32_t max_results,
  int32_t page_direction,
  PgsLeaderboardsClient_LoadMoreScoresCallback callback,
  void *user_data
)
```

Asynchronously loads more scores for a given leaderboard score buffer.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `leaderboard_score_buffer` | The buffer to load more scores from. This buffer must be obtained from a previous call to loadTopScores or loadPlayerCenteredScores. | | `max_results` | The maximum number of scores to return. | | `page_direction` | The direction to load scores from. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_loadPlayerCenteredScores

```
void PgsLeaderboardsClient_loadPlayerCenteredScores(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  int32_t span,
  int32_t collection,
  int32_t max_results,
  bool force_reload,
  PgsLeaderboardsClient_LoadPlayerCenteredScoresCallback callback,
  void *user_data
)
```

Asynchronously loads player-centered scores for a specific leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to load scores for. | | `span` | The time span for the leaderboard scores. | | `collection` | The score collection for the leaderboard. | | `max_results` | The maximum number of scores to return. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_loadTopScores

```
void PgsLeaderboardsClient_loadTopScores(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  PgsLeaderboardTimeSpan time_span,
  PgsLeaderboardCollection collection,
  int32_t max_results,
  bool force_reload,
  PgsLeaderboardsClient_LoadTopScoresCallback callback,
  void *user_data
)
```

Asynchronously loads top scores for a specific leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to load scores for. | | `time_span` | The time span for the leaderboard scores. | | `collection` | The score collection for the leaderboard. | | `max_results` | The maximum number of scores to return. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_showAllLeaderboardsUI

```
void PgsLeaderboardsClient_showAllLeaderboardsUI(
  PgsLeaderboardsClient *leaderboards_client,
  jobject activity,
  PgsLeaderboardsClient_ShowAllLeaderboardsUICallback callback,
  void *user_data
)
```

Asynchronously loads and displays the standard leaderboards UI.

This function asynchronously loads the necessary components and then presents the leaderboards screen to the player.

The callback is invoked to report the success or failure of the operation to load and display the UI.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `activity` | A JNI reference to the Android Activity to use for launching the new UI. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_showLeaderboardUI

```
void PgsLeaderboardsClient_showLeaderboardUI(
  PgsLeaderboardsClient *leaderboards_client,
  jobject activity,
  const char *leaderboard_id,
  PgsLeaderboardTimeSpan time_span,
  PgsLeaderboardCollection collection,
  PgsLeaderboardsClient_ShowLeaderboardUICallback callback,
  void *user_data
)
```

Asynchronously loads and displays the UI for a specific leaderboard with time span and collection.

This function asynchronously loads the necessary components and then presents the leaderboard screen to the player.

The callback is invoked to report the success or failure of the operation to load and display the UI.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `activity` | A JNI reference to the Android Activity to use for launching the new UI. | | `leaderboard_id` | The ID of the leaderboard to display. | | `time_span` | The time span for the leaderboard. | | `collection` | The collection for the leaderboard. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient\_submitScoreImmediate

```
void PgsLeaderboardsClient_submitScoreImmediate(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  int64_t score,
  const char *score_tag,
  PgsLeaderboardsClient_SubmitScoreImmediateCallback callback,
  void *user_data
)
```

Submits a score to a leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to submit to. | | `score` | The score to submit. | | `score_tag` | An optional score tag. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |
---
title: Play Games Services LeaderboardScore  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard-score
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# Play Games Services LeaderboardScore

Data interface for retrieving leaderboard score information.

## Summary

| Typedefs | |
| --- | --- |
| `PgsLeaderboardScore` | typedef `struct PgsLeaderboardScore`  Represents a single leaderboard score. |

| Functions | |
| --- | --- |
| `PgsLeaderboardScore_Release(PgsLeaderboardScore *leaderboard_score)` | `void`  Releases memory held by [PgsLeaderboardScore](/games/services/cpp/v2/api/struct/pgs-leaderboard-score#struct_pgs_leaderboard_score), including its fields. |

| Structs | |
| --- | --- |
| [PgsLeaderboardScore](/games/services/cpp/v2/api/struct/pgs-leaderboard-score) | Represents a single leaderboard score. |

## Typedefs

### PgsLeaderboardScore

```
struct PgsLeaderboardScore PgsLeaderboardScore
```

Represents a single leaderboard score.

## Functions

### PgsLeaderboardScore\_Release

```
void PgsLeaderboardScore_Release(
  PgsLeaderboardScore *leaderboard_score
)
```

Releases memory held by [PgsLeaderboardScore](/games/services/cpp/v2/api/struct/pgs-leaderboard-score#struct_pgs_leaderboard_score), including its fields.

Details | || Parameters | |  |  | | --- | --- | | `leaderboard_score` | The leaderboard score to release. | |
---
title: Play Games Services Game Stats  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/game-stats
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# Play Games Services Game Stats

Native API for Play Games Services Game Stats.

## Summary

| Functions | |
| --- | --- |
| `PgsGameStatsClient_recordEvent(PgsGameStatsClient *client, PgsPlayerGameEvent *event)` | `void`  Records a single player game event. |
| `PgsGameStatsClient_recordEvents(PgsGameStatsClient *client, const PgsPlayerGameEvent *events, int32_t events_count)` | `void`  Records a list of player game events. |
| `PgsGameStatsClient_requestEventsUpload(PgsGameStatsClient *client)` | `void`  Requests an upload of player game events. |

## Functions

### PgsGameStatsClient\_recordEvent

```
void PgsGameStatsClient_recordEvent(
  PgsGameStatsClient *client,
  PgsPlayerGameEvent *event
)
```

Records a single player game event.

This method operates in a "fire-and-forget" manner. The event is buffered locally for background upload. Note that the event may not be sent to the server until the next scheduled sync. See [PgsGameStatsClient\_requestEventsUpload()](/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57) if you need to trigger an upload of buffered events.

Details | || Parameters | |  |  | | --- | --- | | `client` | The client handle. | | `event` | The player game event to record. | |

### PgsGameStatsClient\_recordEvents

```
void PgsGameStatsClient_recordEvents(
  PgsGameStatsClient *client,
  const PgsPlayerGameEvent *events,
  int32_t events_count
)
```

Records a list of player game events.

This method operates in a "fire-and-forget" manner. The events are buffered locally for background upload. Note that the events may not be sent to the server until the next scheduled sync. See [PgsGameStatsClient\_requestEventsUpload()](/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57) if you need to trigger an upload of buffered events.

Batching events into a list is more efficient than calling [PgsGameStatsClient\_recordEvent()](/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gab0b4cd91ff01afffb822a459fd7aeb26) multiple times in rapid succession.

Details | || Parameters | |  |  | | --- | --- | | `client` | The client handle. | | `events` | An array of player game events to record. | | `events_count` | The number of events in the array. | |

### PgsGameStatsClient\_requestEventsUpload

```
void PgsGameStatsClient_requestEventsUpload(
  PgsGameStatsClient *client
)
```

Requests an upload of player game events.

This method operates in a "fire-and-forget" manner. It requests an asynchronous background upload of all locally buffered events. Locally stored events are cleared upon successful upload.

Details | || Parameters | |  |  | | --- | --- | | `client` | The client handle. | |
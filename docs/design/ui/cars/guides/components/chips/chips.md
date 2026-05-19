---
title: Chip  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/components/chips/chips
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Chip Stay organized with collections Save and categorize content based on your preferences.





**Note:** Chips are only supported in Sectioned Item template in Car App Library version 1.9.

![hero](/static/design/ui/cars/guides/components/chips/chips-assets/image-161-19879.png)

## Overview

Chips are compact, interactive elements that allow users to filter content below them, or trigger quick actions. The compact components help streamline task completion on the road by presenting contextual options relevant to the content and shortening browse time.

To maintain visual clarity, layouts should be limited to a maximum of 7 chips per row. Chips are highly flexible to match your brand's visual language. You can customize the shape, background color, and border color according to the desired UI theme.

**Chips can contain:**

* An icon only
* A text label only
* Both an icon and a label (in either direction)

---

## Composition

![hero](/static/design/ui/cars/guides/components/chips/chips-assets/image-161-21355.png)


*1.* *Leading icon or image*

*2.* *Label text*



---

## UX requirements

To ensure a safe and consistent experience across all apps, follow these design requirements:

| Requirement level | Content |
| --- | --- |
| MUST | Include either an icon or a label. |
| SHOULD | Use a unique visual style, such as a distinct color or shape, to communicate different chip states. |
| SHOULD | Implement consistent styling across all chips throughout your app. |
| SHOULD | Avoid mixing state and stateless chips within the same component group. |
| SHOULD | Position critical or recommended chips at the leading edge of the container. |
| SHOULD | Keep label text brief and descriptive. Avoid long text that trigger truncation and increase cognitive load. |
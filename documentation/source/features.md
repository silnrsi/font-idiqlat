---
title: Idiqlat - Font Features
fontversion: 1.101
---

Idiqlat is an OpenType-enabled font family that supports the East Syriac style of the Syriac script. It includes a number of optional features that may be useful or required for particular uses or languages. This document lists all the available features.

These OpenType features are primarily specified using four-letter tags (e.g. 'cv38'). For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features).

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Idiqlat as a web font see [Idiqlat Webfont Example](../web/Idiqlat-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Character variants

### Kaph alternate

<span class='affects'>Affects: U+071F (this feature is primarily for outlines and only affects the isolate form)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='idiqlat-R normal'>&#x071F;</span> | `cv15=0`
Historic  | <span class='idiqlat-R normal' style='font-feature-settings: "cv15" 1'>&#x071F;</span> | `cv15=1`

### Mim alternate

<span class='affects'>Affects: U+0721 (this feature is primarily for outlines and only affects the isolate form)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='idiqlat-R normal'>&#x0721;</span> | `cv17=0`
Historic  | <span class='idiqlat-R normal' style='font-feature-settings: "cv17" 1'>&#x0721;</span> | `cv17=1`

### Nun alternate

<span class='affects'>Affects: U+0722 (this feature is primarily for outlines and only affects the isolate form)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='idiqlat-R normal'>&#x0722;</span> | `cv18=0`
Historic  | <span class='idiqlat-R normal' style='font-feature-settings: "cv18" 1'>&#x0722;</span> | `cv18=1`

### He Yudh ligature

<span class='affects'>Affects: U+0717 U+071D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='idiqlat-R normal'>&#x0717;&#x071D; &#x200D;&#x0717;&#x071D;</span> | `cv38=0`
Ligature | <span class='idiqlat-R normal' style='font-feature-settings: "cv38" 1'>&#x0717;&#x071D; &#x200D;&#x0717;&#x071D;</span> | `cv38=1`

### Sadhe Nun ligature

<span class='affects'>Affects: U+0728 U+0722</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='idiqlat-R normal'>&#x0728;&#x0722; &#x200D;&#x0728;&#x0722;</span> | `cv55=0`
Ligature | <span class='idiqlat-R normal' style='font-feature-settings: "cv55" 1'>&#x0728;&#x0722; &#x200D;&#x0728;&#x0722;</span> | `cv55=1`

### Taw Alaph ligature

<span class='affects'>Affects: U+072C U+0710</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='idiqlat-R normal'>&#x072C;&#x0710; &#x200D;&#x072C;&#x0710;</span> | `cv59=0`
Triangle    | <span class='idiqlat-R normal' style='font-feature-settings: "cv59" 1'>&#x072C;&#x0710; &#x200D;&#x072C;&#x0710;</span> | `cv59=1`
Intertwined | <span class='idiqlat-R normal' style='font-feature-settings: "cv59" 2'>&#x072C;&#x0710; &#x200D;&#x072C;&#x0710;</span> | `cv59=2`

### Taw Yudh ligature

<span class='affects'>Affects: U+072C U+071D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span dir="rtl" class='idiqlat-R normal'>&#x072C;&#x071D; &#x200D;&#x072C;&#x071D;</span> | `cv60=0`
Ligature | <span dir="rtl" class='idiqlat-R normal' style='font-feature-settings: "cv60" 1'>&#x072C;&#x071D; &#x200D;&#x072C;&#x071D;</span> | `cv60=1`

<!-- PRODUCT SITE ONLY
[font id='idiqlat' face='Idiqlat-Regular' size='150%' rtl=1]
-->

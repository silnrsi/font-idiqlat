---
title: Idiqlat - Frequently Asked Questions
fontversion: 2.200
---

Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](https://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [The SIL Open Font License (OFL-FAQ)](https://openfontlicense.org/ofl-faq/)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.

Here are a few of the most frequently asked questions specifically regarding Idiqlat:

#### *How is this font different from East Syriac Marcus?*

This font was initially based on the design of the Syriac characters in East Syriac Marcus. However, significant design changes have been made in order to modernize and opitimize the font for web and mobile use. 

- The Latin characters were imported from Crimson Pro. 
- Significant design changes have been made in order to modernize and opitimize the font for web and mobile use. 
- The font has been resized in order to match standard point sizes in modern fonts. It also includes Light and ExtraLight weights.
- The default isolate designs of _kaph_, _mim_, and _nun_ have been modified. Since isolate forms for these characters do not exist in modern typefaces, a variety of different designs have been created for the isolate forms. The default forms in this font are the most prevalent, but the original forms from East Syriac Marcus are still available through a Stylistic Set.
- The font has added support for alternates, ligatures, and diacritics that the East Syriac style requires.
- The design of two characters, U+0738 (dotted zlama horizontal) and U+0739 (dotted zlama angular), have been swapped to follow the Unicode Standard design. 
- U+0740 (feminine dot) has been reverted to use the single dot, and U+0324 (diaeresis below) was added to support the double dot below.
- It also supports the Syriac abbreviation mark which is rendered by a line with a dot at each end and in the center.
- This font was updated to use a more modern build system so that it can be easily updated in the future.

#### *Why does the Bold weight look so fuzzy?*

Because Idiqlat is already quite heavy, it does not come with a Bold weight. If you tried to turn on Bold using the application’s UI controls such as a “B” button you will get what is called “fake” Bold. This will not look good. It would be better to choose a lighter weight, to use underlining, or to choose another font in order to show emphasis.

### *I notice that 0866 SYRIAC LETTER MALAYALAM BHA is dual-joining in your font. Whas that intentional?*

Yes, it seems that Garushuni Malayalam does require the _bha_ to be dual-joining. A request has been submitted to Unicode for changing the joining behavior of bha.

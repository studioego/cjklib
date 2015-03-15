# Introduction #

This list tries to give an overview of features supported by cjklib. If you would like to see some examples try [Screenshots](Screenshots.md). See abstract [Goals](Goals.md); a different view on features is given by [WhyUseCjklib](WhyUseCjklib.md).


# Details #

## _Romanisations_/_readings_ ##
  * Break down (_decompose_) strings into single reading entities
  * Join (_compose_) single entities together, apply formatting where needed
  * Handle various decompositions for ambiguous input
  * List of supported reading entities
  * Tonal languages:
    * Combine base syllable with tone and get tone from syllable for tonal languages
    * Choice of diacritics and tone marks, set according to placement rules
  * Reading dialects:
    * Support of various (e.g. non-standard) realisations of a reading (_reading dialect_), e.g. type face variations
    * Guessing of given reading realisation to pinpoint _reading dialect_
    * Conversion of variation to standard form
  * Analysis of syllable forms, e.g breaking into onset and rhyme

  * Conversion between readings:
    * Conversion of strings including non-reading entities
    * Preservation of upper and lower case
    * Support of user-adapted conversion for ambiguous cases
    * Error handling for ambiguous cases/conversion errors
    * Support of non-standard realisations of input reading (_reading dialect_)

### Currently supported readings ###
  * Mandarin Chinese:
    * Pinyin
    * Gwoyeu Romatzyh
    * Wade-Giles
    * IPA
    * Braille
  * Yue (Cantonese):
    * Cantonese Yale
    * Jyutping
    * IPA (work in progress)
  * Wu (Shanghainese):
    * IPA
  * Korean
    * Hangul
  * Japanese
    * Kana (Hiragana & Katakana)

## Character to reading mapping ##
  * Character to reading and reading to character mappings as supported by the Unihan database for Mandarin Chinese, Yue (Cantonese), Wu (Shanghainese) and Korean
  * Support of non-standard realisations of input reading (_reading dialect_)

## Radicals ##
  * Mapping of characters to their Kangxi radical
  * Lookup of radical forms and radical variants
  * Mapping between Unicode radical forms and equivalent characters
  * Multi-radical search (see character components)

## Variants ##
  * Variant information as given by the Unihan database:
    * Compatible character forms
    * Semantic variant forms, often used interchangeably
    * Specialised semantic variant forms, often used interchangeably but limited to certain contexts
    * Z-variant forms, which only differ in typeface
    * Simplified Chinese character forms, originating from the character simplification process of the PR China
    * Traditional character forms for a simplified Chinese character
  * Database of character variants for components and stroke decomposition on a glyph basis (see below)
  * Default mapping of glyph form for locale

## Character components ##
  * Decomposition of characters into components
  * Component tree with structural information
  * Component search with equivalent forms

## Strokes ##
  * Glyph dependant stroke count
  * Unicode stroke forms
  * Stroke order of characters
  * Abbreviated ASCII names for strokes

## Data ##
The library comes with its own set of sources on:
  * Pinyin syllables
  * Gwoyeu Romatzyh syllables including rhotacised forms and abbreviations
  * Wade-Giles syllables
  * Jyutping syllables
  * Cantonese Yale syllables
  * Pinyin to Gwoyeu Romatzyh mapping
  * Wade-Giles to Pinyin mapping
  * Pinyin to IPA mapping
  * Pinyin to Braille mapping
  * Jyutping to Cantonese Yale mapping
  * Jyutping to IPA mapping
  * Shanghainese (IPA) syllables
  * mapping of characters to Shanghainese pronunciation
  * mapping of Mandarin syllables to onset and rhyme
  * mapping of Cantonese syllables to onset and rhyme
  * Kangxi radical forms
  * stroke count and stroke order
  * stroke names
  * character decomposition

See the data files for comparison with other sources.

This project makes use of the Unicode Han database provided by the Unicode Consortium: Unicode Standard Annex #38 - Unicode Han database (Unihan): http://www.unicode.org/reports/tr38/, 28.03.2008.

The following data is used:
  * Character Kangxi radical information (from kRSKangxi)
  * Radical residual stroke count (from kRSKangxi) and total stroke count (from KTotalStrokes)
  * Mandarin character readings in Pinyin (from kHanyuPinlu, kXHC1983, kHanyuPinyin)
  * Cantonese character readings in Jyutping (from kCantonese)
  * Korean character readings in Hangul (from kHangul)
  * Character variant forms (from kCompatibilityVariant, kSemanticVariant, kSimplifiedVariant, kSpecializedSemanticVariant, kTraditionalVariant, kZVariant)

This includes dictionary data from:
  * kXHC1983: Xiàndài Hànyǔ Cídiǎn (现代汉语词典). Shāngwù Yìnshūguǎn, Beijing,
  * kHanyuPinlu: Xiàndài Hànyǔ Pínlǜ Cídiǎn (現代漢語頻率詞典). 北京語言學院語言教學研究所編著, First edition 1986/6, 2nd printing 1990/4, ISBN 7-5619-0094-5.
  * kHanyuPinyin: Hànyǔ Dà Zìdiǎn (漢語大字典). 許力以主任，徐中舒主編，（漢語大字典工作委員會）。 武漢：四川辭書出版社，湖北辭書出版社, 1986-1990. ISBN: 7-5403-0030-2/H.16.

## Build system ##
A dependancy based, modular build system is supplied for creating the library's database from packaged data files and from [Unicode's Unihan](http://unicode.org/charts/unihan.html) database or [Kanjidic2](http://www.csse.monash.edu.au/~jwb/kanjidic2/). Additionally Unihan's data can be overloaded by more precise data if available.

## Dictionaries ##
Support for [EDICT](http://www.csse.monash.edu.au/~jwb/j_edict.html), [CEDICT](http://www.mdbg.net/chindict/chindict.php?page=cedict), the [Gwoyeu Romatzyh Version of CEDICT](http://home.iprimus.com.au/richwarm/gr/gr.htm#grdict) (called CEDICTGR here), [HanDeDict](http://www.chinaboard.de/chinesisch_deutsch.php) and [CFDICT](http://www.chinaboard.de/cfdict.php) with full-text search included for command-line tool _cjknife_.
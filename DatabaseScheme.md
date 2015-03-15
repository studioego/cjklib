# Introduction #

This list serves as a (partial) reference to the database scheme listing tables used in the library.

# Details #

  * KangxiRadical
> All radicals from the traditional Kangxi radical index using 214 radical forms, grouped by locale.
```
  CREATE TABLE KangxiRadical (
    RadicalIndex INTEGER NOT NULL,            -- Radical index
    Form CHAR(1) PRIMARY KEY,                 -- Radical character
    Type CHAR(1) NOT NULL,                    -- Type, (R) radical, (V) variant
    Locale VARCHAR(6) NOT NULL DEFAULT '',    -- Locale (T) traditional,
                                              --  (C) simplified Chinese,
                                              --  (J) Japanese,
                                              --  (K) Korean, (V) Vietnamese
    SubIndex INTEGER NOT NULL DEFAULT 0,      -- additional index for uniqueness
    UNIQUE (RadicalIndex, Type, SubIndex)
  );
```
> Example:
```
  select * from KangxiRadical limit 5;
  1|⼀|R|TCJKV|0
  2|⼁|R|TCJKV|0
  3|⼂|R|TCJKV|0
  4|⼃|R|TCJKV|0
  5|⼄|R|TCJKV|0
```
  * RadicalEquivalentCharacter
> Mapping of Unicode radical forms to characters ("ideographs").
```
  CREATE TABLE RadicalEquivalentCharacter (
    Form CHAR(1) NOT NULL,                    -- Radical character
    EquivalentForm CHAR(1) NOT NULL,          -- Radical equivalent character
    Locale VARCHAR(6) NOT NULL DEFAULT '',    -- Locale for mapping of forms
                                              --  (T) traditional,
                                              --  (C) simplified Chinese,
                                              --  (J) Japanese,
                                              --  (K) Korean, (V) Vietnamese
    PRIMARY KEY (Form, Locale),
    UNIQUE (Form, EquivalentForm)
  );
```
> Example:
```
  select * from RadicalEquivalentCharacter limit 5 offset 272;
  ⺁|厂|TCJKV
  ⺂|乛|TCJKV
  ⺄|乙|TCJKV
  ⺆|冂|TCJKV
  ⺇|几|TCJKV
```
  * CharacterKangxiRadical
> Mapping of characters to their Kangxi radical (as defined in Unihan).
```
  CREATE TABLE CharacterKangxiRadical (
    ChineseCharacter      VARCHAR(1) NOT NULL,
    RadicalIndex  INTEGER NOT NULL,
    PRIMARY KEY(ChineseCharacter, RadicalIndex)
  );
```
> Example:
```
  select * from CharacterKangxiRadical limit 5 offset 188;
  亸|30
  亹|8
  人|9
  亻|9
  亼|9
```
  * CharacterResidualStrokeCount
> Mapping of characters to their residual stroke count, i.e. the stroke count minus the stroke count of the radical form.
```
  CREATE TABLE CharacterResidualStrokeCount (
    ChineseCharacter      VARCHAR(1) NOT NULL,
    ZVariant      INTEGER NOT NULL,
    RadicalIndex  INTEGER NOT NULL,
    ResidualStrokeCount   INTEGER DEFAULT NULL,
    PRIMARY KEY(ChineseCharacter, ZVariant, RadicalIndex)
  );
```
> Example:
```
  select * from CharacterResidualStrokeCount limit 5;
  堂|0|32|8
  堂|0|42|8
  沉|0|16|5
  沉|0|85|4
  沉|0|14|5
```
  * CharacterDecomposition
> Decomposition of glyphs into components.
```
  CREATE TABLE CharacterDecomposition (
    ChineseCharacter CHAR(1) NOT NULL,        -- Chinese character (includes
                                              --   radical forms)
    Decomposition VARCHAR(50) NOT NULL,       -- Decomposition into sub parts
    ZVariant INTEGER NOT NULL DEFAULT 0,      -- Z-variant of character
    SubIndex INTEGER NOT NULL DEFAULT 0,      -- additional index for uniqueness
    Flags VARCHAR(5) DEFAULT '',              -- Flags, (O) checked, (S) variant
                                              --   found only as sub part
    PRIMARY KEY (ChineseCharacter, ZVariant, SubIndex)
  );
```
> Example:
```
  select * from CharacterDecomposition limit 5;
  ⾌|⿱⺊⿸？七|0|0|O
  ⾊|⿱⺈巴|0|0|O
  ⽳|⿱丶⺳|0|1|O
  ⽞|⿱亠幺|0|0|O
  ⾇|⿰夕？|0|0|O
```
  * ComponentLookup
> Lookup of glyphs by their component.
```
  CREATE TABLE ComponentLookup (
    ChineseCharacter      VARCHAR(1) NOT NULL,
    ZVariant      INTEGER NOT NULL,
    Component     VARCHAR(1) NOT NULL,
    ComponentZVariant     INTEGER NOT NULL,
    PRIMARY KEY(ChineseCharacter, ZVariant, Component, ComponentZVariant)
  );
```
> Example:
```
  select * from ComponentLookup limit 5;
  示|0|小|0
  示|0|二|0
  堂|0|尚|1
  堂|0|土|0
  堂|0|口|0
```
  * StrokeCount
> Stroke count of glyphs.
```
  CREATE TABLE StrokeCount (
    ChineseCharacter      VARCHAR(1) NOT NULL,
    StrokeCount   INTEGER DEFAULT NULL,
    ZVariant      INTEGER NOT NULL,
    PRIMARY KEY(ChineseCharacter, ZVariant)
  );
```
> Example:
```
  select * from StrokeCount limit 5;
  嶦|16|0
  墰|15|0
  䒉|20|0
  䭮|19|0
  揊|12|0
```
  * StrokeOrder
> Stroke order of gylphs on a purely name basis.
```
  CREATE TABLE StrokeOrder (
    ChineseCharacter CHAR(1) NOT NULL,        -- Chinese character (includes
                                              -- radical forms)
    StrokeOrder VARCHAR(50) NOT NULL,         -- Stroke order, strokes abbreviated
    ZVariant INTEGER NOT NULL DEFAULT 0,      -- Z-variant of character
    Flags VARCHAR(5) DEFAULT '',              -- Flags, (O) checked, (S) variant
                                              --  found only as sub part
    PRIMARY KEY (ChineseCharacter, ZVariant)
  );
```
> Example:
```
  select * from StrokeOrder limit 5;
  ⻏|HP-WG-S|0|
  ⻏|HPWG-S|1|
  ⻝|SP-N-D-HZ-H-H-ST-P-D|1|
  ⻝|SP-N-D-HZ-H-H-ST-P-N|0|
  ⾷|SP-N-D-HZ-H-H-ST-P-D|1|
```
  * Strokes
> List of strokes as decoded in Unicode with name.
```
  CREATE TABLE Strokes (
    StrokeAbbrev VARCHAR(10) PRIMARY KEY, -- Abbreviated stroke name
    Name VARCHAR(20) UNIQUE,              -- Chinese stroke name
    Stroke VARCHAR(3) NOT NULL            -- Stroke char or placeholder
  );
```
> Example:
```
  select * from Strokes limit 5;
  T|提|㇀
  WG|彎鉤|㇁
  WSG|彎豎鉤|㇁
  XG|斜鉤|㇂
  NG|捺鉤|㇂
```
  * CharacterVariant
> Mapping to character variant forms, e.g. Chinese simplfied to traditional.
```
  CREATE TABLE CharacterVariant (
    ChineseCharacter      VARCHAR(1) NOT NULL,
    Variant       VARCHAR(1) NOT NULL,
    Type  CHAR NOT NULL,
    PRIMARY KEY(ChineseCharacter, Variant, Type)
  );
```
> Example:
```
  select * from CharacterVariant limit 5;
  㐀|丘|M
  㐅|五|M
  㐫|凶|M
  㐮|襄|M
  㐯|庸|M
```
  * GB2312Set
> List of characters included in the gb2312 encoding.
```
  CREATE TABLE GB2312Set (
    ChineseCharacter      VARCHAR(1) NOT NULL,
    PRIMARY KEY(ChineseCharacter)
  );
```
> Example:
```
  select * from GB2312Set limit 5;
  一
  丁
  七
  万
  丈
```
  * CharacterPinyin
> Mapping of characters to pronunciation in Pinyin.
```
  CREATE TABLE CharacterPinyin (
    ChineseCharacter      VARCHAR(1) NOT NULL,
    Reading       VARCHAR(255) NOT NULL,
    PRIMARY KEY(ChineseCharacter, Reading)
  );
```
> Example:
```
  select * from CharacterPinyin limit 5;
  㐀|qiu1
  㐁|tian3
  㐁|tian4
  㐄|kua4
  㐅|wu3
```
  * PinyinInitialFinal
> Mapping of Pinyin syllables into initial and final.
```
  CREATE TABLE PinyinInitialFinal (
    Pinyin VARCHAR(7) PRIMARY KEY,    -- syllable in IPA
    PinyinInitial VARCHAR(2),         -- syllable initial in IPA
    PinyinFinal VARCHAR(5),           -- syllable final in IPA
    UNIQUE (PinyinInitial, PinyinFinal)
  );
```
> Example:
```
  select * from PinyinInitialFinal limit 5 offset 55;
  bing|b|ing
  bu|b|u
  pa|p|a
  po|p|o
  pai|p|ai
```
  * PinyinSyllables
> Full list of Pinyin syllables.
```
  CREATE TABLE PinyinSyllables (
    Pinyin VARCHAR(7) PRIMARY KEY,    -- Pinyin syllable
    Source VARCHAR(1)                 -- Source of syllable: (I) for ISO 7098:1991
  );
```
> Example:
```
  select * from PinyinSyllables limit 5;
  a|I
  ai|I
  an|I
  ang|I
  ao|I
```
  * JyutpingYaleMapping
> Mapping of syllables from LSHK's Jyutping to the Cantonese Yale romanisation.
```
  CREATE TABLE JyutpingYaleMapping (
    Jyutping VARCHAR(6) UNIQUE,       -- Jyutping syllable
    CantoneseYale VARCHAR(6) UNIQUE   -- Cantonese Yale syllable
  );
```
> Example:
```
  sqlite> select * from JyutpingYaleMapping limit 5;
  aa|a
  aai|aai
  aak|aak
  aam|aam
  aan|aan
```
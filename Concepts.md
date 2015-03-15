# Introduction #

Cjklib employs some concepts important to understand which should be described here in addition to the information given in the [API](http://www.stud.uni-karlsruhe.de/~uyhc/api/index.html).


# Details #

## Glyphs ##

Chinese characters, as a result of their development in history, nowadays quite often have several different appearances. These can be either simple changes in single strokes but can also go as far as changes in stroke count and visual components. This leads to the concept of _Glyphs_.

_Glyphs_ are the visual renderings of abstract characters as encoded by Unicode and these two classes should be well differentiated.

When the task of encoding the Han characters was started a decision was made that characters would be encoded independently of their variational appearance as in concordance with the general encoding rules. Under the name _Han unification_ characters shapes were analysed and characters having only variation on the z-Axis of Unicode's 3-dimensional character model have been merged (the only exceptions being characters already encoded with different renderings in well known encodings thus being retained under the name z-Variants). On a side note: the criticism this decision for unification created shows how important the concrete visual appearance is for these characters.

With z-Variants being the only exception of the encoding process of abstract forms, Unicode only gives a referential representation of their encoded characters. There is a need of a conceptual visualisation layer before statements with regards to the visual appearance can be made, for example as for actual stroke count, visual character components or stroke order. Cjklib incorporates a glyph dependant system and means to build upon the abstract data provided by Unicode. Methods being dependant on the visual appearance thus need to be given an actual glyph. See _character locales_ for an easy method extending the glyph concept.

## Character Locales ##

As already said above Chinese characters nowadays have quite often different appearances and in particular vary between the societies employing these in their writing system. Additionally to the change in shape special radical forms can be found in some societies, owing to the fundamental change of many characters.

_Character locales_, mostly abbreviated _locales_, define the language environment with regard to functions which operate on Chinese characters. They abstract the places of usage and there exist five locales: traditional writing of characters still found on Taiwan abbreviated with **T**, simplified Chinese as found in the People's Republic and Singapore abbreviated with **C**, simplified Japanese as written in Japan and abbreviated with **J**, Korean as found on the Korean peninsular (nowadays rather limited to South Korea) abbreviated with **K** and finally Vietnamese for Vietnam abbreviated with **V**.

The concept of _locales_ builds on that of _glyphs_ as that each locale in principal gets a default glyph assigned. In reality there are often several glyphs to be found in parallel but it is not in the scope of this project to grasp all of these possibilities, needless to say that such a database would only be targeted at a much smaller audience.

While conceptual already implemented mappings at this development stage still need to be done on a large basis.

## Readings ##

Pronunciations of Characters vary between the languages and their as for their written form even within a language between different writing/transcription systems. This variation is abstracted using the concept of _readings_ and a hierarchy of classes offer a way of dealing with the various characteristics of each language and written form. A big class of readings are romanisations, but there are unique ones like Hangul for Korean or the general International Phonetic Alphabet (IPA).

As many readings vary in their written application, even if standardised, cjklib additionally provides handling of those, called _reading dialects_.
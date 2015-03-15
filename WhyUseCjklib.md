# Introduction #

This list tries to name some arguments why you should use cjklib. There are also abstract [Goals](Goals.md) defined and concrete [Features](Features.md) given.


# Details #

Cjklib is for you if you develop solutions handling Hanzi, Kanji, Hanja and romanisations Pinyin, Wade-Giles, Jyutping, Yale or even Braille (to name only some) and are looking for a clean, easy, yet flexible system providing you with the fundamental functions.

Cjklib
  * **hides complexity** where appropriate,
> > get a stroke count of your character and don't bother finding the correct glyph used in your target locale,
  * gives you **flexibility** if you need something special,
> > tell the Pinyin operator to be strict if you want to, but by default faulty input will be tolerated,
  * offers **good defaults**,
> > Cantonese Yale will fall back to the first level tone if unclear, as it's preferred usage is reported in literature,
  * provides **reliability** using a growing set of test cases,
  * **abstracts** from the language, romanisation, locale used (port your application easily),
  * **informs** with an API full of documentation and examples.

Go to [QuickStart](QuickStart.md) and try it out.
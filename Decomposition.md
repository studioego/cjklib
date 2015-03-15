# Introduction #

Decomposing a Han character will give a tree of component characters. These components can have components themselves.

It is obvious that decomposition data should be valid and complete, but it is difficult to define what makes such a decomposition valid. There are several ways to look at character decomposition and this probably influences the way we think about correctness.

This page shall offer questions and hints to help realize what decomposition needs to achieve. Log in and help contribute to guidelines! It's ok, if you don't keep it as clean as it is now :)

# Questions & Issues #

Where is character decomposition needed?
  * Lookup, aka. multi-radical search ([example](http://jisho.org/kanji/radicals/))
  * Visualisation, learn character by components ([example](http://www.yellowbridge.com/chinese/character-etymology.php?searchChinese=1&zi=或))
  * Phonetic analysis, collect information about phonetic components
  * Model generation, generate handwriting models from components ([example](http://cburgmer.nfshost.com/content/bootstrapping-tegaki-handwriting-models-using-character-decomposition))

What kind of different decomposition can exist?
  * Visual decomposition, including all well-known characters
  * Ethymological decomposition, use the actual components as used in history
  * Including Kangxi radical (might not generally overlap with visual and ethymological)

What else needs to be considered?
  * Are there different grades in decomposition? People might disagree on what is a component and this disagreement can possibly be expressed in a degree of validity. Some might argue components need to be separated by a "void", as to clearly cut through a character. For them 龙 might not be expressed as ⿻尤？ (the question mark denoting a missing character to express that component). A degree might express how well a decomposition seems fitting: 1=can be cut through into two clear components, 2=overlap, but both character exist in their own right, 3=one component clearly is a character.
  * Can non-Han characters serve as components? If not, why?
  * What code point to use for "characters" that got encoded in different places, e.g. radical form vs. unified character
  * Are in-frequent characters outside the [BMP](http://en.wikipedia.org/wiki/Basic_Multilingual_Plane#Basic_Multilingual_Plane) useful?
  * What to do with frequent components that didn't get encoded with Unicode?
  * Should components be mapped to a similar character or the ethymological character with a different visual representation if no exact character exists?
  * What about component structures not recognized by Unicode (IDS), e.g. 众?
    * http://linguistics.berkeley.edu/~rscook/pdf/UniProp-Final/02221-n2480.pdf
  * http://appsrv.cse.cuhk.edu.hk/~irg/irg/irg28/IRGN1298_IDS_check_result.doc

# Current Organisation #

## Glyphs ##
Currently every character can have as many decompositions as possible. Actually each character can have as many glyphs as possible of which each locale has one set as default and each glyph can have as many decompositions as possible. Each needs to result in the same stroke order for every glyph.

Each glyph is a particular graphical representation, of which most characters luckily should have only few if not just one.

As components have glyphs again each decomposition matches to a character's glyph, not the character itself. This is important as character can change appearance, e.g. ⾷ will have a dot as last stroke if used as radical on the left side, not a right falling one. In the latter case a decomposition can look like `"枚","⿰木[1]攵",0,1,O`. The first component 木 "tree" is mapped to the glyph no. 1 (2nd glyph), which then should have a dot as last character in the StrokeOrder mapping.
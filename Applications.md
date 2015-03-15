# Introduction #

To help you understand where something like cjklib would be useful, here are a few existing applications. Also given are example applications envisioned by the developers during the creation process.

# Applications #

**Dictionary programs**

  * [Eclectus](http://code.google.com/p/eclectus/), a small Han character dictionary for learners.
  * [Pinyin Toolkit](http://wiki.github.com/batterseapower/pinyin-toolkit), a plugin for the Anki Spaced Repetition System (http://ichi2.net/anki/)

**Useage of character decomposition:**

  * [Tegaki](http://www.tegaki.org) handwriting recognition uses cjklib to bootstrap handwriting models for Traditional Chinese based on models from character components.

**Something having to do with stroke order:**

  * [Single stroke recognition with Tegaki](http://github.com/cburgmer/hwr/commits/strokes): using stroke order data, stroke handwriting models can be created from existing character data.
  * IMEs (Input method editor) like ibus and SCIM can use stroke order data to provide a stroke order input similar to mobile phones.

**Consistence checks of dictionary**

Use Pinyin romanization handling and data from Unicode's Unihan to crosscheck CEDICT and HanDeDict's entries. Example script: [trunk/examples/checkcedict.py](http://code.google.com/p/cjklib/source/browse/trunk/examples/checkcedict.py), list of possibly wrong entries: http://cburgmer.nfshost.com/content/consistency-check-cedict-unihan-pinyin-pronunciations


# Introduction #

_Cjklib_ was started as to increase the support for languages with Chinese character based writing systems on the software side. This goal comes with several others that should be listed here.

# Details #

  * **Scope**: _cjklib_ provides methods for CJKV languages and their writing systems. Using a three element view on the context of a Chinese character, this project includes methods coping with the _pronunciation_ and _visualisation_ of Chinese characters while ignoring their semantics. The latter is in particular done by abstracting character's visual forms as glyphs instead of relying on a single representation.
  * **Everything under one hood**: for all methods, languages (and writing systems) supported are provided together under one hood, being as independant as possible from the particular language, but without losing the flexibility of the aspects covered.
  * **High quality and transparancy**: projects depending on _cjklib_ should be able to build and trust on the services provided. Throughout the library implementation and data sources are backed up by linguistic literature and implementational shortcomings are to be marked as such.
  * **Easy yet powerful**: _cjklib_ tries to be as easy as possible allowing for simple integration and quick results while providing all the necessary functionality and possibilies needed.
  * **Exact**: language quite often becomes vague and fuzzy. Methods to be implemented though should give one definitive answer for each request - tasks with fuzzy knowledge highly depend on the use case and are thus left to the user.
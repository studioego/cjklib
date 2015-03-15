Cjklib provides language routines related to Han characters (characters based on Chinese characters named Hanzi, Kanji, Hanja and chu Han respectively) used in writing of the Chinese, the Japanese, infrequently the Korean and formerly the Vietnamese language(s). Functionality is included for character pronunciations, radicals, glyph components, stroke decomposition and variant information. Cjklib is implemented in Python.

Documentation is hosted on http://cjklib.org. See also [Features](Features.md) and [Screenshots](Screenshots.md) for examples. [QuickStart](QuickStart.md) gives a 3-step guide on installing. Read on with [WhyUseCjklib](WhyUseCjklib.md).

## Examples ##
  * Get characters by pronunciation (here: "국" in Korean):
```
>>> from cjklib import characterlookup
>>> cjk = characterlookup.CharacterLookup('T')
>>> cjk.getCharactersForReading(u'국', 'Hangul')
[u'匊', u'國', u'局', u'掬', u'菊', u'跼', u'鞠', u'鞫', u'麯', u'麴']
```
  * Get characters by components (yielding glyphs):
```
>>> cjk.getCharactersForComponents([u'门', u'⼉'])
[(u'阅', 0), (u'阋', 0)]
```
  * Get stroke order of characters:
```
>>> cjk.getStrokeOrder(u'说')
[u'㇔', u'㇊', u'㇔', u'㇒', u'㇑', u'㇕', u'㇐', u'㇓', u'㇟']
```
  * Convert pronunciation data (here from Pinyin to IPA):
```
>>> from cjklib.reading import ReadingFactory
>>> f = ReadingFactory()
>>> f.convert(u'lǎoshī', 'Pinyin', 'MandarinIPA')
u'lau˨˩.ʂʅ˥˥'
```
  * Access a dictionary (here using Jim Breen's EDICT):
```
>>> from cjklib.dictionary import EDICT
>>> d = EDICT()
>>> d.getForTranslation('Tokyo')
[EntryTuple(Headword=u'東京', Reading=u'とうきょう', Translation=u'/(n) Tokyo (current capital of Japan)/(P)/')]
```
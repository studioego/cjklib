# Introduction #

Most products come with a "screenshot" section, showing functionality or the look and feel  of the application. As cjklib is a library this pages should focus on the former one. The command-line script ''cjknife'' gives quick access to most of the functions, so it shall be used here.


# Details #

### Supplying character-based information ###
Get character information including:
  * Kangxi radical information
  * Stroke count
  * Character reading
  * Encoded character variants
  * Glyphs overview
  * Character decomposition

```
$ cjknife -i 周
Information for character 周 (traditional locale, Unicode domain)
Unicode codepoint: U+5468 (21608, character form)
In character domains: Unicode, BIG5, JISX0208, GlyphInformation, JISX0208_0213, GB2312, BIG5HKSCS, IICore
Radical index: 30, radical form: ⼝
Stroke count: 8
Phonetic data (CantoneseYale): jāu
Phonetic data (GR): jou
Phonetic data (Hangul): 주
Phonetic data (Jyutping): zau1
Phonetic data (MandarinBraille): ⠌⠷⠁
Phonetic data (MandarinIPA): tʂou˥˥
Phonetic data (Pinyin): zhōu
Phonetic data (ShanghaineseIPA): ʦɤ˥˧
Phonetic data (WadeGiles): chou1
Semantic variants: 週
Glyph 0(*), stroke count: 8
⿵⺆⿱土口
Stroke order: ㇓㇆㇐㇑㇐㇑㇕㇐ (SP-HZG H-S-H S-HZ-H)
```


### Looking up characters by reading ###
Get a list of homophon characters with the given reading:
```
$ cjknife -s Hangul -a 국
匊國局掬菊跼鞠鞫麯麴
```


### Get reading of characters ###
```
$ cjknife -t Hangul -r 漢字
한 자
```

Get readings for characters with several pronunciations (多音字):
```
$ cjknife -t Pinyin -r 漢字
[hàn tān] [zì zi]
```


### Convert between traditional and simplified forms ###
```
$ cjknife -f 漢字
Chinese simplified: 汉字
Traditional: 漢字
```


### Get characters by Kangxi radical ###
```
$ cjknife -k 7
+0: 二                                                                   
+1: 亐亍亏于                                                             
+2: 云亓互井五亖                                                         
+3: 亗                                                                   
+4: 亙亘                                                                 
+5: 亜                                                                   
+6: 些亝亟亞                                                             
```


### Limit results to a given character domain ###
```
$ cjknife -d BIG5 -k 7
+0: 二
+1: 亍于
+2: 云亓互井五
+4: 亙
+6: 些亟亞
```


### Get characters by components ###
Get a list of characters including all the given characters:
```
$ cjknife -p 口土
吐呿咥哇垕㖏㙂㙅唑唗唟㖫哩啀啈啩㖶㗌䞤亴喔喹堡臵超㙜䞦䞧䞩喱嗑塣趌㗧䞫嘊嘡塾臺趗
㙮䞳䞸嘢嘵墪趟㘁㙱㙳㙵㯧儓噇噻趦㘆㸀兣嬯懛擡薹䠟嚜嚡檯趫穯籉趮囈
```


### Convert readings ###
Converting from tones given by numbers to standard form with diacritics:
```
$ cjknife -s CantoneseYale -t CantoneseYale -m gwong2dung1wa2
gwóngdūngwá
```

Convert between romanisations:
```
$ cjknife -s Pinyin -t GR -m Guo2yu3
Gwoyeu
```

Get pronunciation in IPA (considering basic tonal changes):
```
$ cjknife -s Pinyin -t MandarinIPA -m lao3shi1
lau˨˩.ʂʅ˥˥
```


### Dictionary lookup ###
_The following extracts are taken from [EDICT](http://www.csse.monash.edu.au/~jwb/j_edict.html) and [CC-CEDICT](http://www.mdbg.net/chindict/chindict.php?page=cedict) licensed under the Creative Commons Attribution-Share Alike 3.0 License._

Looking for an exact English term:
```
$ cjknife -w EDICT -x "Tokyo"
東京 とうきょう /(n) Tokyo (current capital of Japan)/(P)/
```

Looking for exact matches to a given reading:
```
$ cjknife -w CEDICT -x "zhishi"
知識, zhī shi, /intellectual/knowledge-related/knowledge/
執事, zhí shì, /deacon/
只是, zhǐ shì, /merely/simply/only/but/
指事, zhǐ shì, /ideogram (one of the Six Methods 六書|六书 of forming Chinese ch
aracters)/Chinese character indicating an idea, such as up and down/also known a
s self-explanatory character/
指示, zhǐ shì, /to point out/to indicate/(give) directives or instructions/
致使, zhì shǐ, /cause/result in/
制式, zhì shì, /standard (format, e.g. PAL or SECAM for TV signal)/system/servic
e pattern/type of service/
```

Wildcards:
```
$ cjknife -w EDICT -x "東京_"
東京語 とうきょうご /(n) Tokyo dialect (esp. historical)/
東京着 とうきょうちゃく /(n) arriving in Tokyo/
東京都 とうきょうと /(n) Tokyo Metropolitan area/
東京発 とうきょうはつ /(n) departing Tokyo/
東京湾 とうきょうわん /(n) Tokyo Bay/Bay of Tokyo/
```
```
$ cjknife -w CEDICT -x %漢字%
漢字, Hàn zì, /Chinese character, kanji/
漢字查字法, Hàn zì chá zì fǎ, /look-up method for Chinese characters/
漢字輸入, Hàn zì shū rù, /Chinese character input/method for typing Chinese/
漢字輸入系統, Hàn zì shū rù xì tǒng, /Chinese character input system/
漢字字體, Hàn zì zì tǐ, /calligraphic style of Chinese characters/typeface/font/
統漢字, tǒng Hàn zì, /Unihan/CJK unified ideographs/
```

Mixing headword and reading:
```
$ cjknife -w CEDICT -x "中國hua"
中國化（中国化） Zhōng guó huà /to Sinicize/to take on Chinese characteristics/
中國畫（中国画） Zhōng guó huà /Chinese painting/
中國話（中国话） Zhōng guó huà /(spoken) Chinese language/
```
# Introduction #

I've been making some additions to cjklib data tables recently, and encountered some cases which I'd like to raise a discussion of, before performing a wide-scale change.


# Details #

Perhaps an example would be best:

月 is listed as a component in many characters, such as 明，肖，能，胃. However, in all but the first of these, the first stroke is shown by most fonts as S rather than SP, requiring a glyph variant. But the character etymologies (according to www.zhongwen.com) as well as the Unicode code charts actually suggest a graphical variant of 肉 rather than 月.

And now that I've checked more thoroughly, it appears that in fact the majority of characters which appear to have 月 on the left (such as 腦) actually have 肉... And indeed look different in the T locale, having ⺼ (U+2EBC) on the left. They also have it on the bottom in characters such as 肖.

Therefore, I'd suggest using ⺼ (U+2EBC) rather than 月 for characters classified under the 肉 radical, and to specify locale-dependent stroke orders for this component. It appears two glyph variants will be needed:
  * 0 "SP-HZG-H-H" / "SP-HZG D T" for a left component as in 腦.
  * 1 "S-HZG-H-H"  / "SP-HZG D T" for a bottom one as in 肖.
The second stroke order (identical for both) is for T locale, the first order for all others. Glyph 0 is the most common.

It might also be possible to use locale-specific decompositions, and employ 月，⺼ and ⺝ (U+2E9D) as necessary according to graphical appearance, but this IMHO would lead to much unnecessary data duplication.
# Introduction #

The [API](http://cburgmer.nfshost.com/cjklib) already includes a [list of Todos](http://cburgmer.nfshost.com/cjklib/current/todo-index.html) marked with the place where actions needs to be taken. This page in contrast is meant to give a broader overview on things that still need to be done.


# Details #

  * Character decomposition:
> > The given set needs to be reviewed and rules for decomposition to be set up.
  * Stroke order:
> > A rather tedious bit of work includes creating entries for the stroke order of characters in naming the strokes found in particular in each character. This list is combined with the character decomposition and thus far fewer characters actually need an entry. In return more acurate stroke count entries can be generated.
  * Mapping to glyph images:
> > Both stroke order and character decomposition should be mapped to actual graphical representations so that a reference is given for all entries. Sources for reference also need to be discussed.
    * [Ideographic Variation Database](http://unicode.org/reports/tr37/)
  * Mapping to locales:
> > Each character can have a distinct glyph mapped to one of the locales (traditional, Chinese simplified, Japanese simplified, Korean and Vietnamese). This should be done given a valid source.
  * Readings:
> > A lot of standard readings/romanisations are still not implemented, especially for Japanese and Vietnamese.
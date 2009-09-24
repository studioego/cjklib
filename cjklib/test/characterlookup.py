#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file is part of cjklib.
#
# cjklib is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cjklib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cjklib.  If not, see <http://www.gnu.org/licenses/>.

"""
Provides the library's unit tests for L{characterlookup.CharacterLookup}.
"""

# pylint: disable-msg=E1101
#  testcase attributes and methods are only available in concrete classes

import re
import unittest

from cjklib.reading import ReadingFactory
from cjklib import characterlookup
from cjklib import exception
from cjklib.test import NeedsDatabaseTest, attr

class CharacterLookupTest(NeedsDatabaseTest):
    """Base class for testing the L{characterlookup.CharacterLookup} class."""
    class CacheDict(dict):
        def __init__(self, cachedDict, *args, **options):
            dict.__init__(self, *args, **options)
            self.cachedDict = cachedDict
        def __getitem__(self, key):
            try:
                return dict.__getitem__(self, key)
            except KeyError:
                return self.cachedDict.__getitem__(key)

    class DatabaseConnectorMock(object):
        """
        Serves as a normal database connector engine, but fakes existance of
        some tables.
        """
        def __init__(self, dbConnectInst, mockTables=None,
            mockTableDefinition=None, mockNonTables=None):

            self._dbConnectInst = dbConnectInst
            self._dbConnectInst.engine = CharacterLookupTest.EngineMock(
                self._dbConnectInst.engine, mockTables, mockNonTables)

            self.mockTables = mockTables or []
            self.mockTableDefinition = mockTableDefinition or {}

        def __getattr__(self, attr):
            if attr == 'tables':
                return CharacterLookupTest.CacheDict(
                    self.mockTableDefinition, self._dbConnectInst.tables)
            return getattr(self._dbConnectInst, attr)

    class EngineMock(object):
        """
        Serves as a normal SQLAlchemy engine, but fakes existance of some
        tables.
        """
        def __init__(self, engine, mockTables=None, mockNonTables=None):
            self._engine = engine
            self.mockTables = mockTables or []
            self.mockNonTables = mockNonTables or []
        def has_table(self, table):
            if table in self.mockTables:
                return True
            elif table in self.mockNonTables:
                return False
            else:
                return self._engine.has_table(table)
        def __getattr__(self, attr):
            return getattr(self._engine, attr)

    def setUp(self):
        NeedsDatabaseTest.setUp(self)
        self.characterLookup = characterlookup.CharacterLookup('T',
            dbConnectInst=self.db)

    def shortDescription(self):
        methodName = getattr(self, self.id().split('.')[-1])
        # get whole doc string and remove superfluous white spaces
        noWhitespaceDoc = re.sub('\s+', ' ', methodName.__doc__.strip())
        # remove markup for epytext format
        return re.sub('[CLI]\{([^\}]*)}', r'\1', noWhitespaceDoc)


class CharacterLookupMetaTest(CharacterLookupTest, unittest.TestCase):
    def testInitialization(self):
        """Test initialisation."""
        # test if locales are accepted
        for locale in 'TCJKV':
            characterlookup.CharacterLookup(locale, dbConnectInst=self.db)

        # test if locale is rejected
        self.assertRaises(ValueError, characterlookup.CharacterLookup, 'F',
            dbConnectInst=self.db)

        # test default database connector
        characterlookup.CharacterLookup('T')

        # test if character domain 'Unicode' is accepted
        characterlookup.CharacterLookup('T', 'Unicode', dbConnectInst=self.db)

        # test if character domain is accepted
        from sqlalchemy import Table, Column, String
        domain = 'MyDomain'
        tableObj = Table(domain + 'Set', self.db.metadata,
            Column('ChineseCharacter', String))
        mydb = CharacterLookupTest.DatabaseConnectorMock(self.db,
            mockTables=[domain + 'Set'], mockTableDefinition=tableObj)
        characterlookup.CharacterLookup('T', domain, dbConnectInst=mydb)
        self.db.metadata.remove(tableObj)

        # test if character domain is rejected
        domain = 'MyDomain'
        mydb = CharacterLookupTest.DatabaseConnectorMock(self.db,
            mockNonTables=[domain + 'Set'])
        self.assertRaises(ValueError, characterlookup.CharacterLookup, 'T',
            domain, dbConnectInst=mydb)

        # test if character domain is rejected
        domain = 'MyOtherDomain'
        tableObj = Table(domain + 'Set', self.db.metadata,
            Column('SomeColumn', String))
        mydb = CharacterLookupTest.DatabaseConnectorMock(self.db,
            mockTables=[domain + 'Set'], mockTableDefinition=tableObj)
        self.assertRaises(ValueError, characterlookup.CharacterLookup, 'T',
            domain, dbConnectInst=mydb)
        self.db.metadata.remove(tableObj)

    def testAvailableCharacterDomains(self):
        """Test if C{getAvailableCharacterDomains()} returns proper domains."""
        # test default domain
        self.assert_('Unicode' \
            in self.characterLookup.getAvailableCharacterDomains())

        # test provided domain
        from sqlalchemy import Table, Column, String
        domain = 'MyDomain'
        tableObj = Table(domain + 'Set', self.db.metadata,
            Column('ChineseCharacter', String))
        mydb = CharacterLookupTest.DatabaseConnectorMock(self.db,
            mockTables=[domain + 'Set'], mockTableDefinition=tableObj)
        cjk = characterlookup.CharacterLookup('T', dbConnectInst=mydb)
        self.assert_(domain in cjk.getAvailableCharacterDomains())
        self.db.metadata.remove(tableObj)

        # test domain not included
        domain = 'MyDomain'
        mydb = CharacterLookupTest.DatabaseConnectorMock(self.db,
            mockNonTables=[domain + 'Set'])
        cjk = characterlookup.CharacterLookup('T', dbConnectInst=mydb)
        self.assert_(domain not in cjk.getAvailableCharacterDomains())

        # test domain not included
        domain = 'MyOtherDomain'
        tableObj = Table(domain + 'Set', self.db.metadata,
            Column('SomeColumn', String))
        mydb = CharacterLookupTest.DatabaseConnectorMock(self.db,
            mockTables=[domain + 'Set'], mockTableDefinition=tableObj)
        cjk = characterlookup.CharacterLookup('T', dbConnectInst=mydb)
        self.assert_(domain not in cjk.getAvailableCharacterDomains())
        self.db.metadata.remove(tableObj)


class CharacterLookupCharacterDomainTest(CharacterLookupTest,
    unittest.TestCase):

    def testCharacterDomainInUnicode(self):
        """
        Tests if all character domains are included in the maximum Unicode
        domain.
        """
        for domain in self.characterLookup.getAvailableCharacterDomains():
            characterLookupDomain = characterlookup.CharacterLookup('T',
                domain, dbConnectInst=self.db)
            domainChars = [c for c \
                in characterLookupDomain.getDomainCharacterIterator()]
            self.assert_(domainChars \
                == self.characterLookup.filterDomainCharacters(domainChars))

    @attr('slow')
    def testDomainCharsAccepted(self):
        """Test if all characters in the character domain are accepted."""
        for domain in self.characterLookup.getAvailableCharacterDomains():
            characterLookupDomain = characterlookup.CharacterLookup('T',
                domain, dbConnectInst=self.db)
            for char in characterLookupDomain.getDomainCharacterIterator():
                self.assert_(characterLookupDomain.isCharacterInDomain(char))

    def testFilterIdentityOnSelf(self):
        """
        Test if filterDomainCharacters operates as identity on characters from
        domain.
        """
        for domain in self.characterLookup.getAvailableCharacterDomains():
            characterLookupDomain = characterlookup.CharacterLookup('T',
                domain, dbConnectInst=self.db)
            domainChars = [c for c \
                in characterLookupDomain.getDomainCharacterIterator()]
            self.assert_(domainChars \
                == characterLookupDomain.filterDomainCharacters(domainChars))


class CharacterLookupStrokesTest(CharacterLookupTest, unittest.TestCase):

    def testUnicodeNamesMatchAbbreviations(self):
        """
        Tests if the stroke form names by Unicode match the abbreviations
        defined here.
        """
        import unicodedata
        for strokeCP in range(int('31C0', 16), int('31EF', 16)+1):
            stroke = unichr(strokeCP)
            try:
                abbrev = unicodedata.name(stroke).replace('CJK STROKE ', '')
            except ValueError:
                continue
            try:
                self.assertEquals(stroke,
                    self.characterLookup.getStrokeForAbbrev(abbrev))
            except ValueError:
                self.fail("Abbreviation '%s' not supported" % abbrev)


class CharacterLookupReadingMethodsTest(CharacterLookupTest, unittest.TestCase):
    """
    Runs consistency checks on the reading methods of the
    L{characterlookup.CharacterLookup} class.
    @todo Impl: include script table from Unicode 5.2.0 to get character ranges
        for Hangul and Kana
    """
    DIALECTS = {}

    SPECIAL_ENTITY_LIST = {}

    def setUp(self):
        CharacterLookupTest.setUp(self)
        self.f = ReadingFactory(dbConnectInst=self.db)

    def testReadingMappingAvailability(self):
        """
        Test if the readings under
        C{CharacterLookup.CHARARACTER_READING_MAPPING} are available for
        conversion.
        """
        # mock to simulate availability of all tables in
        #   characterLookup.CHARARACTER_READING_MAPPING
        tables = [table for table, _ \
            in self.characterLookup.CHARARACTER_READING_MAPPING.values()]
        self.characterLookup.db.engine = CharacterLookupTest.EngineMock(
                self.characterLookup.db.engine, mockTables=tables)

        for reading in self.characterLookup.CHARARACTER_READING_MAPPING:
            # only if table exists
            table, _ = self.characterLookup.CHARARACTER_READING_MAPPING[reading]

            self.assert_(
                self.characterLookup.hasMappingForReadingToCharacter(reading))
            self.assert_(
                self.characterLookup.hasMappingForCharacterToReading(reading))

        # test proper checking for all known readings
        for reading in self.f.getSupportedReadings():
            self.assert_(
                self.characterLookup.hasMappingForReadingToCharacter(reading) \
                in [True, False])
            self.assert_(
                self.characterLookup.hasMappingForCharacterToReading(reading) \
                in [True, False])

    @attr('slow')
    def testGetCharactersForReadingAcceptsAllEntities(self):
        """Test if C{getCharactersForReading} accepts all reading entities."""
        for reading in self.f.getSupportedReadings():
            if not self.characterLookup.hasMappingForReadingToCharacter(
                reading):
                continue

            dialects = [{}]
            if reading in self.DIALECTS:
                dialects.extend(self.DIALECTS[reading])

            for dialect in dialects:
                if hasattr(self.f.getReadingOperatorClass(reading),
                    'getReadingEntities'):
                    entities = self.f.getReadingEntities(reading, **dialect)
                elif reading in self.SPECIAL_ENTITY_LIST:
                    entities = self.SPECIAL_ENTITY_LIST[reading]
                else:
                    continue

                for entity in entities:
                    try:
                        results = self.characterLookup.getCharactersForReading(
                            entity, reading, **dialect)

                        self.assertEquals(type(results), type([]),
                            "Method getCharactersForReading() doesn't return" \
                                + " a list for entity %s " % repr(entity) \
                        + ' (reading %s, dialect %s)' % (reading, dialect))

                        for entry in results:
                            self.assertEquals(len(entry), 1,
                                "Entry %s in result for %s has length != 1" \
                                    % (repr(entry), repr(entity)) \
                                + ' (reading %s, dialect %s)' \
                                % (reading, dialect))
                    except exception.UnsupportedError:
                        pass
                    except exception.ConversionError:
                        pass


class CharacterLookupReferenceTest(CharacterLookupTest):
    METHOD_NAME = None

    def shortDescription(self):
        methodName = getattr(self, self.id().split('.')[-1])
        # get whole doc string and remove superfluous white spaces
        noWhitespaceDoc = re.sub('\s+', ' ', methodName.__doc__.strip())
        # remove markup for epytext format
        clearName = re.sub('[CL]\{([^\}]*)}', r'\1', noWhitespaceDoc)
        # add name of reading
        return clearName + ' (for %s)' % self.METHOD_NAME

    def getCharacterLookupInst(self, options):
        if not hasattr(self, '_instanceDict'):
            self._instanceDict = {}
        if options not in self._instanceDict:
            self._instanceDict[options] = characterlookup.CharacterLookup(
                dbConnectInst=self.db, *options)

        return self._instanceDict[options]

    def testMethodReferences(self):
        """Test if the given references are reached"""
        for options, references in self.REFERENCE_LIST:
            cjk = self.getCharacterLookupInst(options)
            method = getattr(cjk, self.METHOD_NAME)

            for methodArgs, methodOptions, target in references:
                result = method(*methodArgs, **methodOptions)
                self.assertEquals(result, target,
                    "Target %s not reached for input %s: %s" \
                        % (repr(target), repr((methodArgs, methodOptions)),
                            repr(result)))


class CharacterLookupFilterDomainCharactersReferenceTest(
    CharacterLookupReferenceTest, unittest.TestCase):
    METHOD_NAME = 'filterDomainCharacters'

    REFERENCE_LIST = [
        (('T', 'Unicode'), [
            (([u'说', u'説', u'說', u'丷', u'か', u'국'], ), {},
                [u'说', u'説', u'說', u'丷']),
            ]),
        (('T', 'BIG5'), [
            (([u'说', u'説', u'說', u'丷', u'か', u'국'], ), {}, [u'說']),
            ]),
        (('T', 'GB2312'), [
            (([u'说', u'説', u'說', u'丷', u'か', u'국'], ), {}, [u'说']),
            ]),
        ]


class CharacterLookupIsCharacterInDomainReferenceTest(
    CharacterLookupReferenceTest, unittest.TestCase):
    METHOD_NAME = 'isCharacterInDomain'

    REFERENCE_LIST = [
        (('T', 'Unicode'), [
            ((u'说', ), {}, True),
            ((u'説', ), {}, True),
            ((u'說', ), {}, True),
            ((u'丷', ), {}, True),
            ((u'か', ), {}, False),
            ((u'국', ), {}, False),
            ]),
        (('T', 'BIG5'), [
            ((u'说', ), {}, False),
            ((u'説', ), {}, False),
            ((u'說', ), {}, True),
            ((u'丷', ), {}, False),
            ((u'か', ), {}, False),
            ((u'국', ), {}, False),
            ]),
        (('T', 'GB2312'), [
            ((u'说', ), {}, True),
            ((u'説', ), {}, False),
            ((u'說', ), {}, False),
            ((u'丷', ), {}, False),
            ((u'か', ), {}, False),
            ((u'국', ), {}, False),
            ]),
        ]


class CharacterLookupGetReadingForCharacterReferenceTest(
    CharacterLookupReferenceTest, unittest.TestCase):
    METHOD_NAME = 'getReadingForCharacter'

    REFERENCE_LIST = [
        (('T', ), [
            ((u'中', 'Pinyin'), {}, [u'zhōng', u'zhòng']),
            ((u'漢', 'Hangul'), {}, [u'한']),
            ((u'漢', 'MandarinBraille'), {}, [u'⠓⠧⠆', u'⠞⠧⠁']),
            ]),
        ]


class CharacterLookupGetCharactersForReadingReferenceTest(
    CharacterLookupReferenceTest, unittest.TestCase):
    METHOD_NAME = 'getCharactersForReading'

    REFERENCE_LIST = [
        (('T', 'GB2312'), [
            ((u'èr', 'Pinyin'), {}, [u'二', u'佴', u'贰', u'铒']),
            ]),
        (('T', 'BIG5'), [
            ((u'm\u0300h', 'CantoneseYale'), {}, [u'唔', u'嘸']),
            ]),
        ]
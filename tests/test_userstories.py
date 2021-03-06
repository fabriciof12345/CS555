import unittest
from gedcom.parser import Parser
from gedcom.element.individual import IndividualElement
from datetime import datetime

import os
import sys
sys.path.append('.')
import team6

# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)
# import team6


class TestBirthBeforeDeath(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(team6.birthBeforeDeath(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test01.ged")), 'Birth came before death')

    def test_incorrect(self):
        self.assertFalse(team6.birthBeforeDeath(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test02.ged")), 'Death came before birth')

    def test_none(self):
        self.assertIsNone(team6.birthBeforeDeath(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test03.ged")), 'Birth or death records missing')


class TestBirthBeforeMarriage(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(team6.birthBeforeMarriage(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test04.ged")), 'Birth came before marriage')

    def test_incorrect(self):
        self.assertFalse(team6.birthBeforeMarriage(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test05.ged")), 'Marriage came before birth')

    def test_none(self):
        self.assertIsNone(team6.birthBeforeMarriage(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test06.ged")), 'birth or marriage records missing')


class TestDatesBeforeCurrentDate(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(team6.datesBeforeCurrentDate(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US01-US05/test01.ged")), 'All dates came before current date')

    def test_incorrect(self):
        self.assertFalse(team6.datesBeforeCurrentDate(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US01-US05/test02.ged")), 'A date came after the current date')


class TestMarriageBeforeDeath(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(team6.marriageBeforeDeath(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US01-US05/test03.ged")), 'Marriage came before death')

    def test_incorrect(self):
        self.assertFalse(team6.marriageBeforeDeath(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US01-US05/test04.ged")), 'Death came before Marriage')

    def test_none(self):
        self.assertIsNone(team6.marriageBeforeDeath(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US01-US05/test05.ged")), 'Death or marriage records missing')

class TestNoBigamy(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(team6.noBigamy(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US11-US14/test01.ged")), 'Divorce always came before remarrage')

    def test_incorrect(self):
        self.assertFalse(team6.noBigamy(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US11-US14/test02.ged")), 'Bigamy occurred')


class TestMultipleBirths(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(team6.multipleBirths(team6.processGedcomFamily(
            "tests/GEDCOM files for unit testing/US11-US14/test03.ged")), 'Less than 5 births occurred at once')

    def test_incorrect(self):
        self.assertFalse(team6.multipleBirths(team6.processGedcomFamily(
            "tests/GEDCOM files for unit testing/US11-US14/test04.ged")), 'More than 5 births occurred at once')

class TestListErrors(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(team6.listErrors(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test02.ged")), 'At least one error occurred')
    
    def test_incorrect(self):
        self.assertFalse(team6.listErrors(team6.processGedcom(
            "tests/GEDCOM files for unit testing/US02-US03/test01.ged")), 'No errors occurred')
        


if __name__ == '__main__':
    unittest.main(verbosity=2)

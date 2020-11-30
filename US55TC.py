
import unittest
import US55

# Less than 150 years old
class TestStringMethods(unittest.TestCase):
   

    #Format (husband,wife)
    def test_century_leap_year(self):
        self.assertTrue(US55.CenturyBabies("2000AUG27"),"Century Leap Year")
        
    def test_invalid_Feb(self):
        self.assertFalse(US55.CenturyBabies("1950JUN17"),"Feb more than 3 days")
            
    def test_valid_CLY_Feb(self):
        self.assertTrue(US55.CenturyBabies("1900JAN03"),"Non Century Leap Year Valid Date")
        
    def test_valid_date(self):
        self.assertTrue(US55.CenturyBabies("2000MAR10"),"Husband is two times older")
        
    def test_invalid_CLY_Feb(self):
        self.assertFalse(US55.CenturyBabies("1999FEB20"),"Not a Leap Year")
        
    def test_fail_on_same_year(self):
        self.assertFalse(US55.CenturyBabies("2020NOV30"),"Invalid Normal Month")

if __name__ == '__main__':
    unittest.main()

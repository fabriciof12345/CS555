import unittest
import US54


class TestStringMethods(unittest.TestCase):

    global result
    result = US54.retrieveInfo()
    
    #Format (husband,wife)
    def test_century_leap_year(self):
        self.assertEqual(US54.eldestIndividual(result),['Federico Diaz', '84'])
        
    def test_invalid_Feb(self):
        self.assertEqual(US54.eldestIndividual([['Javier Diaz', 20], ['Xavier Diaz', 21]]), ['Xavier Diaz', 21])
            
    def test_valid_CLY_Feb(self):
        self.assertEqual(US54.eldestIndividual([['Valentina Bustamante', 20], ['Dariel Pena', 11], ['Daisy Geronimo', 66],['Jamel Abubakar', 30]]),['Daisy Geronimo', 66])
        
    def test_valid_date(self):
        self.assertEqual(US54.eldestIndividual([['Valentina Bustamante', 20]]),['Valentina Bustamante', 20])
        
    def test_invalid_CLY_Feb(self):
        self.assertFalse(US54.eldestIndividual([]),"Empty List")

if __name__ == '__main__':
    unittest.main()



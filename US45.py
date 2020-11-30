import unittest;
#
# User story for giving birth before 14.
# 
# Matthew Evanego
class TestUS45(unittest.TestCase):

    childBirthDate = [3,4,1993]
    birthDate = [1, 5, 1960]
    #Ensures that person has not given birth before 14
    def birthbefore14(self, childBirthDate, birthDate):
        if(childBirthDate[2] - birthDate[2] < 14):
            return False
        elif(childBirthDate[2] - birthDate[2] == 14 and childBirthDate[1] - birthDate[1] > 0 and childBirthDate[0] - birthDate[0] > 0):
            return False
        return True

    #Testing both of the parents
    def test_birthbefore14(self):
        childBirthDate = [3, 4, 1993]
        birthDate = [1, 5, 1960]
        self.assertTrue(self.birthbefore14(childBirthDate, birthDate))
        childBirthDate = [3,4,1970]
        self.assertFalse(self.birthbefore14(childBirthDate, birthDate))
        

        

if __name__ == '__main__':
    unittest.main()
        

import unittest;
#
# User story for listing all elders (>=63)
# 
# Matthew Evanego
class TestUS46(unittest.TestCase):


    #returns all elders
    def listElders(self, peopleList):
        returnList = []
        for person in peopleList:
            if(person[1] >= 63):
                returnList = returnList + [person[0]]
        return returnList

    #Testing list Elders
    def test_listElders(self):
        peopleList = [["Alan", 32], ["Jeff", 54], ["Susan", 76]]
        self.assertEquals(self.listElders(peopleList), ["Susan"])
        peopleList = [["Matt", 21], ["Sammy", 23]]
        self.assertEquals(self.listElders(peopleList), [])
        

        

if __name__ == '__main__':
    unittest.main()
        

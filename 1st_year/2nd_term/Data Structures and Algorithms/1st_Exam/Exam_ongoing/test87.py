from midtermexam87 import SList

import unittest #package that contains the classes t

class Test(unittest.TestCase):
    
    mark=0

    def setUp(self):
        """This functions is executed for each of the test functions"""
        self.l1=SList()
        self.data=[1,2,3,4,5,6]
        for x in self.data:
            self.l1.append(x)
           
        self.l2=SList()
        self.data=[1,1,2,2,3,4,5,6]
        for x in self.data:
            self.l2.append(x)

        self.l3=SList()
        self.data=[1,2,3,4,5,6,6]
        for x in self.data:
            self.l3.append(x)
        
        self.l4=SList()
        self.data=[1,2,3,3,4,4,5,5,5,6]
        for x in self.data:
            self.l4.append(x)


    def test1_reverseDup(self):
        """ Case empty list"""
        self.empty=SList()
        expected=[]
        self.assertEqual(str(self.empty), str(expected), "Fail: Case 1: list empty'")
           
    def test2_reverseDup(self):
        """ Case list with one elem"""
        self.l=SList()
        self.l.append(1)
        expected = [1]
        self.assertEqual(str(self.l), str(expected), "Fail: Case 2: list with one element'")

               
    def test3_reverseDup(self):
        """ Case list with 2 different elems"""
        self.l=SList()
        self.l.append(1)
        self.l.append(2)
        expected=[2,1]
        self.l.reverseDup()
        self.assertEqual(str(self.l), str(expected), "Fail: Case3: list with 2 different elements")
     
    def test4_reverseDup(self):
        """ Case list with different elems"""
        expected = [6,5,4,3,2,1]
        self.l1.reverseDup()
        self.assertEqual(str(self.l1), str(expected), "Fail: Case 4: list with different elements")
      
        
    def test5_reverseDup(self):
        """ Case list with 2 duplicated elems"""
        self.l=SList()
        self.l.append(1)
        self.l.append(1)
        expected=[1]
        self.l.reverseDup()
        self.assertEqual(str(self.l), str(expected), "Fail: Case 5: 2 duplicated elements")
   
        
    def test6_reverseDup(self):
        """ Case list starting with 2 duplicated elements"""
        expected = [6,5,4,3,2,1]
        self.l2.reverseDup()
        self.assertEqual(str(self.l2), str(expected), "Fail: Case 6: list starting with 2 duplicated elements")
      
         
    def test7_reverseDup(self):
        """ Case list ending with2 duplicated elements"""
        expected = [6,5,4,3,2,1]
        self.l3.reverseDup()
        self.assertEqual(str(self.l3), str(expected), "Fail: Case 7: list ending with 2 duplicated elements")
     
        
    def test8_reverseDup(self):
        """ Case list  with repeated elems"""
        expected = [6,5,4,3,2,1]
        self.l3.reverseDup()
        self.assertEqual(str(self.l3), str(expected), "Fail: Case 8: list with repeated elements")
        Test.mark+=2

  

#If you are using Spyder, please comment the following line: 
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#To use Spyder, remove the following comments:
if __name__ == '__main__':
    unittest.main()


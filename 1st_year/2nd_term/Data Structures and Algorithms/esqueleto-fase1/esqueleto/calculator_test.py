# This is a unit tests class containing proper tests, which is the good way to proceed. 
# This will allow you to automate your tests so that you make sure that your code behaves as expected
# Note that third test will fail automatically, so there is no way that we miss it

import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

    # this method is meant to be executed BEFORE EACH TEST defined below, so we initialize calc here to 
    # avoid duplicating code
    
    def setUp(self):
        self.calc = Calculator()
        self.l1=[]
        self.l2=[1,2,3]

    # Testing add as before
    def testAdd(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result,8)

   # Testing subtract as before
    def testSubtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result,2)
    
    # Testing wrongAdd as before
    def testWrongAdd(self):
       result = self.calc.wrongAdd(5, 3)
       self.assertEqual(result,8)
       
  


if __name__ == '__main__':
    unittest.main()
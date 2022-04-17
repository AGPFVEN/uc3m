#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:30:41 2022

@author: isegura
"""

import unittest
import random
from phase1 import SList2

class Test(unittest.TestCase):

    def setUp(self):
        self.l = SList2()
        self.data=[]
        for i in range(10):
            self.data.append(random.randint(0,10))

        for x in self.data:
            self.l.addLast(x)
            
        self.data2=[]
        for i in range(11):
            self.data2.append(random.randint(0,10))

        self.l2 = SList2()

        for x in self.data2:
            self.l2.addLast(x)
            
        self.l3= SList2()
        for x in range(5):
            self.l3.addLast(x)
        

    def testsumLastN1_Nnegative(self):
         print("\n\ttestsumLastN1 n negative")
         expected = None
         result = self.l.sumLastN(-3)
         self.assertEqual(result, expected)
         print("\ttestsumLastN1 n negative, OK!!!")
    
    def testsumLastN2_lenList(self):
        print("\n\ttestsumLastN2 n=len(l)")
        expected = sum(self.data)
        result = self.l.sumLastN(len(self.l))
        self.assertEqual(result, expected)
        print("\ttestsumLastN2 n=len(l), OK!!!")

    def testsumLastN3_Nlarge(self):
        print("\n\ttestsumLastN3 n>len(l)")
        expected = sum(self.data)
        result = self.l.sumLastN(len(self.l)+5)
        self.assertEqual(result, expected)
        print("\ttestsumLastN3 n>len(l), OK!!!")

    def testsumLastN4_Listempty(self):
        print("\n\ttestsumLastN4, list empty)")
        expected = 0
        lEmpty=SList2()
        result = lEmpty.sumLastN(0)
        self.assertEqual(result, expected)
        print("\ttestsumLastN4, list empty, OK!!!")
        
        
    def testsumLastN5_n1(self):
        print("\n\ttestsumLastN5, n=len(l)-1")
        expected = sum(self.data)-self.data[0]
        result = self.l.sumLastN(len(self.l)-1)
        self.assertEqual(result, expected)
        print("\ttestsumLastN5, n=len(l)-1, OK!!!")
        

        
    def testsumLastN6_N6(self):
        print("\n\ttestsumLastN6, n=6")
        expected = sum(self.data[len(self.data)-6:])
        result = self.l.sumLastN(6)
        self.assertEqual(result, expected)
        print("\ttestsumLastN6, n=6, OK!!!")
        
    
    def testsumLastN7_N2(self):
        print("\n\ttestsumLastN7, n=2")
        expected = sum(self.data[len(self.data)-2:])
        result = self.l.sumLastN(2)
        self.assertEqual(result, expected)
        print("\ttestsumLastN7, n=2, OK!!!")
        
    def testinsertMiddle_1(self):
        print("\n\tinsertMidle1 in an empty list")
        l=SList2()
        l.insertMiddle(5)

        expected = [5]
        self.assertEqual(str(l), str(expected))
        print("\tinsertMidle1 in an empty list, OK")


    def testinsertMiddle_2(self):
        print("\n\tinsertMidle2 in an non empty even list")
        
        #print(str(self.l),self.data)
        _size=len(self.l)
        _index=_size//2
        
        e=35 #value to insert

        self.l.insertMiddle(e)
        self.data.insert(_index,e)


        self.assertEqual(str(self.l), str(self.data))
        print("\tinsertMiddle2 in an non-empty even list, OK!!!")

    def testinsertMiddle_3(self):
        print("\n\tinsertMiddle3 in an non-empty odd list")

        _size = len(self.l2)
        _index = _size // 2 + 1
        
        e = 17  # value to insert

        self.l2.insertMiddle(e)
        self.data2.insert(_index, e)
        self.assertEqual(str(self.l2), str(self.data2))
        print("\tinsertMiddle3 in an non-empty odd list, OK!!!")
        
    def testInsertList1(self):
        print("\n\tinsertList1 start<0")
        inputList=SList2()
        self.l.insertList(inputList,-1,2)
        expected=self.data
        self.assertEqual(str(self.l), str(expected))
        print("\tinsertList start<0, ok!!!")
        
    def testInsertList2(self):
        print("\n\tinsertList2 end>=len(l)")
        inputList=SList2()
        self.l.insertList(inputList,0,len(self.l))
        expected=self.data
        self.assertEqual(str(self.l), str(expected))
        print("\tinsertList2 end>=len(l), ok!!!")
        
    def testInsertList3(self):
        print("\n\tinsertList3 start>end)")
        inputList=SList2()
        self.l.insertList(inputList,2,1)
        expected=self.data
        self.assertEqual(str(self.l), str(expected))
        print("\n\tinsertList3 start>end), ok!!!")

    def testInsertList4(self):
        print("\n\tinsertList4 start=0,end=0")
        
        inputList=SList2()
        inputList.addFirst(10)
        inputList.addFirst(10)
        inputList.addFirst(10)
        
        self.l3.insertList(inputList,0,0)
        expected=[10,10,10,1,2,3,4]
        self.assertEqual(str(self.l3), str(expected))
        print("\tinsertList4 start>end), ok!!!")
    
    def testInsertList5(self):
        print("\n\tinsertList5 start=0,end=len(l)-1")
        
        inputList=SList2()
        inputList.addFirst(10)
        inputList.addFirst(10)
        inputList.addFirst(10)
        
        self.l3.insertList(inputList,0,len(self.l3)-1)
        expected=[10,10,10]
        self.assertEqual(str(self.l3), str(expected))
        print("\tinsertList5 start=0,end=len(l)-1")
        
    def testInsertList6(self):
        print("\n\tinsertList6 start=0,end=len(l)//2")
        
        inputList=SList2()
        inputList.addFirst(10)
        inputList.addFirst(10)
        inputList.addFirst(10)
        
        self.l3.insertList(inputList,0,len(self.l3)//2)
        expected=[10,10,10,3,4]
        self.assertEqual(str(self.l3), str(expected))
        print("\tinsertList6 start=0,end=len(l)//2")
        
    def testInsertList7(self):
        print("\n\tinsertList7 start=len(l)//2, end=len(l)-1")
        
        inputList=SList2()
        inputList.addFirst(10)
        inputList.addFirst(10)
        inputList.addFirst(10)
        
        self.l3.insertList(inputList,len(self.l3)//2,len(self.l3)-1)
        expected=[0,1,10,10,10]
        self.assertEqual(str(self.l3), str(expected))
        print("\tinsertList7 start=len(l)//2, end=len(l)-1, ok")
        
    def testInsertList8(self):
        print("\n\tinsertList7 start=1, end=len(l)-2")
        
        inputList=SList2()
        inputList.addFirst(10)
        inputList.addFirst(10)
        inputList.addFirst(10)
        
        self.l3.insertList(inputList,1,len(self.l3)-2)
        expected=[0,10,10,10,4]
        self.assertEqual(str(self.l3), str(expected))
        print("\tinsertList7 start=1, end=len(l)-2, ok")
    
    
    def testMaximumPair1(self):
        print("\n\tmaximumPair1, list empty")
        inputList=SList2()
        result=inputList.maximumPair()
        expected=None
        self.assertEqual(expected,result)
        print("\tmaximumPair1, list empty, ok!!!")

        
    def testMaximumPair2(self):
        print("\n\tmaximumPair2, list size=1")
        inputList=SList2()
        for x in [3]:
            inputList.addLast(x)
            
        result=inputList.maximumPair()
        expected=3
        self.assertEqual(expected,result)
        print("\tmaximumPair2, list size=1, ok!!")


    def testMaximumPair3(self):
        print("\n\tmaximumPair3, list size=2")
        inputList=SList2()
        for x in [3,2]:
            inputList.addLast(x)
            
        result=inputList.maximumPair()
        expected=5
        self.assertEqual(expected,result)
        print("\tmaximumPair3, list size=2, ok!!!")


    def testMaximumPair4(self):
        print("\n\tmaximumPair4, list size=3")
        inputList=SList2()
        for x in [3,2,8]:
            inputList.addLast(x)
            
        result=inputList.maximumPair()
        expected=11
        self.assertEqual(expected,result)    
        print("\tmaximumPair4, list size=3, ok!!!")

        
    def testMaximumPair5(self):
        print("\n\tmaximumPair5, list size=4")
        inputList=SList2()
        for x in [3,2,8,1]:
            inputList.addLast(x)
            
        result=inputList.maximumPair()
        expected=10
        self.assertEqual(expected,result)
        print("\tmaximumPair5, list size=4, ok!!!")


    def testMaximumPair6(self):
        print("\n\tmaximumPair6, list size=5, middle>max")
        inputList=SList2()
        for x in [3,2,13,8,1]:
            inputList.addLast(x)
            
        result=inputList.maximumPair()
        expected=13
        self.assertEqual(expected,result) 
        print("\tmaximumPair6, list size=5, middle>max, ok!!!")

    
    def testMaximumPair7(self):
        print("\n\tmaximumPair7, list size=5, middle<max")
    
        inputList=SList2()
        for x in [10,2,-1,8,1]:
            inputList.addLast(x)
            
        result=inputList.maximumPair()
        expected=11
        self.assertEqual(expected,result) 
        print("\tmaximumPair7, list size=5, middle<max, ok!!!")

    
    def testMaximumPair8(self):
        print("\n\tmaximumPair8, list size=5, middle<max")
        inputList=SList2()
        for x in [10,2,-1,20, 8,1]:
            inputList.addLast(x)
            
        result=inputList.maximumPair()
        expected=19
        self.assertEqual(expected,result) 
        print("\tmaximumPair8, list size=5, middle<max, ok!!!")

        
    def testreverseK1(self):
        print("\n\treverseK1, list empty")
        inputList=SList2()
            
        inputList.reverseK(1)
        expected=[]
        self.assertEqual(str(expected),str(inputList)) 
        print("\treverseK1, list empty, ok!!!")


    def testreverseK2(self):
        print("\n\treverseK2, k=1")
        inputList=SList2()
        for x in [10,2,-1,20, 8,1]:
            inputList.addLast(x)
        inputList.reverseK(1)
        expected=[10,2,-1,20, 8,1]
        self.assertEqual(str(expected),str(inputList))
        print("\treverseK2, k=1, ok!!!")

    
    def testreverseK3(self):
        print("\n\treverseK3, k=2")
        inputList=SList2()
        for x in [10,2,-1,20, 8,1]:
            inputList.addLast(x)
        inputList.reverseK(2)
        expected=[2,10,20,-1,1,8]
        self.assertEqual(str(expected),str(inputList))
        print("\treverseK3, k=2, ok!!!")

    def testreverseK4(self):
        print("\n\treverseK4, k=3")
        inputList=SList2()
        for x in [10,2,-1,20, 8,1]:
            inputList.addLast(x)
        inputList.reverseK(3)
        expected=[-1,2,10,1,8,20]
        self.assertEqual(str(expected),str(inputList))
        print("\treverseK4, k=3, ok!!!")


    def testreverseK5(self):
        print("\n\treverseK5, k=4")
        inputList=SList2()
        for x in [10,2,-1,20, 8,1]:
            inputList.addLast(x)
        inputList.reverseK(4)
        expected=[20,-1,2,10,1,8]
        self.assertEqual(str(expected),str(inputList))
        print("\treverseK5, k=4, ok!!!")
        

    def testreverseK6(self):
        print("\n\treverseK6, k=len")
        inputList=SList2()
        for x in [10,2,-1,20, 8,1]:
            inputList.addLast(x)
        inputList.reverseK(len(inputList))
        expected=[1,8,20,-1,2,10]
        self.assertEqual(str(expected),str(inputList))
        print("\treverseK6, k=len, ok!!!")
    
    
    def testreverseK7(self):
        print("\n\treverseK7, k=len+3")
        inputList=SList2()
        for x in [10,2,-1,20, 8,1]:
            inputList.addLast(x)
        inputList.reverseK(len(inputList)+3)
        expected=[1,8,20,-1,2,10]
        self.assertEqual(str(expected),str(inputList))
        print("\treverseK7, k=len+3, ok!!!")

        
if __name__ == "__main__":
    unittest.main()
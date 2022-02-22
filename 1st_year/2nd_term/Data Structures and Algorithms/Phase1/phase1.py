from tabnanny import check
from slist import SList
import sys

class SList2(SList):

    def check_int(n):
        if type(n) == int:
            return True
        else:
            return False

    def sumLastN(self, n):
        if(type(n) == False):
            print("Invalid input")
            return None

        if (n < 0):
            print("Invalid input")
            return None

        if self._head == None:
            print("List is empty")
            return 0

        result = 0
        first_node = self._head

        for i in range(1, self.size - n):
            first_node = first_node.next

        for i in range(1, n):
            result += 1
            first_node = first_node.next

        return result
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        ...

    
    def insertList(self,inputList,start,end):
        ...


    def reverseK(self,k):
        ...


    def maximumPair(self):
        ...
 
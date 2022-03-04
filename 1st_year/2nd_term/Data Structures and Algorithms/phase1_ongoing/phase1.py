from phase1.slist import SNode
from slist import SList

class SList2(SList):

    def check_int(n):
        if type(n) == int:
            return True
        else:
            return False

    def sumLastN(self, n):
        if(type(n) != int):
            print("Invalid input")
            return None

        if (n < 0):
            print("Invalid input")
            return None

        if self._head == None:
            print("List is empty")
            return 0

        if (n > self._size):
            n = self._size

        result = 0
        first_node = self._head

        for _ in range(0, self._size - n):
            first_node = first_node.next

        for _ in range(0, n):
            result += first_node.elem
            first_node = first_node.next

        return result
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        if (self._size == 0):
            self.addFirst(elem)

        selected_node = self._head
        new_node = SNode(elem)

        #Slist is even
        if (self._size % 2 == 0):
            for _ in range(1, self._size / 2):
                selected_node = selected_node.next

        #Slist is odd
        else:
            for _ in range(1, (self._size + 1) / 2):
                selected_node = selected_node.next

        #Insert new node
        new_node = selected_node.next
        selected_node.next = new_node
    
    def insertList(self,inputList,start,end):
        ...


    def reverseK(self,k):
        ...


    def maximumPair(self):
        ... 
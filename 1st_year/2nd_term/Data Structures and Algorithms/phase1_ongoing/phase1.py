from ast import LShift
from matplotlib.pyplot import prism
from numpy import insert
from slist import SNode
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
    
    #Method for inserting a new node in the middle
    def insertMiddle(self, elem):
        #Slist is empty
        if (self._size == 0):
            self.addFirst(elem)
            return None

        #Select head and create new node
        selected_node = self._head
        new_node = SNode(elem)

        #Slist is even
        if (self._size % 2 == 0):
            for _ in range(1, int(self._size / 2)):
                selected_node = selected_node.next

        #Slist is odd
        else:
            for _ in range(1, int((self._size + 1) / 2)):
                selected_node = selected_node.next

        #Insert new node
        new_node.next = selected_node.next
        selected_node.next = new_node
    
    def insertList(self,inputList,start,end):
        #Slist is empty
        if self._size == 0:
            self._head = inputList._head

        #Invalid indexes
        if ((start or end) < 0) or ((start or end) > self._size) or (start > end):
            print("Invalid index")
            return None

        #Select head
        selected_node = self._head
        changed = False

        if start == 0:
            self._head = inputList._head
            changed = True

        #Get to start
        while start - 1 > 0:
            selected_node = selected_node.next
            start -= 1
            end -= 1

        #Attach two slists (beggining)
        node_carry = selected_node.next
        if changed == False:
            selected_node.next = inputList._head
        else:
            selected_node = self._head

        #Select final item in slist
        while selected_node.next != None:
            print(selected_node.elem)
            selected_node = selected_node.next

        #Attach two list slists (finish)
        selected_node.next = node_carry

        #Loop to deattach nodes from the list
        while end > 0:
            print("down")
            selected_node.next = selected_node.next.next
            end -= 1

    def reverseK(self,k):
        ...


    def maximumPair(self):
        ... 

ls = SList2()
ls.addFirst(10)
ls.addFirst(1)
ls.addFirst(0)
ls.addFirst(100)
ls.addFirst(99)
ls2 = SList2()
ls2.addFirst(5)
ls2.addFirst(9)
ls2.addFirst(4)
ls2.addFirst(20)
ls.insertList(ls2, 0, 3)

print(str(ls))
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
            return None

        #Invalid indexes
        if ((start or end) < 0) or ((start or end) > self._size) or (start > end):
            print("Invalid index")
            return None

        if inputList.isEmpty() == True:
            print("Input list empty")
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

        if selected_node != None:
            #Select final item in slist
            while selected_node.next != None:
                selected_node = selected_node.next
        else:
            return None

        #Attach two list slists (finish)
        selected_node.next = node_carry

        #Loop to deattach nodes from the list
        while end > 0:
            selected_node.next = selected_node.next.next
            end -= 1

    def maximumPair(self):
        #1)Create an auxiliar list to store the values of the first half of the list (inverted)
        #2)Create a second auxiliar list to store the values of the sums of pairs
        #3)Iterate the second auxiliar list to check the biggest value

        #Special Cases
        if self._size == 0:
            return None
        elif self._size == 1:
            return self._head.elem
        
        #Auxiliar values to accomplish 1)
        count = self._size // 2
        selected_node = self._head
        ls_aux = SList2()

        #Loop till the midlle of the list (if size = odd -> middle + 1)
        while count > 0:
            ls_aux.addFirst(selected_node.elem)
            selected_node = selected_node.next
            count -= 1

        #Create empty list and declaring auxiliar value to iterate second auxilar list
        selected_node2 = ls_aux._head
        ls_aux2 = SList2()

        #If size of list == odd add first value to the results list 
        # (due to consider as a possible result the middle of the list)
        if self._size % 2 != 0:
            ls_aux2.addFirst(selected_node.elem)
            selected_node = selected_node.next

        #Iterate auxiliar list to create the second auxiliar list (results list)
        while selected_node != None:
            ls_aux2.addFirst(selected_node.elem + selected_node2.elem)
            selected_node = selected_node.next
            selected_node2 = selected_node2.next

        #Auxiliar values to iterate second list of results
        selected_node = ls_aux2._head
        result = ls_aux2._head.elem

        #Iterate list of results and compare results
        while selected_node != None:
            if result < selected_node.elem:
                result = selected_node.elem
            selected_node = selected_node.next
    
        return result

    def reverseK(self,k):
        #1) We will need three aux variables and an aux list
        #2) One of the variables will iterate the main list (self) -> selected_node_1
        #3) This variable (selected_node_1) will help us to create the aux list
        #4) The aux list is an inverted list of k elements
        #5) The other two variables will help us implement this list in the main list (self)
        #6) One of the variables will point the last node before the aux list -> selected_node_3
        #(if it is the first aux list) -> we will use the self._head
        #7) The other variable will point the next node of the aux list -> selected_node_2

        #Special Cases
        if self._size == 0:
            return None
        
        if k <= 1:
            return None

        if k > self._size:
            k = self._size

        #All auxiliar values
        aux = k
        ls_aux = SList2()
        selected_node_1 = self._head
        selected_node_2 = None
        selected_node_3 = None

        #Iterate the main slist (self)
        while selected_node_1 != None:
            #Create first reverse group and select 
            while aux > 0 and selected_node_1 != None:
                ls_aux.addFirst(selected_node_1.elem)
                selected_node_1 = selected_node_1.next
                aux -= 1

                #Add first value and store it in a variable to store last element of aux list
                if (aux == k - 1):
                    selected_node_2 = ls_aux._head

            #If first editing of the main list (self)
            if selected_node_2.elem == self._head.elem:
                #Connect slists
                self._head = ls_aux._head
                selected_node_2.next = selected_node_1
            else:
                selected_node_3.next = ls_aux._head
                selected_node_2.next = selected_node_1
            
            #"Create" a last edited node (We are pointing instead of "creating")
            selected_node_3 = selected_node_2

            #Modify self (Cut original aux list and attach new list)
            aux = k
            ls_aux = SList2()

ls = SList2()
ls.addFirst(200)
ls.addFirst(120)
ls.addFirst(95)
ls.addFirst(80)
ls.addFirst(100)
ls.addFirst(30)
ls.addFirst(29)
ls.addFirst(5)
ls.addFirst(20)
ls.addFirst(2)
ls.addFirst(3)
ls.addFirst(4)
ls.addFirst(5)
ls.addFirst(7)
ls.addFirst(1)
ls.addFirst(10)
print(str(ls))
ls.reverseK(3)
print(str(ls))
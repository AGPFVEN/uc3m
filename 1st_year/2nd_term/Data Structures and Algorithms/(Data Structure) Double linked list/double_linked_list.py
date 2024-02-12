from hashlib import new
from operator import truediv
from pickletools import read_uint1
import re


class SNode:
    def __init__(self, e):
        self.e = e
        self.next = None
        self.previous = None

class SList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def addFirst(self, e):
        newNode = SNode(e)
        
        if self.isEmpty():
            self.tail = newNode
        else:
            self.head.previous = newNode
        
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def removeFirst(self):
        result = None

        if self.isEmpty():
            print("The list is empty")
            return result

        else:
            if self.size == 1:
                self.tail = None

            result = self.head.e
            self.head = self.head.next 
            self.head.previous = None #//////
            self.size -= 1
        
        return result

    def addLast(self, e):
        #If the list has no elements use addfirst
        if self.isEmpty == True:
            self.addFirst(e)

        else:
            newNode = SNode(e)
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
    
    def removeLast(self):
        result = None

        if self.isEmpty():
            print("List is empty")
            return result

        result = self.tail.e
        self.tail = self.tail.previous

        if self.tail == None:           #/////
            self.head = None            #/////
            
        else:                           #/////
            self.tail.next = None

        self.size -= 1
        
        return result

    def getAt(self, index):
        if index < 0 or index > self.size:
            print("Invalid index")
            return None
 
        result = self.head
        i = 0 
            
        while i < index:
            result = result.next
            i += 1 
            
        return result.e 
 
    def insertAt(self, index, e):  #????????
        result = None

        if index == 0:
            self.addFirst(e)
            return result

        if index == self.size:
            self.addLast(e)
            return result

        elif index < 0 or index >= self.size:
            print("Invalid index")
            return result
 
        else:
            aux_node = SNode(e)
            aux = self.head
            i = 0 

            #Iterate until the previus desired spot 
            while i < index - 1:
                aux = aux.next
                i += 1

            aux.next.previous = aux_node
            aux_node.next = aux.next
            aux_node.previous = aux
            aux.next = aux_node
            self.size += 1

            return result

    def removeAt(self, index): 
        if index >= self.size:
            print("Invalid index")
 
        aux = self.head

        for _ in range(index -1):
            aux = aux.next
 
        aux.next.next.previous = aux
        aux.next = aux.next.next
        self.size -= 1

    def contains(self, a):
        if self.isEmpty():
            print("The list is empty!")
            return None

        aux = self.head
        index_counter = 0
        found = False

        while aux.e != a or aux != None :
            aux = aux.next
            index_counter += 1

        if aux.e == a:
            return index_counter

        else:
            return -1

    def __str__(self):
        result = "list: ["
        aux = self.head

        while aux != None:
            result += str(aux.e)

            if aux.next != None:
                result += ", "
            
            aux = aux.next

        result += "]    size: " + str(self.size) + "   head: " + str(self.head.e) + "     tail: " + str(self.tail.e) 

        return result


#Check implementation of singly linked list
list1 = SList()

list1.addFirst(1)
print(str(list1))
list1.addFirst(2)
print(str(list1))
list1.addFirst(5)
print(str(list1))
list1.removeFirst()
print(str(list1))
list1.addLast("hola")
print(str(list1))
list1.addLast("9")
print(str(list1))
list1.removeLast()
print(str(list1))
print(list1.getAt(2))
list1.insertAt(1, "Holadenuevo")
print(str(list1))
print(list1.getAt(2))
list1.removeAt(2)
print(str(list1))

#Would it be an error for the function addlast to return none ?? Mostly because if it could be then I can skip conditionals??
#The InsertAt should be able to insert values at the end and beginning of the linked list??
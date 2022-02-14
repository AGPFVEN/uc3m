class SNode:
    def __init__(self, e):
        self.e = e
        self.previous = None
        self.next = None

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
        newNode.next = self.head
        self.head = newNode
        self.size += 1

        if self.size == 0:
            self.tail = newNode

    def removeFirst(self):
        if self.isEmpty():
            print("The list is empty")
        
        result = self.head
        self.head = self.head.next 
        self.size -= 1

        if self.size == 1:
            self.tail = None

    def addLast(self, e):
        #aux = self.head

        #if aux == None:
            #self.addFirst(e)

        #else:
            #while aux.next != None:
                #aux = aux.next

            #aux.next = SNode(e)
              
        #self.size += 1
        result_node = SNode(e)

        if self.tail == None:
            self.addFirst(e)

        else:
            result_node.previous = self.tail
            self.tail = result_node
    
    def removeLast(self):
        result = None

        if self.isEmpty():
            print("List is empty")
            return result
 
        aux = self.head

        if aux == None:
            self.removeFirst()
            return result

        while aux.next.next != None:
            aux = aux.next
            
        aux.next = None
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
 
    def insertAt(self, index, e):
        result = None

        if index == self.size:
            self.addLast(e)

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

            aux_node.next = aux.next
            aux.next = aux_node
            self.size += 1

            return result

    def removeAt(self, index): 
        if index >= self.size:
            print("Invalid index")
 
        aux = self.head

        for _ in range(index -1):
            aux = aux.next

        aux.next = aux.next.next
        self.size -= 1

    def contains(self, a):
        if self.isEmpty():
            print("The list is empty!")
            return None

        aux = self.head
        index_counter = -1

        while aux.e != a or aux != None :
            aux = aux.next
            index_counter += 1

        return 

    def __str__(self):
        result = "list: ["
        aux = self.head

        while aux != None:
            result += str(aux.e)

            if aux.next != None:
                result += ", "
            
            aux = aux.next

        result += "]    size: " + str(self.size) + "    head: " + str(self.head.e) + "      tail: " + str(self.tail)

        return result


#Check implementation of singly linked list
list1 = SList()

list1.addFirst(1)
list1.addFirst(2)
list1.addFirst(5)
print(str(list1))
list1.removeFirst()
print(str(list1))
list1.addLast("hola")
list1.addLast("9")
list1.removeLast()
print(str(list1))
print(list1.getAt(2))
list1.insertAt(0, "Holadenuevo")
print(str(list1))
print(list1.getAt(2))
list1.removeAt(2)
print(str(list1))

#Would it be an error for the function addlast to return none ?? Mostly because if it could be then I can skip conditionals??
#The InsertAt should be able to insert values at the end and beginning of the linked list??
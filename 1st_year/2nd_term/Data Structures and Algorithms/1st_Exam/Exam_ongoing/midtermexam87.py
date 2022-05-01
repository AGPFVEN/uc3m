#Alfonso Pineda

from ast import Slice


class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next

class SList:
  
    def __init__(self):
        self._head=None
        self._size=0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return len(self)==0   

    def __str__(self):
        nodeIt=self._head
        result='['
        while nodeIt:
            if type(nodeIt.elem)==int:
                result+= str(nodeIt.elem)+ ", "
            else:
                result+= "'"+str(nodeIt.elem)+ "', "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result
    
       
    def append(self,e):
        """This functions adds e to the end of the list"""
        if self.isEmpty():
          newNode=SNode(e)
          self._head=newNode
        else:
          newNode=SNode(e)
  
          current=self._head
          while current.next is not None:
            current=current.next
      
          current.next=newNode
          
        self._size=self._size+1

    def reverseDup(self):
        #Special cases
        if (self.isEmpty() == True):
            return None
        
        if self._head.next == None:
            return None
        
        #First we need to declear a valid head to our list
        auxiliar_node = self._head

        #This loop iterates until the next value of the head is different from the head
        while auxiliar_node.elem == auxiliar_node.next.elem:
            auxiliar_node = auxiliar_node.next
            self._head = auxiliar_node
            self._size -= 1

            #This happens when the whole list is the same value
            if (self._head.next == None):
                return None
        
        #Now we want to iterate the rest of the list, know it only has iterated the "head"
        #For that we want to have a variable to iterate the list
        selected_node = auxiliar_node.next

        #This loop iterates the list
        while selected_node != None:
            #Check if it is the end of the list or the next node has the same value of the selected one
            if selected_node.next == None or (selected_node.elem != selected_node.next.elem):
                #My approach to reverse the list is to add new elements at the beggining of the list
                #And when the selected node is the last one disconnect the original list with the auxiliar node
                new_node = SNode(selected_node.elem)
                new_node.next = self._head
                self._head = new_node
            else:
                self._size -= 1

            #Pass to the next value of the list
            selected_node = selected_node.next
        
        print(str(self))
        
        #This node is the head of the original list, so if you disconnect it, you are "deleting all the original values"
        auxiliar_node.next = None

mly = SList()
mly.append(2)
mly.append(3)
mly.append(4)
mly.append(5)
mly.append(7)
mly.append(0)
mly.append(6)
print(str(mly))
mly.reverseDup()
print(mly)
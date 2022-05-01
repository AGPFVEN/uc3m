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
        
      ...
        
class Stack1:
  """LIFO Stack implementation using a Python list as storage. 
  The top of the stack stored at the end of the list."""
  
  def __init__(self):
    """Create an empty stack"""
    self.items=[]
    
  def __len__(self):
    """Return the number of elements in the stack"""
    return len(self.items)
  
  def isEmpty(self):
    """Return True if the stack is empty"""
    return len(self)==0
  
  def __str__(self):
    #print the elements of the list
    return str(self.items)


  def push(self,e):
    """Add the element e to the top of the stack"""
    self.items.append(e)
    
  def pop(self):
    """Remove and return the element from the top of the stack"""
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    return self.items.pop() #remove last item from the list
  
  def top(self):
    """Return the element from the top of the stack"""
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    #returns last element in the list
    return self.items[-1] 

def reverse(word:str):
  result = ""
  stack_ = Stack1()
  for i in word:
    stack_.push(i)

  while stack_.isEmpty() == False:
    result += stack_.pop()

  return result

def parentesis_detector(expression:str):
  stack_ = Stack1()

  for i in expression:
    if (i == "("):
      stack_.push("(")

    if (i == ")"):
      stack_.pop()

  if(stack_.isEmpty() == True):
    return True
    
  else:
    return False
    

print(reverse("long"))

#print('testing Stack1')
#s=Stack1()
#print('isEmpty()',s.isEmpty())
#s.push('W')
#s.push('O')
#print('top element',s.top())
#print('isEmpty()',s.isEmpty())
#s.push('R')
#s.push('D')
#print('Content of stack',str(s))
#print('pop:',s.pop())
#print('Content of stack',str(s))
#print('top element:',s.top())
#print()



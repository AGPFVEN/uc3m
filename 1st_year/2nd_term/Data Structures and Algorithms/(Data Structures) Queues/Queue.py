#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import queue


class Queue:
  """FIFO Queue implementation using a Python list as storage. 
  We add new elements at the tail of the list (enqueue)
  and remove elements from the head of the list (dequeue)."""
  
  def __init__(self):
    """Create an empty queue"""
    self.items=[]
  
  def __len__(self):
    """Return the number of elements in the queue"""
    return len(self.items)
  
  def isEmpty(self):
    """Return True if the queue is empty"""
    #return len(self.items)==0
    return len(self)==0
    #return self.items==[]

  def __str__(self):
    return str(self.items)
  
    
  def enqueue(self,e):
    """Add the element e to the tail of the queue"""
    self.items.append(e)
    
  def dequeue(self):
    """Remove and return the first element in the queue"""
    if self.isEmpty():
      print('Error: Queue is empty')
      return None
    #remove first item from the list
    return self.items.pop(0)
  
  def front(self):
    """Return the first element in the queue"""
    if self.isEmpty():
      print('Error: Queue is empty')
      return None
    
    #returns first element in the list
    return self.items[0]

def JosephusProblem(n, k):
  q_ = Queue()
  
  for i in range(n):
    q_.enqueue(i)

  while len(q_) != 1:
    for i in range(k):
      aux = q_.dequeue()
    
    q_.enqueue(aux)
    
  return str(q_)

print(JosephusProblem(12, 2))

#q=Queue()
#print('isEmpty()',q.isEmpty())
#q.enqueue(5)
#q.enqueue(1)
#q.dequeue()
#q.enqueue(3)
#print('front (first) element',q.front())

#print('Content of queue',str(q))
#print('front (first) element',q.front())
#print('isEmpty()',q.isEmpty())
#print('dequeue():',q.dequeue())
#print('Content of queue',str(q))
#print('front element:',q.front())
#print('size:',len(q))
#print('size:',q.__len__())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from midtermexam import MyDList

import unittest

class Test(unittest.TestCase):
    def setUp(self):
      
      self.x1=0
      self.input=MyDList()
      self.expected1=[7,3,2,10,0,2,8,0,0,4,1,1,10,6,0,3,0,5,3,7]
      
      for e in self.expected1:
        self.input.append(e)

      self.x2=8
      self.expected2=[10,8,10]
      
    
      self.x3=100

    def test_removeSmaller1(self):
      print()
      print('Caso 1: borramos menores que ', self.x1,' en una lista vacía')
      lEmpty=MyDList()
      lEmpty.removeSmaller(self.x1)
      expected=[]
      self.assertEqual(len(lEmpty),0)
      self.assertEqual(str(lEmpty),str(expected))
     
    def test_removeSmaller2(self):
      print()
      print('Caso 2: borrar menores que ', self.x1, ' (no existen)')
      print('Antes de llamar a removeSmaller: ', self.input)
      self.input.removeSmaller(self.x1)
      print('Después:',self.input)
      print('Lista esperada:',self.expected1)
      self.assertEqual(len(self.input),len(self.expected1))
      self.assertEqual(str(self.input),str(self.expected1))

    def test_removeSmaller3(self):
      print()
      print('Caso 3: borrar menores que ', self.x2, ' en la lista')
      print('Antes de llamar a removeSmaller: ', self.input)
      self.input.removeSmaller(self.x2)
      print('Después:',self.input)
      print('Lista esperada:',self.expected2)
      print()
      self.assertEqual(len(self.input),len(self.expected2))
      self.assertEqual(str(self.input),str(self.expected2))


    def test_removeSmaller4(self):
      print()
      print('Caso 4: borrar menores que ', self.x3, '')
      print('Antes de llamar a removeSmaller: ', self.input)
      self.input.removeSmaller(self.x3)
      print('Después:',self.input)
      expected=[]

      print('Lista esperada:',expected)
      print()
      self.assertEqual(len(self.input),0)
      self.assertEqual(str(self.input),str(expected))

    

#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()
    

#Alfonso Pineda

from typing import Tuple
from xml.dom import NoModificationAllowedErr


class MyNode:
    def __init__(self, elem: int, node_left: 'MyNode' = None, node_right: 'MyNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

class MyBST:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def add(self, elem: int) -> None:
        if self._root is None:
            self._root = MyNode(elem)  # if tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                if node.left is None:  # this is the place to insert it
                    node.left = MyNode(elem)
                    not_exist = False
                else:
                    node = node.left
            elif elem > node.elem:
                if node.right is None:  # this is the place to insert it
                    node.right = MyNode(elem)
                    not_exist = False
                else:
                    node = node.right
            elif elem == node.elem:
                print('duplicate elements not allowed!!', elem, node.elem)
                not_exist = False
                
    def remove(self, elem: object) -> None:
      self._root = self._remove(self._root, elem)

    def _remove(self, node: MyNode, elem: object) ->MyNode:
      if node is None:
            print(elem, ' not found')
            return node

      if elem < node.elem:
            node.left = self._remove(node.left, elem)
      elif elem > node.elem:
            node.right = self._remove(node.right, elem)
      else:
            # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                return None
            # Case 2: node only has a child, so the function has to return it
            if node.left is None:
                # It only has the right child
                return node.right
            elif node.right is None:
                # It only has the left child
                return node.left
            else:
                successor = self._minimum_node(node.right)
                node.elem = successor.elem
                node.right = self._remove(node.right, successor.elem)

      return node

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n')

    def _draw(self, prefix: str, node: MyNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True) 

    def isFullBinary(self) -> bool:
        """Returns True if the tree is a Full Binary tree. 
        Returns False otherwise.
        A full binary tree is defined as a binary tree in which all nodes
        have either zero or two child nodes. """
        return self._isFullBinary(self._root)

    def _isFullBinary(self, node: MyNode) -> bool:
        if (node.left != None and node.right == None) or (node.left == None and node.right != None):
            return False
        elif node.right == None and node.left == None:
            return True
        elif node.right != None and node.left != None:
            return self._isFullBinary(node.left) and self._isFullBinary(node.right)
        print("ENters")

if __name__ == "__main__": 
    #case full binary tree True
    tree = MyBST()
    for x in [46, 11, 81, 51, 56, 94, 5, 20,49]:
        tree.add(x)

    tree.draw()
    
    print (tree.isFullBinary())
    print()
    
    #case full binary tree False
    tree = MyBST()
    for x in [46, 11, 81, 51, 56, 94, 5, 20]:
        tree.add(x)

    tree.draw()
    
    print (tree.isFullBinary())
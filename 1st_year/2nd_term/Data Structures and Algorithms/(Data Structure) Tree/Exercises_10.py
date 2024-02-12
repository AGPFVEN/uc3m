from itertools import count
from typing import List

from numpy import binary_repr
from binarytree import BinaryTree, Node

#Take as input a an ordered array (ascendent order) and tranform it to a balanced binary search tree
def array2bst(input: list):
    middle = len(input)


ar = [1, 2, 3, 4, 5, 6, 7]
mid = int(len(ar) / 2)
print(ar[mid])
print(ar[:mid])
print(ar[mid + 1:])
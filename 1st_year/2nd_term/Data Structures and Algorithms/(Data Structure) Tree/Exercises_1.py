from binarytree import Node
from binarytree import BinaryTree

nodeD = Node("A")
nodeB = Node("B")
nodeA = Node("C")
nodeC = Node("D")
nodeE = Node("E")

nodeD.left = nodeB
nodeD.right = nodeE
nodeB.left = nodeA
nodeB.right = nodeC

nodeB.parent = nodeD
nodeE.parent = nodeD
nodeC.parent = nodeB
nodeA.parent = nodeB

myTree = BinaryTree()
myTree._root = nodeD
myTree.draw()
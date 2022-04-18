# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode

class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root=self._insert(self._root,elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        if node == None:
            return None

        """ gets node and balances it"""
        left_original = node.left
        right_original = node.right
        difference_heights = self._height(right_original) - self._height(left_original)
        balance_factor = 1

        #Balanced tree
        if abs(difference_heights) > balance_factor:
            tree_balanced = AVLTree()
            auxiliar_tree = None

            #Left Rotations
            if difference_heights > balance_factor:
                #Simple
                if self._height(right_original.right) > self._height(right_original.left):
                    auxiliar_tree = node.right.left
                    tree_balanced._root = right_original
                    tree_balanced._root.left = node
                    tree_balanced._root.left.right = auxiliar_tree
                
                #Double
                else:
                    tree_balanced._root = right_original.left
                    auxiliar_tree = right_original.left.left
                    tree_balanced._root.left = node
                    tree_balanced._root.right = node.right
                    tree_balanced._root.left.right = None
                    tree_balanced._root.right.left = None

            #Right Rotations
            else:
                #Simple
                if self._height(left_original.left) > self._height(left_original.right):
                    auxiliar_tree = node.left.right
                    tree_balanced._root = left_original
                    tree_balanced._root.right = node
                    tree_balanced._root.right.left = None

                #Double
                else:
                    tree_balanced._root = left_original.right
                    tree_balanced._root.left = left_original
                    tree_balanced._root.right = node
                    tree_balanced._root.left.right = None
                    tree_balanced._root.right.left = None

            return tree_balanced._root
        
        else:
            node.left = self._rebalance(node.left)
            node.right = self._rebalance(node.right)

            return node

"""  remove(8), 7 is unbalanced, right rotation with subtrees """
avl = AVLTree()
data = [17, 8, 12, 2, 7, 27, 48, 58, 3, 4]
for n in data:
    avl.insert(n)
     avl.draw()

# we remove 8 (root), it will be replaced with 7
avl.remove(8)  # root
avl.draw()

data = [12, 3, 27, 2, 7, 17, 48, 4, 58]
expected = BinarySearchTree()
for n in data:
    expected.insert(n)
expected.draw()
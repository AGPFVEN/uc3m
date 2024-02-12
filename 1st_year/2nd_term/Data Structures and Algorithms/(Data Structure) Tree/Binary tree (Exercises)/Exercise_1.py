from ..binarytree import BinaryTree, Node

def smallest_value_tree(selected_node: Node):
    if selected_node.right == None and selected_node.left == None:
        return selected_node.elem
    elif selected_node.right == None:
        return min(selected_node.elem, smallest_value_tree(selected_node.left))
    elif selected_node.left == None:
        return min(selected_node.elem, smallest_value_tree(selected_node.right))
    else:
        return min(selected_node.elem, smallest_value_tree(selected_node.left), smallest_value_tree(selected_node.left))
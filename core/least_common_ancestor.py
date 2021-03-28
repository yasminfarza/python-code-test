# A program to find least common ancestor of two nodes
class Node:
    # Constructor for creating new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, node1, node2):

    # If root is None return None
    if root is None:
        return None

    # If any node match with root,
    # So this root value is the LCA
    if root.data == node1 or root.data == node2:
        return root

    # Check value in left and right subtrees
    left_lca = lca(root.left, node1, node2)
    right_lca = lca(root.right, node1, node2)

    # If both of the above value is not None
    # So this root value is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

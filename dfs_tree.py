class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Pre-order Traversal: Root -> Left -> Right
def get_preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.val)
        get_preorder(node.left, result)
        get_preorder(node.right, result)
    return result


# In-order Traversal: Left -> Root -> Right
def get_inorder(node, result=None):
    if result is None:
        result = []
    if node:
        get_inorder(node.left, result)
        result.append(node.val)
        get_inorder(node.right, result)
    return result


# Post-order Traversal: Left -> Right -> Root
def get_postorder(node, result=None):
    if result is None:
        result = []
    if node:
        get_postorder(node.left, result)
        get_postorder(node.right, result)
        result.append(node.val)
    return result


if __name__ == "__main__":
    print("==========================================")
    print("Assessment 3.6: DFS Method in Tree")
    print("Name: Villarino, Daniel | BSIT - 2C")
    print("==========================================\n")

    # Constructing the binary tree based on Assessment 3.5 diagram
    root = Node('D')

    # Level 1
    root.left = Node('A')
    root.right = Node('N')

    # Level 2
    root.left.left = Node('I')
    root.left.right = Node('E')
    root.right.left = Node('L')
    root.right.right = Node('V')

    # Level 3 (Leaves/Sub-leaves)
    root.left.left.left = Node('I')
    root.left.left.right = Node('L')

    root.left.right.left = Node('L')
    root.left.right.right = Node('A')

    root.right.left.left = Node('R')
    root.right.left.right = Node('I')

    root.right.right.left = Node('N')
    root.right.right.right = Node('O')

    print("PREORDER :", ", ".join(get_preorder(root)))
    print()
    print("INORDER  :", ", ".join(get_inorder(root)))
    print()
    print("POSTORDER:", ", ".join(get_postorder(root)))
    print()
#Binary Search Tree: node based tree structure with properties such as
# left subtree of node contains only nodes with key less than the node's
# Right subtree conatines nodes greater than node's key
# Left and Right subtree each must be also binary tree.

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

def search(root,key):
    if root is None or root.key == key:
        return root
    if root.key > key:
        return search(root.right, key)
    return search(root.left, key)

#if key is grater than node recursively search in right subtree else search in left subtree
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root

#while deleting node if node is leaf simply remove, if node has only one child
#copy child into node and delete child, if node has two children then find the inorder
#successor, copy the inorder successor into the node and delete successor.

def minValue(node):
    current = node
    while(current.left is not None):
        current = current.left
    
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValue(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right,temp.key)
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def minValue(node):
    current = node

    while(current.left is not None):
        current = current.left

    return current.key

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
print ("Inorder traversal of the given tree")
inorder(root)

root = deleteNode(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)
print(minValue(root))
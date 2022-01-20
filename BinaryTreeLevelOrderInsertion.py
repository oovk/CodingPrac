""" If we find a node whose left child is empty, 
we make new key as left child of the node. 
Else if we find a node whose right child is empty, 
we make the new key as right child. We keep traversing the 
tree until we find a node whose either left or right child is empty.
 """

from curses import keyname
from logging import root


class Node():
    def __init__(self,data):
        self.right = None
        self.left = None
        self.val = data

def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.val, end=" ")
    inorder(temp.right)

def insert(temp,key):
    if not temp:
        root = Node(key)
        return
    q = []
    q.append(temp)

    while (len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    print("inorder traversal before insertion", end=" ")
    inorder(root)

    key = 12
    insert(root,key)
    print()
    print("Inorder traversal after insertion",end=" ")
    inorder(root)
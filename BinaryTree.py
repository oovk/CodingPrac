#Trees are hierarchical datastructures unlike linear datasturctures such as arrays, linkelists
#Top most node is called root node
#Elements that are directly under an element are called its children
#Elements directly above something are called parents.
#Elements with no childern are called leaves
#Useful for quicker search, easy insertion/deletion.
#A tree whose elements have at most two childern called binary tree.
#Types: Full binary tree(every node has 0 or 2 children), Complete binary tree(all the levels are completely filled except possibly the last level)
# Perfect binary tree(all the internal nodes have two children and all leaf nodes are at the same level), Balanced binary tree(balanced if the height of the tree is O(Log n) where n is the number of nodes) 



class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.printTree()
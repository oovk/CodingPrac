#both the left and right part of tree is similar ie mirror trees
#left subtree of tree1 is similar to right subtree of second one and right subtree of first one is similar to left subtree of second one
#we usually use recursion on left and right trees

def are_symmetrice(root1, root2):
    if root1 in None and root2 is None:#when both are Null
        return True
    elif ((root1 is None)!= (root2 is None)) or root1.val != root2.val:#when one of them is null and other is not and values at root are not equal then return false 
        return False
    else:
        return are_symmetrice(root1.left, root2.right) and are_symmetrice(root1.right, root2.left)

def is_symmetric(root):
    if root is None:
        return True
    return are_symmetrice(root.left, root.right)


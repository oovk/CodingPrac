#Stack is a linear data sturcture. Follows LIFO(last in first out). There are three basic methods push,pop,peek or top and isEmpty.
# Time complexity is O(1)
#Applications: balacing symbols, undo-redo, infix-postfix-prefix,memory management
#Two ways to implement stack - Using Array, Using LinkedList

""" from inspect import stack
from sys import maxsize

from LinkedList import Node


def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item + " pushed to stack")

def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1)
    return stack.pop()

def peek(stack):
    if(isEmpty(stack)):
        return str(-maxsize -1)
    return stack[len(stack)-1]

stack = createStack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
print(pop(stack) + " popped from stack")
print(stack)
 """

# Stack using linked list

class stackNode():

    def __init__(self,data):  #constructor to initialize a node
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self): #constructor to initialize the root of linked list 
        self.root = None
    
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            False
    def push(self,data):
        newNode = stackNode(data)
        newNode.next = self.root #new node becomes the top of the stack ie root/head node of linkedlist
        self.root = newNode
        print(data," Pushed to stack")

    def pop(self):
        if(self.isEmpty()):
            return float("-inf") #negative infinity
        else:
            temp = self.root
            self.root = self.root.next
            popped = temp.data
            return popped
    
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print("-----")
print((stack.pop())," popped from the stack")
print(stack)
print("-----")
print((stack.peek()),"is top element")
print("-----")
print(stack)
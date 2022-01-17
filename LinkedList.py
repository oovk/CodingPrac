#Linked List: The elements are not stored continously. They are connected via pointers. It has dynamic size and easy insertion and deletion.
#Time complexity of insert,delete at any position - O(1)
# Time complexity of accessing ith element, traverse all the elements - O(n) 


class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    
    #This function adds new node to the front of linked list
    def push(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    #This function inserts a node after a certain node
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("the given node must be available in linked list")
            return
        else:
            new_node = Node(new_data) #creating a node with new data
            new_node.next = prev_node.next #make new node as next of prev node
            prev_node.next = new_node #make next of prev node as new node

    #This function adds the node at the end of linked List
    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node

    def deleteNode(self,key):
        temp = self.head
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if(temp==None):
            return

        prev.next = temp.next

        temp = None

    def deleteNodeatPosition(self,position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
 
    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
 
    llist.append(4)
    llist.push(5)
    llist.append(6)
    llist.push(7)
    
    llist.insertAfter(llist.head.next.next, 8)
    llist.printList()
    llist.deleteNode(8) 
    print("------")
    llist.printList()
    llist.deleteNodeatPosition(0)
    print("------")
    llist.printList()

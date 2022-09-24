class node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node Data: %s>" % self.data


class Linked_List:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = node(data)
        new_node.next_node = (self.head)  # so that we don't loose the curent head of linked list
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):  # inserting node at a position takes constant time but finding a index where we wanna insert takes O(n) time
        if index == 0:
            self.add(data)
        if index > 0:
            new = node(data)  # create a node with data

            position = index
            current = self.head

            while position > 1:
                current = (current.next_node)  # traverse the node until position becomes 1 i.e right before inserting position
                position -= 1

            prev_node = current  # point index - 1nth node to prev
            next_node = current.next_node  # point the next node to (index-1)nth.next

            prev_node.next_node = new  # make new node as (index-1)nth nodes next
            new.next_node = next_node  # make new_node.next point to (index-1)nth.next

    def remove(self,key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if key == current.data and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key: #if node.data contains a key
                found = True
                previous.next_node = current.next_node
            else: #if node does not contain a key then set prev to current and current to next
                previous = current
                current = current.next_node

        return current #return the removed item

    def removeatindex(self, index):
        count = None
        current = self.head
        previous = None

        while current:
            count += 1
            previous = current
            current = current.next_node
            if count == index:
                previous.next_node = current.next_node
        
        return count        

    def nodeatindex(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            
            return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head is: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail is: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "->".join(nodes)

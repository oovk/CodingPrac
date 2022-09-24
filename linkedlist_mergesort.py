from linkedlist import Linked_List

def mergesort(linkedlist):
    
    if linkedlist.size() == 1:
        return linkedlist
    
    elif linkedlist.head is None:
        return linkedlist

    left, right = split(linkedlist)
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def split(linkedlist):
    if linkedlist == None or linkedlist.head is None:
        left = linkedlist
        right = None

        return left, right
    else:
        size = linkedlist.size()
        mid = size // 2 

        mid_node = linkedlist.nodeatindex(mid - 1)
        left = linkedlist
        right = Linked_List()
        right.head = mid_node.next_node
        mid_node.next_node = None
    
    return left, right


def merge(left, right):
    merged = Linked_List
    merged.add(0)
    current = merged.head
    right_head = right.head
    left_head = left.head

    while left_head or right_head:
        if left.head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right.head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
        if left_data < right_data:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            current.nect_node = right_head
            right_head = right_head.next_node    
    
    current = current.next_node
    head = merged.head.next_node
    merged.head = head

    return merged


l = Linked_List()
l.add(10)
l.add(47)
l.add(67)
l.add(54)

print(l)
sorted_linked_list = mergesort(l)
print(sorted_linked_list)
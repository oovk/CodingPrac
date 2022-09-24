def mergesort(list):
    if len(list) <=1 :
        return list
    
    left, right = split(list)
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def split(list):
    mid = len(list)//2
    left = list[:mid]#without including a midpoint
    right = list[mid:] #including mid point

    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1 

    while i < len(left): #when one is bigger than other then simply append rest elements
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1    
    
    return l

def verify_sorted(list):
    l = len(list)

    if l == 0 or l == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])#checking the rest of list again and again


alist = [54, 26, 96, 12, 80,57]
l = mergesort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
def binary_srch(list, target):
    first = 0
    last = len(list) - 1
    while(first<=last):
        mid = (first + last) // 2

        if list[mid]==target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None

def verify(index):
    if index is not None:
        print("Targate found at index ", index)
    else:
        print("not found")

numbers = [1,2,3,4,5,6,78,88,8,8,8,6,3]
result = binary_srch(numbers, 78)
verify(result)
 


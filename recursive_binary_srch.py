import re


def recursive_binary_srch(list, target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list))//2

        if list[mid] == target:
            return True
        elif list[mid] < target:
            return recursive_binary_srch(list[mid+1:],target)
        else:
            return recursive_binary_srch(list[:mid-1],target)

def verify(result):
    print("target found: ", result)


numbers = [1,2,3,4,5,6,78,88,8,8,8,6,3]
result = recursive_binary_srch(numbers, 78)
verify(result)
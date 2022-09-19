def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Targate found at index ", index)
    else:
        print("not found")

numbers = [1,2,3,4,5,6,78,88,8,8,8,6,3]
result = linear_search(numbers, 78)
verify(result)

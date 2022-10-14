#Given array of integers and an integer k find the kth largest element.
# eg. arr = [4, 2, 9, 7, 5, 6, 7,1,3], k=4
# the 4th largest element is 6 solution is to remove maximum element 4 times
""" 
def kthlargest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)
    
arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
print(kthlargest(arr, k))
 """
#Using sorting
""" 
def sortedkthlargest(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
print(sortedkthlargest(arr, k)) """

#using max heap costs log(n) only
# in python we have heapq module but implemented with min heap only

import heapq

def kth_largest(arr, k):
    arr = [-elem for elem in arr]#makeing each element negative
    heapq.heapify(arr)#heapyfying array
    for i in range(k-1):
        heapq.heappop(arr)#popping k-1 times
    return -heapq.heappop(arr)#returning the kth largest element

arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
print(kth_largest(arr, k))
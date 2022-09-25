#Randomizes the order of the list until its sorted O(n!) really bad algorithm
import numbers
import random

def is_sorted(values):
    for i in range(0, len(values)-1):
        if values[i] > values[i+1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values

numbers = [0, 4,6,7,3,28, 1,2]
print(bogo_sort(numbers))
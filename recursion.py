def sum(list):
    if not list: # A base case when we reach last item and sum(list[n:]) returns empty list causing error in recursive call
        return 0
    return list[0] + sum(list[1:])

numbers = [1, 9, 7, 2]
print(sum(numbers))
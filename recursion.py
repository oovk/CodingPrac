def sum(list):
    if not list: # A base case when we reach last item and sum(list[n:]) returns empty list causing error in recursive call
        return 0
    print("Calling sum(%s)" % list[1:])
    print("Call to sum(%s) returning %d + %d" % (list, list[0], sum(list[1:])))
    return list[0] + sum(list[1:])

numbers = [1, 9, 7, 2]
print(sum(numbers))
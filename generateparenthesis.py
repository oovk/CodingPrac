#given an integer n generate all valid combinations of n pairs of parentheses
#valid if each opening parenthesis has a closing parenthesis

#check if its valid

def is_valid(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff += 1 #increase value if it is opening parenthesis
        else:
            if diff == 0: #difference should be zero
                return False
            else:
                diff -= 1 #reduce the value if it is closing parathesis
    return diff == 0 #stack must be empty at the end

#using stack(((()))))
def valid(combination):
    stack = []
    for par in combination:
        if par == "(":
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
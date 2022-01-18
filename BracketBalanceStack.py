def areBracketBalanced(expr):
    stack = []

    for char in expr:
        if char in ['[','{','(']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    #for loop check each element if it is opening brac then add to stack
    #else check if it is closing if it is closing pop it out of stack
    if stack:
        return False
    return True
            
if __name__ == "__main__":
    expr = "{()}["

    if areBracketBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
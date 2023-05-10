def is_valid_paraetheses(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != "(":
                return False
    return len(stack) == 0

s =["(((()))((()()()()))((()()((())))))"]

if is_valid_paraetheses(s):
    print("Valid parentheses")
else:
    print("Invalid parentheses")






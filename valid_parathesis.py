#Valid Parathesis
def isValidstr(stack):
    stack=[]
    mapping={')':'(',']':'[','}':'{'}
    for char in stack:
        if char in mapping:
            top_element=stack.pop() if stack else '#'
            if top_element==mapping[char]:
                return False
            else:
                stack.append(char)
        return not stack
#test
isValidstr("()[]{}")
isValidstr("([)]")

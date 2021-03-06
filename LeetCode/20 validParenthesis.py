# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.

def isValid( s) -> bool:
        stack = []
        
        for char in s:
            if (char == '(' or char == '[' or char == '{'):
                stack.append(char)
            else:
                if (char == ')'):
                    if(len(stack) == 0 or stack[-1] != '(' ):
                        return False
                    else:
                        stack.pop()
                
                if (char == '}'):
                    if(len(stack) == 0 or stack[-1] != '{'):
                        return False
                    else:
                        stack.pop()
                
                if (char == ']'):
                    if(len(stack) == 0 or stack[-1] != '['):
                        return False
                    else:
                        stack.pop()
                
        if(len(stack) != 0):
            return False
        
        return True

print(isValid('()'))
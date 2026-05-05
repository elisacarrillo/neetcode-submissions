class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for real_i, i in enumerate(s):
            print("HERE")
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                print("IN STACK: " + i)
            
            if i == ')' or i == '}' or i == ']':
                
                if (len(stack) == 0):
                    return False
                to_check = stack.pop()
                print("POPPED: " + to_check)
                if to_check == '(' and i != ')':
                    return False
                elif to_check == '[' and i != ']':
                    return False
                elif to_check == '{' and i != '}':
                    return False
        if (len(stack) > 0):
            return False
        return True

        
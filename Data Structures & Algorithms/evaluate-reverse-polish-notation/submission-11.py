class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for t in tokens:
            if (t == "+"):
                val1 = stack.pop(-1)
                val2 = stack.pop(-1)
                total = val1 + val2
                stack.append(total)
                print(f'{val1} + {val2}= {total}')
                print(total)
            elif (t == "*"):
                val1 = stack.pop(-1)
                val2 = stack.pop(-1)
                total = val1 * val2
                stack.append(total)
                print(f'{val1} * {val2} = {total}')
                print(total)
            elif (t == "-"):
                # stack.pop()
                
                val1 = stack.pop(-1)
                val2 = stack.pop(-1)
                print(f'{val2} - {val1}= {total}')
                total = val2 - val1
                stack.append(total)
                print(total)
            elif (t == "/"):
                
                val1 = stack.pop(-1)
                val2 = stack.pop(-1)

                total = int(val2 / val1)
                print(f'{val2} // {val1}= {total}')
                stack.append(total)
                print(total)
            else:
                print(f'adding {t}')
                stack.append(int(t))

        print(len(stack))
        return stack[-1]
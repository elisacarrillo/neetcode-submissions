class MinStack:

    def __init__(self):
        
        self.stack = []
        

    def push(self, val: int) -> None:
        print("push")
        self.stack.append(val)
        

    def pop(self) -> None:
        print("pop")
        self.stack.pop()

    def top(self) -> int:
        print("top")
        return self.stack[-1]
        

    def getMin(self) -> int:
        print("getmin")
        sorted_stack = sorted(self.stack)
        print(sorted_stack[0])
        return sorted_stack[0]
        

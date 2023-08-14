# 59ms (Beats 90% of users) / 20mb (Beats 48% of users)
# There's not really a lot of different ways to do this one and the methods are all pretty self explanatory
class MinStack:
    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minimumStack[-1] if self.minimumStack else val)
        self.minimumStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimumStack[-1]

def main():
    obj = MinStack()
    for i in range(100):
        obj.push(i)
    print(obj.top())
    print(obj.getMin())


main()
# 76ms (Beats 76% of users) / 16mb (Beats 84% of users)
# After understanding the problem it became really easy 
# Loop through the list of values, and whenever you come by an operand you have to do whatever that operand says 
# The values you take in are the second to last value in the stack and the last value in the stack respectively
# Then all you have to do is reinsert that back into the second to last value of the stack and pop the last value in the stack
# Once you're at the end just return the only number left in the stack
def evalRPN(tokens: list[str]) -> int:
    if len(tokens) == 1:
        return int(tokens[0])
    stack = [] 
    for value in tokens:
        if value == '+':
            stack[-2] = int(stack[-2]) + int(stack[-1])
            stack.pop()
        elif value == '-':
            stack[-2] = int(stack[-2]) - int(stack[-1])
            stack.pop()
        elif value == '*':
            stack[-2] = int(stack[-2]) * int(stack[-1])
            stack.pop()
        elif value == '/':
            stack[-2] = int(int(stack[-2]) / int(stack[-1]))
            stack.pop()
        else:
            stack.append(value)
    return stack[0]

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


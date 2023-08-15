# Done recursively answer taken from Neetcode people cause I couldn't solve it
# Basically the idea is to keep track of how many open and closed parethesis there are
# If you know how much of each there are you can tell whether it's appropriate to add an open or a closed parenthesis
# Basically you only want to increment the amount of open parenthesis if the amount of open parenthesis is less than there
# can be (represented by the integer n). You only want to add closed parenthesis if the amount of open parenthesis is greater
# than the number of closed parenthesis 
# it's crucial that at the start of the recursive function there is an if checking for the end condition which is when the
# amount of closed and open parenthesis both equal the integer n.

def generateParenthesis(n: int) -> list[str]:
    stack = []
    res = []

    def backtrack(openParen, closedParen):
        if openParen == closedParen == n:
            res.append("".join(stack))
            return
        if openParen < n:
            stack.append("(")
            backtrack(openParen+1, closedParen)
            stack.pop()
        if closedParen < openParen:
            stack.append(")")
            backtrack(openParen, closedParen + 1)
            stack.pop()
    backtrack(0,0)
    return res


print(generateParenthesis(1))
print(generateParenthesis(2))
print(generateParenthesis(3))
print(generateParenthesis(4))

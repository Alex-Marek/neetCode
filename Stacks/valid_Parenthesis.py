# 33 ms (Beats 96.8% of users) / 16.3 mb (Beats 85% of users)
# Create a dict with the closed values in the keys spot and the opening values in the values position, and an empty stack
# Loop through the string, if the value isn't a key in the i_Values (Meaning it's an opening parenthesis) then append it to the stack
# Then continue to skip the remaining code in the for loop
# Have a secondary if statement which should cover all situations in which the program ought to return False
# If the stack is empty or the value at the back of the tack isn't equivalent to it's opening bracket coorespondence then
# return False
# Once the for loop is over return the inverse of whether the stack has values or not
# If it does have values then the Not changes the True to a False because all the parenthesis haven't been handled
# If it doesn't have values then the Not changes the False to a True because an empty List means all the parenthesis have been
# handled validly
def isValid(s: str) -> bool:
    i_Values = {")": "(", "]": "[", "}": "{"}
    stack = []
    for value in s:
        if value not in i_Values:
            stack.append(value)
            continue
        if not stack or stack[-1] != i_Values[value]: 
            return False
        stack.pop()
    return not stack

print(isValid("()"), "Expected True")
print(isValid("()[]{}"), "Expected True")
print(isValid("(]"), "Expected False")


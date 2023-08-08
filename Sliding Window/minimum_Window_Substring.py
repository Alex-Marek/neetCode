# Can confirm that there is an answer with a simple and operation
# Once I know there is an answer then we have to figure out how to get it
# Otherwise return false

# To get it we should assume there is a valid character at the starting and the ending point 
# Find the closest valid character to the start and end of the string and then check if the string is valid
# if it is valid then we have to try and find a smaller one inside of that string
# If we want to check if there's a smaller one inside decrement the right most pointer first
# if there is still one keep doing that until there isn't then store that value
# After that do the same thing with the left one 
# do a min of both of those values for the resolution
def checkIfHasSubstring(count1 = [], count2 = []):
    count3 = [0] * 56
    num = 0
    for x,y in zip(count1,count2):
        if x >= 1 and y >= 1 and x >= y:
            count3[num] = count2[num]
        else:
            count3[num] = 0
        num += 1
    if count3 != count2:
        return False
    else:
        return True



def minWindow(s: str, t: str) -> str:
    if t == s:
        return t
    res = 100000
    validChars = []
    l,r = 0, 0
    s_Count = [0] * 56
    t_Count = [0] * 56
    for value in s:
        s_Count[(ord(value) - ord("A"))] += 1
    for value in t:
        if value not in validChars:
            validChars.append(value)
        t_Count[(ord(value) - ord("A"))] += 1
    
    if not checkIfHasSubstring(s_Count, t_Count):
        return ""
    
    for value in validChars:
        l = min(s.find(value), l)
    for value in validChars:
        r = max(s.rfind(value), r)

    while checkIfHasSubstring(s_Count, t_Count):
        s_Count[(ord(s[r-1:r]) - ord("A"))] -= 1
        r -= 1
    r += 1
    while checkIfHasSubstring(s_Count, t_Count):
        s_Count[(ord(s[l:l+1]) - ord("A"))] -= 1
        l += 1
    print(l,r)
    
    # if s.count(s[l:l+1]) >= s.count(s[r:r-1]):

print(minWindow("ADOBECODEBANC", "ABC"), "Was expecting BANC")
# print(minWindow("a", "a"), "Was expecting a")
# print(minWindow("a" , "aa"), "Was expecting a blank string")

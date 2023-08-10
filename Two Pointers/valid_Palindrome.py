# 40m 38 ms (Beats 99.54%) / 17 mb (Beats 58%)
# This took way longer than it should have, I misread the directions and thought it wanted me to remove numbers too
# That took up most of the time honestly

# An easy way to find out if a word is a palindrome is just to divide it in two and compare the first half and the second half
# If it has an even number of characters then you can compare direction, if it has an odd you have to ignore the middle char

# Updated to be significantly more readable 39 ms (Beats 98.71% of users) / 17mb (Beats 25% of users)
def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()
    if len(s) == 0:
        return True

    w_Len = len(s) / 2
    first_Half = s[:int(w_Len)][::-1]
    if len(s) % 2 == 0:
        second_Half = s[int(w_Len):]
    else:
        second_Half = s[int(w_Len)+1:]

    if first_Half == second_Half:
        return True
    return False
    
print(isPalindrome("a."))
print(isPalindrome("abb"))
print(isPalindrome("a"))
print(isPalindrome("0P"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
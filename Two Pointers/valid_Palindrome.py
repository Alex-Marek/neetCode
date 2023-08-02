# 40m 38 ms (Beats 99.54%) / 17 mb (Beats 58%)
# This took way longer than it should have, I misread the directions and thought it wanted me to remove numbers too
# That took up most of the time honestly

# An easy way to find out if a word is a palindrome is just to divide it in two and compare the first half and the second half
# If it has an even number of characters then you can compare direction, if it has an odd you have to ignore the middle char

def isPalindrome(s: str) -> bool:
    #Cleanup 
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()
    # Sanity Check
    if len(s) == 0:
        return True
    if len(s) % 2 == 0:
        w_Len = len(s) / 2
        first_Half = s[:int(w_Len)]
        second_Half = s[int(w_Len):]
        if first_Half == second_Half[::-1]:
            return True
        else:
            return False
    else:
        w_Len = len(s) / 2
        first_Half = s[:int(w_Len)]
        second_Half = s[int(w_Len)+1:]
        if first_Half == second_Half[::-1]:
            return True
        else:
            return False
    
print(isPalindrome("a."))
print(isPalindrome("abb"))
print(isPalindrome("a"))
print(isPalindrome("0P"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
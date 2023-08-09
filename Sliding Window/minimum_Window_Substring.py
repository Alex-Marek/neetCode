# Wasn't able to solve by myself
# This program creates two dictionaries, one of the key letters in the substring word and their amounts, and another for the
# letters that are found in the current window stored with their amounts
# Until it finds all the letters needed in their appropriate amounts it will continue moving the right pointer 
# Once it has found all the letters in their correct amounts it stores the length and indexes of substring
# After this it begins moving the left pointer forward until the requirement is not met anymore if it successfully
# moves the left pointer and still meets requirements it will of course store the length and index of the substring
# Once the requirement isn't met again it will begin incrementing the right pointer again until it finds another time where 
# the requirement is met at which point it will start moving the left pointer again until we are at the end of the array
# At which pointer it sets l and r to the resolution and returns that value assuming the length isn't infinity which'd return ""

def minWindow(s: str, t: str) -> str:
    if t == "": 
        return ""
    countT, window = {}, {}
    
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have,need = 0,len(countT)
    res, resLength = [-1,-1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c,0)
        
        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            if (r-l+1) < resLength:
                res = [l,r]
                resLength = (r-l+1)

            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l,r = res
    return s[l:r+1] if resLength != float("infinity") else ""

 
        


    


print(minWindow("ADOBECODEBANC", "ABC"), " Was expecting BANC")
print(minWindow("a", "a"), " Was expecting a")
print(minWindow("a" , "aa"), " Was expecting a blank string")

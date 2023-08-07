# Solution from neetcode 
# Code works by looping through the whole length of the word, every loop it is going to add to the dictionary a count of each
# specific letter
# After that it will check if the right pointer - the left pointer(+1) then subtracting the count of the most frequent character
# if that is greater than k then it means the window isn't valid anymore and we need to move on so we move our left pointer
# while of course making sure to decrement whatever the left most character is from our dict since there is now one less of it
def characterReplacement(s: str, k: int) -> int:
    count = {}
    
    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

    return (r - l + 1)

print(characterReplacement("ABAB",2))
print(characterReplacement("AABABBA",1))

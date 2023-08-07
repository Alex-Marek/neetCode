def characterReplacement(s: str, k: int) -> int:
    # Find the letter that occurs most
    maxNum = 0
    maxLetter = "A"
    for value in s:
        if s.count(value) > maxNum:
            maxLetter = value
            maxNum = s.count(value)
    print(maxLetter)


    # Get the position of the largest string of that letter
    res = 0
    longestL, longestR = 0,0
    l,r = 0, 0
    while r <= len(s):
        curLength = len(set(s[l:r]))
        if curLength >= len(s[l:r]) and s[l:l+1] == maxLetter:
            if max(res, curLength) > res:
                longestL = l
                longestR = r - 1
                res = curLength
            r += 1
        else:
            l += 1
    print(s[longestL:longestR])
    print(longestL, longestR)

print(characterReplacement("ABAB",2))
print(characterReplacement("AABABBA",1))

# 141 ms (Beats 20% of users) / 16.40 mb (Beats 80% of users)
# Solution is basically loop through from right to left if the set of chars is smaller than the non-set chars then increment
# the left side by one. At the end of every loop check if the length of the current set of characters is the largest yet
# By the time you reach the end of the loop you'll have a solution
def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    l,r = 0, 1
    while r <= len(s):
        curLength = len(set(s[l:r]))
        if curLength < len(s[l:r]):
            l += 1
        r += 1
        res = max(res, curLength)
    return res


print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
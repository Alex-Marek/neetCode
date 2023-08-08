# 68ms (Beats 90% of users) 16.28mb (Beats 98.50% of Users)
# This code is disgusting
# Immediately return False if s1 is longer than s2 because that means s1 can't be a permutation of s2
# Otherwise create two arrays representing the entire alphabet initialized to 0
# Create two pointers l (left) and r (right) l initialized to 0 because that is the start of the string r initialized to 
# the length of string1 because that well set our window to the size of the entirely of string1 which is important for this
# method of checking permutations
# After this load up the arrays with their letters using for loops to go through each of the words appropriately
# Check if they are the same then we already have our permutation found which means the program should return True
# loop through string2 while the right pointer is less than the length of string2 to ensure we get through the whole word
# If both the arrays aren't the same it means we need to remove the furthest left character and take in the one after
# the furthest to the right. We also need to make sure to remove these from the array to keep an appropriate count
# After that operation occurs check to make sure if they're the same (if they are return true)
# If the loop finishes without finding a permutation then return false because there are no permutations in string2
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1_Count = [0] * 26
    s2_Count = [0] * 26
    l,r = 0,len(s1)

    for character in s1:
        s1_Count[(ord(character) - ord("a"))] += 1
    for character in s2[l:r]:
        s2_Count[(ord(character) - ord("a"))] += 1
    if s2_Count == s1_Count:
        return True

    while r < (len(s2)):
        if s2_Count != s1_Count:
            l += 1
            r += 1
            s2_Count[(ord(s2[l-1:l]) - ord("a"))] -= 1
            s2_Count[(ord(s2[r-1:r]) - ord("a"))] += 1
            if s2_Count == s1_Count:
                return True
        else:
            return True
    return False

print(checkInclusion("ab", "eidbaooo"), "Was expecting True")
print(checkInclusion("ab", "eidboaoo"), "Was expecting False")
print(checkInclusion("a", "ab"), "Was expectiing True")
print(checkInclusion("adc", "dcda"), "Was expecting True")
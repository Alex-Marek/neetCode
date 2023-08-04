# 54ms (Beats 91%)/ 16mb (Beats 65%)
# Initially checks to see if the two words are the same length becauses if they're not then they can't be an anagram
# Creates a dict and populates it with all the letters and their cooresponding amounts
# Runs through the list of the potential anagram subtracting from the dict if it finds a letter they both have
# Loops through the dict checking for any values greater than 0, if one is found then it means there was an excess letter
# and therefore cannot be an anagram
def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
              return False
        o_Word = {}
        for letter in s:
            if letter in o_Word:
                  o_Word[letter] += 1
            else:
                  o_Word[letter] = 1
        for letter in t:
            if letter in o_Word:
                  o_Word[letter] -= 1
        for value in o_Word:
              if o_Word[value] > 0:
                    return False
        return True
                

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))
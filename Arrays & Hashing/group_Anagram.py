#Loop through the list of potential anagrams checking each word against each entry

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


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    big_List = []
    o_Strs = strs.copy()   #Creating a copy that won't remove any values for it to loop through
    for p_Index in range(len(o_Strs)):
            p_Anagram = o_Strs[p_Index]
            if p_Anagram not in strs:
                 continue
            else:                    
                temp_List = []
                temp_List.append(p_Anagram)
                strs.remove(p_Anagram)
                for c_Index in range(len(o_Strs)):
                    c_Anagram = o_Strs[c_Index]
                    if c_Anagram in strs:
                        if isAnagram(p_Anagram,c_Anagram):
                            temp_List.append(c_Anagram)
                            strs.remove(c_Anagram)
            big_List.append(temp_List)
    return big_List
                        
          


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["","",""]))
print(groupAnagrams(["a"]))

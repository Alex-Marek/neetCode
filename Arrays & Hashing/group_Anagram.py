#My solution was too slow so I had to check the video solution posted on the site.
#This solution works by creating a hashmap/dictionary to solve the problem
#You need to make a dictionary hold the resulting group of anagrams
#It was decided to use a defaultdictionary because when you supply them with a type the key will default to a
#Blank of that type. So in our case a blank list []

# From there when you are running through the letters of each word use the fact ascii letters are ordered sequentially to
# Decide a place for them in the array, all you have to do is subtract the lowest ascii character from each one and they
# Will go into their own unique bins (0-26) (because there are 26 letters)
 
# Because of the way anagrams work every possible anagram should have the same array here because all we're doing is 
# Counting letters. Python specifically doesn't like arrays to be keys (because they are mutable) for dictionaries
# So we have to cast it as a tuple, which is fine in our case since we won't need to change them after this
# From here we just append our word and pass in the array as our key. Any words that happen to have the same key will 
# Naturally get grouped together in this format.

# Due to the fact we don't care about sending the array with the key of letters back we'll only return the values
from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for string in strs:
        count = [0] * 26

        for character in string:
            count[(ord(character) - ord("a"))] += 1
        res[tuple(count)].append(string)
    return res.values()
                        
          


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["","",""]))
print(groupAnagrams(["a"]))

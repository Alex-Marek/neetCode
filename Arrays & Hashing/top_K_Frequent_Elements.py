#45 Minutes
#105ms (Beats 92.79%) / 21mb (Beats 75.81%)
# Works by using a hashmap where the key is the unique value and the value is the amount of times in the list the unique
# value appeared. 

# Once that was done all I had to do was sort the dictionary. Using the sorted function on the items in the dict then having
# them recombined via a lambda function 
# From there simply recast them as a dict and you have a sorted dictionary based on the values

# Because the dictionary is sorted all you need to do is create blank list then loop through k times each time appending
# the key from the position you are at in the loop
from collections import defaultdict
def topKFrequent(nums: list[int], k: int) -> list[int]:
    h_Map = defaultdict(int)
    for value in nums:
        h_Map[value] += 1
    h_Map = dict(sorted(h_Map.items(), key=lambda item: item[1], reverse=True))
    res = []
    for num in range(k):
        res.append(list(h_Map.keys())[num])
    return res

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1],1))


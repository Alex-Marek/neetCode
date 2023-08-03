# 5 minutes 113ms (Beats 98.75% of users) / 17mb (Beats 61% of users)
# After I finished the original two_Sum I watched the video on it because my way of doing it was a bit slow but good on memory
# This was essentially the same solution as the previous problem except with +1 added to the return values. 

# Basically make a hash map of all the values and indexes in the array stored as (value:idx in this case)
# Once you do that you can solve this in constant time by just going through the array once
# Every time you go through a new element of the array add it and it's index to the hash map
# You can always find the target number by subtracing whatever number you're looking at from it and searching the hashmap
# If the number is found in the hashmap then simply return the index of that number in the hashmap and the index of where
# you are in the array.
def twoSum(numbers: list[int], target: int) -> list[int]:
    h_Map = {}
    for idx, value in enumerate(numbers):
        curSearch = target - value
        if curSearch in h_Map:
            return [h_Map[curSearch]+1, idx+1]
        h_Map[value] = idx
    return

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
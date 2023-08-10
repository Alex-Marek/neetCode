# 431ms (Beats 42%) / 17mb (Beats 60%)
# Did this problem a long time ago (before I even started the github for this) so it def needed to be redone to be faster/better
# This solution is cleaner easier to write/understand and faster 
# The solution works by looping through all the values in the nums list given to us
# Every time a new num is tried it calculates out the solution number for that number and adds it to the dict
# Before doing that it checks whether the number is currently already in the dict, if it is then it will return that plus
# the current index value since that ought to the solution
def twoSum(nums: list[int], target: int) -> list[int]:
    solNumbers = {}
    for idx, value in enumerate(nums):
        solNum = target - value
        if solNum in solNumbers:
            return [solNumbers[solNum], idx]
        solNumbers[value] = idx
    return False

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
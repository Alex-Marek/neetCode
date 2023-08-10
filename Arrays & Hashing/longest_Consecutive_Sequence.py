# 40 Minutes
# 352 ms (Beats 99% of users) / 30 mb (Beats 98% of users)

# A consecutive numbers is just any number where if you subtract the previous number you will get 1
# After sorting the numbers in ascending order, the solution is basically just make a loop to go through the list,
# Every iteration should check if the current streak is the new maximum, if it is then set the resolution to it
# if the numbers are consecutive you add to a streak until they are no longer consecutive
# if they are no longer consecutive it means that the subtraction wasn't either 1 or 0 which means you can reset your streak

# Updated to be more readable 364 ms (Beats 94% of users) / 30 mb (Beats 95% of users)

def longestConsecutive(nums: list[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    
    nums.sort()
    cur_Max = 1
    res = 1

    for idx, value in enumerate(nums):
        cur_Dif = value - nums[idx-1]
        if cur_Dif == 1:
            cur_Max += 1
        elif cur_Dif != 1 and cur_Dif != 0:
            cur_Max = 1
        
        res = max(cur_Max, res)
            
    return res

print(longestConsecutive([-8,-4,9,9,4,6,1,-4,-1,6,8]))
print(longestConsecutive([1,2,0,1]))
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# 40 Minutes
# 352 ms (Beats 99% of users) / 30 mb (Beats 98% of users)

# A consecutive numbers is just any number where if you subtract the previous number you will get 1
# After sorting the numbers in ascending order, the solution is basically just make a loop to go through the list,
# if the numbers are consecutive you add to a streak until they are no longer consecutive at which point you reset
# the streak to 1 and start over again
# At the end do a quick check to make sure the current streak isn't higher than the max one rn if it is just set maxStreak
# Also an edge case needed to be handled where we were passed in a blank array
# Additionally if the previous number and the current are the same that doesn't count toward the streak but doesn't end it

def longestConsecutive(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    maxStreak = 0
    streak = 0
    nums.sort()
    prevValue = nums[0] - 1
    for value in nums:
        if value - prevValue == 1:
            streak += 1
        elif value - prevValue == 0:
            continue
        else:
            if streak > maxStreak:
                maxStreak = streak
            streak = 1
        prevValue = value
    if streak > maxStreak:
        maxStreak = streak
    return maxStreak

print(longestConsecutive([-8,-4,9,9,4,6,1,-4,-1,6,8]))
print(longestConsecutive([1,2,0,1]))
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
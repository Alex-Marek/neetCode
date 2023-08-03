# Had to use solution from neetcode. My original solution of brute forcing with a triple for loop was too slow and bad
# For this solution you have to sort the list initially as it makes it reasonably fast to prevent duplicate values
# After sorting you have to loop through the list of numbers you were given, iniitally you have to make sure you're
# not right at the beginning or end of the array
# From there you create two pointers on the array one on the left side and one on the right side. 
# because we have a sorted list this will give us the ability to decide based on if we're too high or too low
# whether to have one pointer navigate down (right) the array or one navigate up it (left)
# From this point we put in a simple while loop which will stop when the left pointer is further along than the right pointer
# this would mean we've gone over every spot in the array and that there is no point in continuing
# Once we add all the values together we can simply check which pointer to move to make the goal value 0
# If the goal value is 0 then we had to add it to the array and move in both the left and right pointers
# In order to prevent duplicate numbers from being a problem we also put a while loop in there which will continue incrementing
# until a different number has been reached on the left side

def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for idx, value in enumerate(nums):
        if value > 0:
            break

        if idx > 0 and value == nums[idx-1]:
            continue

        l, r = idx+1, len(nums)-1 
        while l < r:
            threeSum = value + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([value, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l < r:
                    l+=1
    return res





print(threeSum([-1,0,1,2,-1,-4]))
#print(threeSum([0,1,1]))
#print(threeSum([0,0,0]))
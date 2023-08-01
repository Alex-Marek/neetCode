#Solution from Leetcode video people
# This problem can be divided into two steps for maximal efficiency
# The first step is to get a prefix multiplier, this will be the result of multiplying every number before the num in question
# The second step is to get the postfix multiplier, this is the result of multiplying every num after the num in question
# Once you have both of those if you multiply them together then you have the answers

# In this program we optimize for memory efficiency by storing the prefix in the results and then just replacing the values
# when multiplying with the postfix later
# To do this all that needed be done was reverse through the array and multiply
def productExceptSelf(nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    


print(productExceptSelf([1,1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
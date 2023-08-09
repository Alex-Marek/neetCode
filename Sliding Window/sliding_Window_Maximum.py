# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# returns [3,3,5,5,6,7]
def calcNewMax(nums2 = []):
    maxim = float('-inf')
    for value in nums2:
        maxim = max(maxim, value)
    return maxim

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    r = k
    curMax = float('-inf')
    
    curMax = calcNewMax(nums[0:r])
    res.append(curMax)

    while r < len(nums):
        if nums[r] >= curMax:
            curMax = nums[r]
            res.append(curMax)
        else:
            if nums[r-k] == curMax:
                curMax = calcNewMax(nums[r-k +1 : r+1])
            res.append(curMax)
        r += 1
    return res
            

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1,-1], 1))
print(maxSlidingWindow([5,3,4], 1))
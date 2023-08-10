def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    if k == 1:
        return nums
    res = []
    r = k

    curWin = []
    for value in nums[0:k]:
        curWin.append(value)
    curWin.sort(reverse=True)
    res.append(curWin[0])
    
    while r < len(nums):
        if nums[r] >= curWin[0]: 
            curWin.insert(0,nums[r])
        elif nums[r] < curWin[0]:   
            for idx in range(len(curWin)-1):
                if nums[r] == curWin[idx]:
                    curWin.insert(idx, nums[r])
                    break
                if nums[r] < curWin[idx] and nums[r] > curWin[idx+1]:
                    curWin.insert(idx+1, nums[r])
                    break    
            else:
                curWin.append(nums[r])

        curWin.remove(nums[r-k])
        res.append(curWin[0])
        
        r += 1
    
    return res

print(maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5), "Expecting: ", [10,10,9,2])
print(maxSlidingWindow([1,3,1,2,0,5], 3), "Expecting: ", [3,3,2,5])
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), "Expecting: ", [3,3,5,5,6,7])
print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1,-1], 1))
print(maxSlidingWindow([5,3,4], 1))
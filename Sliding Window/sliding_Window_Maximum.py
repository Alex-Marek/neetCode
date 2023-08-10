# Works by using a deque which allows items to be inserted or removed from either end of the queue
# If we aren't far enough in the list such that we've not seen k elements then it will repeatedly append the number that
# cooresponds with the left-most position of the deque to the resolution because that is going to be the largest number
# The deque is for storing indexes and will store the right-most index everytime
# if the furthest right index number found is less than the new number coming in then it will remove the furthest right index
# it will loop through this until the condition is no longer true, keeping the deque sorted
# If the left-most index is greater than the right-index that was stored in the deque it means that we must remove the left
# - most point because it is no longer in the window
from collections import deque
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    q = deque()
    l = r = 0
    while r < len(nums):
        
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()
        
        if (r+1) >= k:
            res.append(nums[q[0]])
            l += 1
        r += 1
    
    return res

print(maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5), "Expecting: ", [10,10,9,2])
print(maxSlidingWindow([1,3,1,2,0,5], 3), "Expecting: ", [3,3,2,5])
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), "Expecting: ", [3,3,5,5,6,7])
print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1,-1], 1))
print(maxSlidingWindow([5,3,4], 1))
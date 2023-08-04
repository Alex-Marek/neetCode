# 593 ms (Beats 93% of users) / 29 mb (Beats 55% of users)
# Had to listen to the video explanation of how this ought to work because I couldnt think of a non-brute force method that
# was foolproof for providing the answer
# The code for it was very easy so I didn't bother watching the guy code it

# Basically the idea is just you have a pointer at the left and the right side of the array, and keep moving inward 
# calculating the area each time. You decide which side to move inward based on which side is smaller
# I probably should have been able to think of this, but I couldn't think of what factor ought to decide which moves in
def maxArea(height: list[int]) -> int:
    res = 0
    l,r = 0, len(height) -1 
    
    while l < r:
        area = min(height[l], height[r]) * (r-l)
        res = max(res, area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return res



print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
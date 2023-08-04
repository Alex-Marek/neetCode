# 15 minutes / 891 ms (Beats 91% of users) / 27.37 mb (Beats 64% of users)
# I like thinking of it as a two pointer problem rather than a window sliding problem because it just makes more sense
# I don't really like this problem actually for some reason it feels like the solution shouldn't work, like there should be 
# another edge case to consider that would cause it to fail, but I know there isn't
def maxProfit(prices: list[int]) -> int:
    res = 0 
    l, r = 0, 1
    while r < len(prices):
        res = max(res, prices[r]- prices[l])
        if prices[r] < prices[l]:
            l = r
        r += 1
    return res

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# 431ms (Beats 42%) / 17mb (Beats 60%)
# Subtracts every number from every other number in the last and checks if they equal the target value if they do return
def twoSum(nums: list[int], target: int) -> list[int]:
        solNum = 0
        sol = []
        for x in range(len(nums)):
            solNum = target - nums[x]
            try:
                posNum = nums.index(solNum, x+1)
            except ValueError:
                continue
            else:
                if len(sol) < 2:
                    sol.append(posNum)
                    sol.append(x)
        return sol

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
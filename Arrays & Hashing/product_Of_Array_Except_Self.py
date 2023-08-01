#Too slow to work for Leetcode
def productExceptSelf(nums: list[int]) -> list[int]:
    res = []
    answers = {}
    for idx, value in enumerate(nums):
        curProd = 1
        if value not in answers:
            for kdx, m_Val in enumerate(nums):
                if kdx != idx:
                    curProd = curProd * m_Val
        else:
            res.append(answers[value])
            break
        res.append(curProd)
    return res
    


print(productExceptSelf([1,1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
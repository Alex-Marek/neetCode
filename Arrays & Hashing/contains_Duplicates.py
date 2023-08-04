# 476ms(Beats 98.74%)/31.03mb (Beats 42%)
# Converts the list into a set which can only have unique entries. After that just checks the length.
# If the new list is shorter a duplicate must have been removed meaning True should be returned
def containsDuplicate(nums: list[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
        
print(containsDuplicate(nums=[1,1,2,2,5,5]))
print(containsDuplicate(nums=[1,2,3,4,5]))
print(containsDuplicate(nums=[1,1,2,3,4,5]))
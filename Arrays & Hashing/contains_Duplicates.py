#476ms(Beats 98.74%)/31.03mb (Beats 42%)
#Converts the list into a set which can only have unique entries. After that just checks the length.
#If the new list is shorter a duplicate must have been removed meaning True should be returned
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
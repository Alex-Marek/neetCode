# An interesting idea is everytime the next value isn't greater than the previous you add that number to a dict starting at 
# if that dict isn't empty then whenever you add a new number you loop through all the previous numbers and if it's greater
# than them increment their number by one
from collections import defaultdict
def dailyTemperatures(temperatures: list[int]) -> list[int]:
   stack = []
   res = []
   test = defaultdict(int)
   for idx, value in enumerate(temperatures):
      stack.append(value)
      if value > stack[0]:
         stack.pop()
         res.append(len(stack))
         if len(test) > 0:
            for nums in test.keys():
               if test[nums] > 0:
                  res.append(test[nums])
                  test.pop(nums)
               elif test[nums] == 0:
                  break
      else:
         test[value] += 1
         if len(test) > 0:
            for nums in test.keys():
               if value > nums:
                  test[nums] += 1

   return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))


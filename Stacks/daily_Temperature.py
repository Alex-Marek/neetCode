# Here a different idea have a stack that stores a pair. The pair will hold the temperature it's index
# Then we while loop through that stack checking if the temperature is greater than the temperature from the most recently
# stored temp on the stack then we can pop out that pair and add it to the resolution at it's original index with the value
# of where we are in the for loop minus its index
# everytime the for loop runs all the way through it should append onto the stack the temperature and the index 

def dailyTemperatures(temperatures: list[int]) -> list[int]:
   stack = []
   res = [0] * len(temperatures)
   for idx, temp in enumerate(temperatures):
      while stack and temp > stack[-1][0]:
         sTemp, sIdx = stack.pop()
         res[sIdx] = idx - sIdx
      stack.append((temp,idx))
   return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))


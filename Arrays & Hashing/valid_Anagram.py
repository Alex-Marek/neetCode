# 54ms (Beats 91%)/ 16mb (Beats 65%)
# Updated to be a more elegant easier to program solution with what I've learned
# Basically the idea behind this one is that you can just populate both at the same time, and return if they're the same at
# the end rather than adding one to a dict then subtracting the other and returning instantly if any character didn't match up
# This solution may be marginally slower, but it is much easier to understand and write.
# New speed = 62 ms (Beats 63%) / 16mb (Beats 63%)
def isAnagram(s: str, t: str) -> bool:
      if len(t) != len(s):
            return False

      s_Letters, t_Letters = {}, {}      
      for idx in range(len(s)):
            s_Letters[s[idx]] = 1 + s_Letters.get(s[idx], 0)
            t_Letters[t[idx]] = 1 + t_Letters.get(t[idx], 0)

      return s_Letters == t_Letters
                

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))
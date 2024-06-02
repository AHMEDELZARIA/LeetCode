# Give a solution with constant space complexity
# Time complexity: O(|s|log|s|)
# Space complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      
      return sorted(s) == sorted(t)
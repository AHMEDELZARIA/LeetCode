# Time complexity: O(|s|)
# Space complexity: O(|s+t|)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      return Counter(s) == Counter(t)
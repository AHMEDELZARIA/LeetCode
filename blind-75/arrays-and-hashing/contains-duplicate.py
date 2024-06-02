# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      return len(set(nums)) != len(nums)
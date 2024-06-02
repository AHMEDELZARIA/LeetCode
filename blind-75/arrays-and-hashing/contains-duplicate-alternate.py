# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      nums_set = set()
        
      for num in nums:
        if num in nums_set:
          return True
            
      return False
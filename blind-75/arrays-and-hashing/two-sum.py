# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prev_nums = {}
      
      for index, num in enumerate(nums):
        num_needed = target - num
        if num_needed in prev_nums:
          return [prev_nums[num_needed], index]
        
        prev_nums[num] = index
    
      return
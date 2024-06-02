# Time complexity: O(m^2log(n)) where m is |strs| and n is the average str length in strs
# Space complexity: O(n + k) where k is the total number of chars in all strings
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      ans = defaultdict(list)

      for s in strs:
        c_sorted = "".join(sorted(s))
        ans[c_sorted].append(s)

      return ans.values()     
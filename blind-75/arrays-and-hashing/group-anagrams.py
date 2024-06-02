# Time complexity: O(m*n) where m is the |strs| and n is the avg length of a str in strs
# Space complexity: O(n + k) where k is the total number of characters in all strings
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      ans = defaultdict(list)

      for s in strs:
        c_count = [0] * 26
        for c in s:
          c_count[ord(c) - ord("a")] += 1
        ans[tuple(c_count)].append(s)

      return ans.values()     
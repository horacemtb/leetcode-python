"""
URL: https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

      shortest_word = ''
      min_len = 200

      for i in strs:
        if len(i) < min_len:
          min_len = len(i)
          shortest_word = i

      prefix = ''

      for i in range(len(shortest_word)):
        q = 0
        for s in strs:
          if shortest_word[i] == s[i]:
            q+=1
            if q == len(strs):
              prefix += shortest_word[i]
          else:
            return prefix

      return prefix

sol = Solution()

strs = ["flower", "flow", "flight"]

assert sol.longestCommonPrefix(strs) == 'fl'
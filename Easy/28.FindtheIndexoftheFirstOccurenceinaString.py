"""
URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

      if len(needle) > len(haystack):
        return -1

      if haystack == needle:
        return 0

      step = len(needle)

      for i in range(0, len(haystack)):
        if haystack[i:i+step] == needle:
          return i
      return -1

sol = Solution()

haystack = "sadbutsad"
needle = "sad"

assert sol.strStr(haystack, needle) == 0
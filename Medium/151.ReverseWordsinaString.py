"""
URL: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:

      space = 0
      char = 0
      l = 0
      res = ''

      for i in range(len(s)-1, -1, -1):
        if s[i] == ' ':
          space += 1
        else:
          char += 1
          l += 1
          if i == 0 or s[i-1] == ' ':
            start = space+char
            if space == 0:
              word = s[-start:]
            else:
              word = s[-start:-start+l]
            l = 0
            res += word + ' '
      return res[:-1]

sol = Solution()

s = "  hello world  "

assert sol.reverseWords(s) == "world hello"
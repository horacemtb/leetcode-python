"""
URL: https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      
      l = 0

      for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
          l+=1
          if i == 0 or s[i-1] == ' ':
            return l
      return l

sol = Solution()

s = "Hello World"

assert sol.lengthOfLastWord(s) == 5
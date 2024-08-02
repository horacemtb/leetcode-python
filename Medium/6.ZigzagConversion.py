"""
URL: https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows == len(s):
          return s

        l_strings = ['' for i in range(numRows)]

        current_row = 0
        going_down = False

        for char in s:
          l_strings[current_row] += char

          if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
          
          if going_down:
            current_row += 1 
          else:
            current_row -= 1

        return ''.join(l_strings)

sol = Solution()

s = "PAYPALISHIRING"
numRows = 3

assert sol.convert(s, numRows) == "PAHNAPLSIIGYIR"
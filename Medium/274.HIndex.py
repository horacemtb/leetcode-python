"""
URL: https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

274. H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1

"""

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

      if len(citations) == 1:
        if citations[0] == 0:
          return 0
        else:
          return 1

      counter = {}

      n_sorted = sorted(citations)

      for i in set(citations):
        min_ind = n_sorted.index(i)
        counter[i] = len(n_sorted[min_ind:])

      h = 0
      for k,v in counter.items():
        if min(k,v) > h:
          h = min(k,v)

      return h

sol = Solution()

citations = [3,0,6,1,5]

assert sol.hIndex(citations) == 3
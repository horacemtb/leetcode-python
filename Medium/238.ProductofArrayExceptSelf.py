"""
URL: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

      prefix_prod = [0]*len(nums)
      prefix_res = 1
      suffix_prod = [0]*len(nums)
      suffix_res = 1

      for i in range(len(nums)):

        prefix_res = prefix_res*nums[i]
        prefix_prod[i] = prefix_res
      
      for q in range(len(nums)-1, -1, -1):

        suffix_res = suffix_res*nums[q]
        suffix_prod[q] = suffix_res

      prod = []

      for i in range(len(nums)):
        if i == 0:
          prod.append(suffix_prod[1])
        elif i == len(nums)-1:
          prod.append(prefix_prod[-2])
        else:
          prod.append(prefix_prod[i-1]*suffix_prod[i+1])

      return prod

sol = Solution()

nums = [1,2,3,4]

assert sol.productExceptSelf(nums) == [24,12,8,6]
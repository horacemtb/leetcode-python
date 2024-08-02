"""
URL: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      
      i = 0
      count_dict = {}

      while i < len(nums):
        if nums[i] not in count_dict:
          count_dict[nums[i]]=1
        else:
          count_dict[nums[i]]+=1
        if max(count_dict.values()) > len(nums)/2:
          return max(count_dict, key=count_dict.get)
        i+=1

sol = Solution()

nums = [2,2,1,1,1,2,2]

assert sol.majorityElement(nums) == 2
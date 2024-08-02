"""
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count_dict = {}
        pointer = 0

        while pointer < len(nums)-1:
            if nums[pointer+1] == nums[pointer]:
                if not count_dict.get(nums[pointer+1]):
                    count_dict[nums[pointer+1]] = 2
                    pointer+=1
                else:
                    nums.remove(nums[pointer+1])
            else:
                pointer+=1

        return len(nums)

sol = Solution()

nums = [1,1,1,2,2,3]

assert sol.removeDuplicates(nums) == 5
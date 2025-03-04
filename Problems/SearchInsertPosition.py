from collections.abc import Iterable



"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


def searchInsertv1(nums: List[int], target: int) -> int:
    """
    Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
    """

    first = nums[0]
    last = nums[-1]
    for i in range(0, len(nums)):
        if target in nums:
            if nums[i] == target:
                return i

        elif target > last:
            return nums.index(last)+1

        elif target < first:
            return 0

        elif nums[i] < target and nums[i+1] > target:
            return i+1


def searchInsertv2(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start


print(searchInsertv2(nums = [1,3,5,6], target = 5))
print(searchInsertv2(nums = [1,3,5,6], target = 2))
print(searchInsertv2(nums = [1,3,5,6], target = 7))
print(searchInsertv2(nums = [1,3,5,6], target = 0))

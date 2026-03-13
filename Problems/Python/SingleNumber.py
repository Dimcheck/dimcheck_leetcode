"""
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List


def singleNumber(nums: List[int]) -> int:
    """
    Example 1:
    Input: nums = [2,2,1]
    Output: 1

    Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

    Example 3:
    Input: nums = [1]
    Output: 1
    """

    d_pop = {}
    start = 0
    end = len(nums) - 1

    while start <= end:
        if nums[start] in d_pop:
            d_pop[nums[start]] += 1
        else:
            d_pop[nums[start]] = 1
        start += 1
    del nums

    for key, s_n in d_pop.items():
        if s_n == 1:
            return key


def singleNumberv2(nums: List[int]) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i

print(singleNumberv2([4,1,2,1,2]))
print(singleNumberv2([2,2,1]))

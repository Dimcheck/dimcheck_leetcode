"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List

def twoSumv2(nums: List[int], target: int) -> List[int]:
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    result = {}

    for idx, number in enumerate(nums):
        # print(idx, number)
        if target - number in result:
            print([result[target - number], idx])
        else:
            result[number] = idx





def twoSumv1(nums: List[int], target: int) -> List[int]:
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    first_number = abs(target - nums[0])
    second_number = abs(first_number - target)

    result = []
    first_index, second_index = nums.index(first_number), nums.index(second_number)

    result.append(first_index)
    result.append(second_index)

    return result

twoSumv2(nums=[2,7,11,15], target=9)


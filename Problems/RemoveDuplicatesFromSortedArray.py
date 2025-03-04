"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
- The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    """
    new_nums = set(nums)
    nums = list(new_nums)
    k = len(nums)
    return k

def removeDuplicatesv2(nums: List[int]) -> int:
    k = len(nums)
    for i in range(k-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i]
    return k


print(removeDuplicatesv2([1,1,2]))
# print(removeDuplicates([1,1,2]))
print(removeDuplicatesv2([0,0,1,1,1,2,2,3,3,4]))
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



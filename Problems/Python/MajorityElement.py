from typing import List
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""




def majorityElement(nums: List[int]) -> int:
    count_table = {}
    counter = 0
    len_nums = len(nums)

    while counter < len_nums:
        if nums[counter] in count_table:
            count_table[nums[counter]] += 1
            counter += 1
        else:
            count_table[nums[counter]] = 1
            counter += 1

    del nums
    for key, value in count_table.items():
        if value > len_nums // 2:
            return key









print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([4, 3, 3]))




"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

from typing import List

# def reset(numbers: List, start: int, end: int):
#     start = 0
#     end = len(numbers) - 1
#     return start, end



def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

    Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

    Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    """
    start = 0
    end = len(numbers) - 1
    result = []

    while start < end:
        if numbers[start] + numbers[end] == target:
            result.append(start+1)
            result.append(end+1)
            break
        else:
            end -= 1
    if not result:
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                result.append(start+1)
                result.append(end+1)
                break
            else:
                start += 1

    return result

def twoSumv2(numbers: List[int], target: int) -> List[int]:
    """
    Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

    Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

    Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    """
    start = 0
    end = len(numbers) - 1
    result = []

    while start < end:
            if numbers[start] + numbers[end] == target:
                result.append(start+1)
                result.append(end+1)
                break
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
    return result


print(twoSumv2(numbers=[3,24,50,79,88,150,345], target=200))
# print(twoSumv2(numbers=[2,7,11,15], target=9))


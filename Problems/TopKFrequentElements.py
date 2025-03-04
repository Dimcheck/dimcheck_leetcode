"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List
import operator

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:

    Input: nums = [1], k = 1
    Output: [1]
    """
    mfe = {}
    start = 0
    result = []

    while len(nums) > start:
        if nums[start] in mfe:
            mfe[nums[start]] += 1
        else:
            mfe[nums[start]] = 1
        start += 1

    mfe = sorted(mfe.items(), key=operator.itemgetter(1))
    for num, count in mfe[-abs(k):]:
        result.append(num)

    return result



def topKFrequentv2(nums: List[int], k: int) -> List[int]:
    ...



print(topKFrequent(nums=[1,1,1,2,2,3], k=2))     #output: [1,2]
print(topKFrequent(nums=[1], k=1))               #output: [1]
print(topKFrequent(nums=[-1,-1], k=1))           #output: [-1]
print(topKFrequent(nums=[1,2], k=2))             #output: [1,2]
print(topKFrequent(nums=[3, 0, 1, 0], k=1))      #output: [0]
print(topKFrequent(nums=[4,1,-1,2,-1,2,3], k=2)) #output: [[-1,2]]
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

from typing import List


def mergev1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
    """

    nums1 = set(nums1)
    nums1 = list(nums1)
    nums1.extend(nums2)
    return nums1[1:]

def mergev2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums3 = []
    n1 = 0
    n2 = 0
    while n1 <= m and n2 != n:
        if nums1[n1] <= nums2[n2] and nums1[n1] != 0:
            nums3.append(nums1[n1])
            n1 += 1
        else:
            nums3.append(nums2[n2])
            n2 += 1
    nums3 = nums1
    return nums1

def mergev3(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    
    last = m + n - 1
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n-1]
        n, last = n-1, last-1
    return nums1

# print(mergev2(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(mergev3(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(mergev3(nums1 = [0], m = 0, nums2 = [1], n = 1))
# print(mergev3(nums1 = [0], m = 0, nums2 = [1], n = 1))
# print(mergev1(nums1 = [0], m = 0, nums2 = [1], n = 1))


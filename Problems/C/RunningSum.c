/* 
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17] 
*/

#include <stdlib.h>
#include <stdbool.h>  // For boolean data type (bool, true, false)

int* runningSum(int* nums, int numsSize, int* returnSize) {
    int *result = malloc(sizeof(int) * numsSize);
    int counter = 1;
    int lastSum = nums[0];
    result[0] = lastSum;
    
    while (numsSize > counter) {
        lastSum = lastSum + nums[counter];
        result[counter] = lastSum;
        counter = counter + 1;
    }
    
    *returnSize = numsSize; // C has no built-in metadata for arrays.
    return result;
}


int numsSize = 4;
int nums[4] = {1,2,3,4};
int *returnSize = &numsSize;


int main() {
    runningSum(nums, numsSize, returnSize);
}
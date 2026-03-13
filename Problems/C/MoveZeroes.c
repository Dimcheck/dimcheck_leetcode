/*
 Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
 Note that you must do this in-place without making a copy of the array.
 
 Example 1:
 
 Input: nums = [0,1,0,3,12]
 Output: [1,3,12,0,0]
 
 Example 2:
 
 Input: nums = [0]
 Output: [0]
 */
 
 #include <stdio.h>
 #include <stdlib.h>
 
 
void moveZeroes(int* nums, int numsSize) {
    int temp;
    int start = 0;
    int end = 1;

    printf("Before: ");
    for (int i = 0; i < numsSize; ++i) {
        printf("%d", nums[i]);
    }

    while (end < numsSize) {
        if (nums[start] < nums[end]) {
            printf("\n start %d end %d", nums[start], nums[end]);
            printf("-> start %d end %d", nums[end], nums[start]);
            temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
        }
    ++start;
    ++end;
    }
    
    start = 0; end = 1;
    while (end < numsSize) {
        if (nums[start] < nums[end]) {
            printf("\n start %d end %d", nums[start], nums[end]);
            printf("-> start %d end %d", nums[end], nums[start]);
            temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
        }
    ++start;
    ++end;
    }
    
    printf("\nAfter:  ");
    for (int i = 0; i < numsSize; ++i) {
        printf("%d", nums[i]);
    }
    printf("\n");
}
 
 
int numsSize = 5;
int nums[5] = {0,1,0,3,12};
// int nums[5] = {1,0,3,12,0};

int main() {
    moveZeroes(nums, numsSize);
    return 1;
}
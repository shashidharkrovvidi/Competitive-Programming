/**
time complexity: O(n) where n is the length of the nums array
space complexity: O(1)
approach: step 1: from the right side, find out the break point. this is where nums[i] < nums[i+1]
step 2: now, in the list after ith index, find out the number which is just greater than the number at break point and swap these two numbers. this ensures that the next permutation is just one step larger.
step 3: after the break index, reverse the numbers in the array. the subarray after the break point is guaranteed to be in descending order, so reversing it gives the smallest lexicographic continuation. 
*/
class Solution {
    public void reverseSubArray(int[] nums, int start, int end)
    {
        while(start<end)
        {
            swap(nums,start,end);
            start++;
            end--;
        }
    }
    public void swap(int[] nums, int i, int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    public void nextPermutation(int[] nums) {
        int breakIndex = -1;
        int len = nums.length;
        for(int i=len-2;i>=0;i--)
        {
            if(nums[i] < nums[i+1])
            {
                breakIndex = i;
                break;
            }
        }
        System.out.printf("break point is %d",breakIndex);
        if(breakIndex == -1)
        {
            reverseSubArray(nums,breakIndex+1,len-1);
            return;
        }
        for(int i=len-1;i>breakIndex;i--)
        {
            if(nums[i] > nums[breakIndex])
            {   
                swap(nums, breakIndex,i);
                break;
            }
        }
        reverseSubArray(nums,breakIndex+1,len-1);
    }
}
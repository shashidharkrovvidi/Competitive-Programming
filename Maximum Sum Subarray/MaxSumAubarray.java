/**
 https://leetcode.com/problems/maximum-subarray/
time complexity: O(n) where n is the size of the nums array
space complexity: O(1)
approach: we are using kadane's algorithm. we iterate over the array and keep track of the overall maximum sum and the current running maximum sum.
if at any point, the current running sum is greater than the overall maximum sum, we update the overall maximum sum.
also, if the current running sum is less than 0, we drop the subarray. so we set the current running sum to 0
 */
class Solution {
    public int maxSubArray(int[] nums) {
        int start = 0;
        int startMaxSubarray = -1;
        int endMaxSubarray = -1;
        int runningSum = 0;
        int maxSum = Integer.MIN_VALUE;
        int len = nums.length;
        for(int i=0;i<len;i++)
        {
            if(runningSum == 0)
            {
                start = i;
            }
            runningSum += nums[i];
            if(runningSum > maxSum)
            {
                maxSum = runningSum;
                startMaxSubarray = start;
                endMaxSubarray = i;
            }
            if(runningSum < 0)
            {
                runningSum = 0; //when the running sum is zero, it is vain to consider this subarray, so we drop the subarray and set running sum to 0
            }
        }
        System.out.printf("start index = %d\nend index = %d\n", startMaxSubarray, endMaxSubarray);
        return maxSum;
    }
}
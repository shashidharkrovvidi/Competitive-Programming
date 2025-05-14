'''
https://leetcode.com/problems/maximum-subarray/
time complexity: O(n) where n is the size of the nums list
space complexity: O(1)
approach: we are using kadane's algorithm. we iterate over the list and keep track of the overall maximum sum and the current running maximum sum.
if at any point, the current running sum is greater than the overall maximum sum, we update the overall maximum sum.
also, if the current running sum is less than 0, we drop the subarray. so we set the current running sum to 0
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -(2**31-1)
        running_sum = 0
        length = len(nums)
        start = 0
        end_max_subarray = -1
        start_max_subarray = -1
        for i in range(length):
            if running_sum == 0:
                start = i
            running_sum += nums[i]
            if(running_sum > max_sum):
                max_sum = max(running_sum,max_sum) #max_sum will be updated when running_sum is greater than the current value of max_sum
                start_max_subarray = start
                end_max_subarray = i
            if running_sum < 0: #when the running sum is zero, it is vain to consider this subarray, so we drop the subarray and set running sum to 0
                running_sum = 0
        print(f"start index = {start_max_subarray}\nend index={end_max_subarray}")
        return max_sum

        
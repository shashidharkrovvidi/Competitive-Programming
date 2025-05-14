/**
https://leetcode.com/problems/sort-colors/
time complexity: O(n) where n is the size of the nums array
space complexity: O(1)
approach: think of a hypothetical array where [0, low-1] are all 0s
[low, mid-1] are all 1s
[high+1,n-1] are all 2s
and the array that you need to sort is between [mid,high]
so if nums[mid] is 0, tthen you need to swap nums[mid] with nums[low] and increment low so that [0, low-1] is all zeroes. increment mid index.
if nums[mid] is 2, then you need to swap nums[mid] with nums[high] and decrement high so that [high+1, n-1] is all 2s. in this case you dont increment mid because you dont know which number was there at high index before swapping.
if nums[mid]==1, you increment mid since [low to mid-1] will all be zeroes.
*/
class Solution {
    public void swap(int[] nums,int i,int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length-1;
        while(mid <= high)
        {   
            int curr = nums[mid];
            if(curr == 0)
            {
                swap(nums, low, mid);
                low++;
                mid++;
            }
            else if(curr == 1)
            {
                mid++;
            }
            else
            {
                swap(nums, mid, high);
                high--;
            }
        }
        
    }
}
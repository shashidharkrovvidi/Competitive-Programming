'''
time complexity: O(n) where n is the length of the nums list
space complexity: O(1)
approach: step 1: from the right side, find out the break point. this is where nums[i] < nums[i+1]
step 2: now, in the list after ith index, find out the number which is just greater than the number at break point and swap these two numbers. this ensures that the next permutation is just one step larger.
step 3: after the break index, reverse the numbers in the list. the sublist after the break point is guaranteed to be in descending order, so reversing it gives the smallest lexicographic continuation.
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        break_index = -1
        for i in range(length-2,-1,-1):
            if nums[i] < nums[i+1]:
                break_index = i
                break
        if break_index == -1:
            nums.reverse()
            return nums
        for i in range(length-1,break_index,-1):
            if nums[i] > nums[break_index]:
                nums[i], nums[break_index] = nums[break_index], nums[i]
                break
        nums[break_index+1:length] = nums[break_index+1:length][::-1]
        return nums


        
#https://leetcode.com/problems/subsets/description/

#time complexity: O((2 ^ n) * n) where n the number of distinct elements. at every decision point, there is a branching factor of 2 (we include or exclude the integer) and the max depth of the state space tree is n. for every 2 ^ n subsets created, we copy them which takes O(n) time.
#space complexity: O(n) owing to the max depth of the recursion tree. candidate list also takes up O(n) space.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(result, [], nums,0)
        return result

    def backtrack(self, result, candidate, nums, index):
        if index == len(nums):
            result.append(candidate.copy())
            return
        
        candidate.append(nums[index])
        self.backtrack(result, candidate, nums, index+1)
        candidate.pop()
        self.backtrack(result, candidate, nums, index+1)
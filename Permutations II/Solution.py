#https://leetcode.com/problems/permutations-ii/description/

#time complexity: O(n * n!) where n is the number of distinct integers. for each n, we explore the remaining integers to form a permutation, which gives us n! and for each of the n! permutation, we make a copy and add it to the result list which is O(n)

#space complexity: O(n) where n the depth of the state space tree. candidate list and visited set also take up O(n) space.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        result = []
        self.dfs(result, visited, [], nums)
        return result
    
    def dfs(self, result, visited, candidate, nums):
        if len(candidate) == len(nums) and candidate not in result:
            result.append(candidate.copy())
            return
        
        for i in range(len(nums)):
            if visited[i] == 0:
                visited[i] = 1
                candidate.append(nums[i])
                self.dfs(result, visited, candidate, nums)
                candidate.pop()
                visited[i] = 0
    
        
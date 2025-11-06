#https://leetcode.com/problems/permutations/

#time complexity: O(n * n!) where n is the number of distinct integers. for each n, we explore the remaining integers to form a permutation, which gives us n! and for each of the n! permutation, we make a copy and add it to the result list which is O(n)

#space complexity: O(n) where n the depth of the state space tree. candidate list and visited set also take up O(n) space.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(result, [], set(), nums)
        return result

    def dfs(self, result, candidate, visited, nums):
        if len(candidate) == len(nums):
            result.append(candidate.copy())
            return
        
        for num in nums:
            if num not in visited:
                candidate.append(num)
                visited.add(num)
                self.dfs(result, candidate, visited, nums)
                candidate.pop()
                visited.remove(num)
    

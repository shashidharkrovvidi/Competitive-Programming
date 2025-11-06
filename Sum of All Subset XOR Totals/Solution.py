#https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        xor = 0
        self.backtrack(result, [], nums, 0)
        print(result)
        total = 0
        for combo in result:
            xor = 0
            for num in combo:
                xor ^= num
            total += xor
        return total
    
    def backtrack(self, result, candidate, nums, index):
        if index == len(nums):
            result.append(candidate.copy())
            return
        candidate.append(nums[index])
        self.backtrack(result, candidate, nums, index+1)
        candidate.pop()
        self.backtrack(result, candidate, nums, index+1)
        

        
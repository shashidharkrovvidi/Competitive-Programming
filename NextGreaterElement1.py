'''
https://leetcode.com/problems/next-greater-element-i/
time complexity: O(m+n) where m is the length of nums1 list and n is the length of nums2 list
space complexity: O(1)
approach: 
we use a stack.
we are also maintaining a dictionary which stores (number, next greater number) as key value pairs
we iterate over the nums2 list, and if the current number is greater than the top element of the stack,
we pop the top element and add a pair of (top element, current number) in the dictionary.
we do this until all the top elements of the stack which are lesser than the current number are in the dictionary entries
we add the current number to the stack
at the end of the iteration, we may have a stack which has numbers . these are numbers which dont have next greater elements, so we add these numbers with -1 as pairs in the dictionary.
lastly, we iterate over the nums1 list and use the dictionary to create a result list 
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        stack = []
        result = []

        for curr in nums2:
            while stack and curr > stack[-1]:
                map[stack.pop()] = curr
            stack.append(curr)
        
        while stack:
            map[stack.pop()] = -1
        
        for curr in nums1:
            result.append(map[curr])
        
        return result
        
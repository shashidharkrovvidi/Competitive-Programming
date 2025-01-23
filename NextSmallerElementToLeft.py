'''
https://www.interviewbit.com/problems/nearest-smaller-element/
time complexity: O(n) where n is the length of the A list
space complexity: O(1)
the stack here is used to keep track of the least value element the left of the current element on which we are during the iteration
'''
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
		result = []
		stack = []
		for curr in A:
			while stack and curr <= stack[-1]:
				stack.pop()
			result.append(-1 if not stack else stack[-1])
			stack.append(curr)
		return result
				
				
		
				
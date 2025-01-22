class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize the result array with -1, as default values for "no next greater element"
        result = [-1] * n
        
        # Initialize an empty stack to store elements in a decreasing order
        stack = []
        
        # Iterate backwards through the circular array (2*n-1 to 0)
        # The modulus operation allows us to simulate the circular nature of the array
        for i in range(2 * n - 1, -1, -1):
            # Get the current element from the circular array
            curr = nums[i % n]
            
            # Pop elements from the stack that are less than or equal to the current element
            # This ensures the stack always contains potential "next greater elements" for the current index
            while stack and stack[-1] <= curr:
                stack.pop()
            
            # For the first pass through the array (i < n), determine the next greater element if the stack is not empty
            if i < n and stack:
                result[i] = stack[-1]  # The top of the stack is the next greater element
            
            # If the stack is empty and we're in the first pass, the next greater element remains -1 (default)
            elif i < n and not stack:
                result[i] = -1
            
            # Push the current element onto the stack for future comparisons
            stack.append(curr)
        
        # Return the result array containing the next greater elements for each index
        return result

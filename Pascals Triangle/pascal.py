'''
https://leetcode.com/problems/pascals-triangle/description/
time complexity: O(number of rows ^ 2)
space complexity: O(number of rows)
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        for i in range(2,numRows):
            row_list = [1]
            previous = result[i-1]
            for j in range(len(previous)-1):
                row_list.append(previous[j] + previous[j+1])
            row_list.append(1)
            result.append(row_list)
        return result
        
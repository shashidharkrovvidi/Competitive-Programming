/**
 https://leetcode.com/problems/pascals-triangle/
time complexity: O(numRows ^ 2)
space complexity: O(numRows)
 */
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        result.get(0).add(1);
        if(numRows == 1)
        {
            return result;
        }
        result.add(new ArrayList<>());
        result.get(1).add(1);
        result.get(1).add(1);
        if(numRows == 2)
        {
            return result;
        }
        for(int i=2;i<numRows;i++)
        {
            List<Integer> previous = result.get(i-1);
            List<Integer> temp = new ArrayList<>();
            temp.add(1);
            for(int j=0;j<previous.size()-1;j++)
            {
                temp.add(previous.get(j) + previous.get(j+1));
            }
            temp.add(1);
            result.add(temp);
        }
        return result;
    }
}
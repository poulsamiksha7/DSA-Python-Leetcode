class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []

        for num in range(numRows):
            row = [1] * (num + 1) 
            for j in range(1, num):
                row[j] = pascal[num - 1][j - 1] + pascal[num - 1][j]
            pascal.append(row)

        return pascal
        
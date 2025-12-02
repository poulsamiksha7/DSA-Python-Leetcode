class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
              square=i*i
              ans.append(square)
              ans.sort()
        return ans
                
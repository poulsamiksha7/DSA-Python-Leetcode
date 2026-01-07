class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum, rightSum = 0, sum(nums)
        for i, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return i
            leftSum += ele
        return -1      
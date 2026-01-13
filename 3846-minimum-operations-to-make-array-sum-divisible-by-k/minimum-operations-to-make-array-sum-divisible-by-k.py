class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total=sum(nums)
        reminder=total%k
        if reminder==0:
            return 0
        elif reminder>0:
            return reminder
        else:
            return -1
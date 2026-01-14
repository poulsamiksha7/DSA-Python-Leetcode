class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]%3!=0:
               ans+=1
        return ans
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
            if count[i]>n//2:
                return i
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
        
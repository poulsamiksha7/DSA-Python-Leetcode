class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        total=list()
        c_sum=0
        for i in range (len(nums)):
            c_sum+=nums[i]
            total.append(c_sum)
        return total    
        
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        count=0
        max_no=0
        for i in range(0,n):
            if count==0:
                max_no=nums[i]
                count=1
            elif max_no==nums[i]:
                count+=1
            else:
                count-=1
        return max_no
                  
            
     

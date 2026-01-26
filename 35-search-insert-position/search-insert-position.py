class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a=0
        if target in nums:
            return nums.index(target)
        elif(target>nums[len(nums)-1]):
            return len(nums)
        elif target-1 in nums:
            a= (nums.index(target-1)+1)
        elif target+1 in nums:
            a= (nums.index(target+1))
        if(a<0):
            return 0
        else:
            return a
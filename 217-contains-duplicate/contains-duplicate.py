class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                return True
        return False

        

            

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        l_h = 0
        for num in count:
            if num + 1 in count:
                l_h = max(l_h, count[num] + count[num+1])
        return l_h
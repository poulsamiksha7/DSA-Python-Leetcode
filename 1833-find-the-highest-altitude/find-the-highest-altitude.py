class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n=0
        max_num=0

        for i in gain:
            n+=i
            max_num=max(n,max_num)
        return max_num
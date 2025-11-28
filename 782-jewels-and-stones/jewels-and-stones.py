class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        for ch in jewels:
            if ch in stones:
                count+=stones.count(ch)
        return count

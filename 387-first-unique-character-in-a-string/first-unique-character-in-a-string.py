class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=Counter(s)
        for ch in s:
            if count[ch]==1:
                return s.index(ch)
        return -1
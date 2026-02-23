class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return len({s[i-k:i] for i in range(k,len(s)+1)})==2**k
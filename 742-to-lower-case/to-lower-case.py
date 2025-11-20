class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        for ch in s:
            if 'A' <= ch <= 'Z':
                ans+=chr(ord(ch)+32)
            else:
                ans+=ch
        return ans

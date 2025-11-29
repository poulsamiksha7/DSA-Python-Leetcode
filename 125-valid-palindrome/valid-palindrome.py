class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=""
        for i in s:
            if i.isalnum():
                a+=i.lower()
        return a==a[::-1]
                
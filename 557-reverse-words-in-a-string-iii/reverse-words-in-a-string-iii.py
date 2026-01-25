class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        s=s.split()
        for i in s:
            l.append(i[::-1])
        return " ".join(l)

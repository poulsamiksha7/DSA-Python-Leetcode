class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        a=len(g)
        b=len(s)
        g.sort()
        s.sort()
        l=0
        r=0
        while l<b and r<a:
            if s[l]>=g[r]:
                r+=1
            l+=1
        return r
        
        
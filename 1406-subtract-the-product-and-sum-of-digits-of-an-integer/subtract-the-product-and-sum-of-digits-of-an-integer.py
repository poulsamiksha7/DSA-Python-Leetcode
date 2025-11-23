class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        add=0
        mult=1
        while n>0:
            digit=n%10
            mult*=digit
            add+=digit
            res=mult-add
            n=n//10
        return res
                                                        
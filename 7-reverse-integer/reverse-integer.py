class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n_sign= -1 if x<0 else 1
        x = abs(x)
        
        rev_no=0
        while x>0:
            ld=x%10
            rev_no=(rev_no*10)+ld
            x//=10
        rev_no*=n_sign

        if rev_no < -2**31 or rev_no >2**31 -1:
            return 0
        return rev_no
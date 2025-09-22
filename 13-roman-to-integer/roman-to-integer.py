class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        for i in range(len(s)-1):
            if my_dict[s[i]]<my_dict[s[i+1]]:
                result-=my_dict[s[i]]
            else:
                result+=my_dict[s[i]]
        result+=my_dict[s[-1]]
        return result
        
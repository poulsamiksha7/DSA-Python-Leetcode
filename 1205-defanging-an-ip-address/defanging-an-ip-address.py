class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defangIPaddress=""
        for i in address:
            if i=='.':
                defangIPaddress += "[.]"
            else:
                defangIPaddress += i
        return defangIPaddress
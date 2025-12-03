class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result=""
        for i in range(len(indices)):
            result+=s[indices.index(i)]
        return result
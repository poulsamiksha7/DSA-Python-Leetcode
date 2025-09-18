class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix=""
        first_str =strs[0]
        for i in range(len(first_str)):
            for other_str in strs[1:]:
                if i>=(len(other_str)) or other_str[i]!=first_str[i]:
                    return prefix
            prefix+=first_str[i]
        return prefix
        
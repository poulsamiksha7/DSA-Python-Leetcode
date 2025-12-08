class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for ch in strs:
            arr=[0]*26
            for char in ch:
                arr[ord(char)-ord('a')]+=1
            key=tuple(arr)
            if key not in d:
                d[key]=[]
            d[key].append(ch)
        return list(d.values())

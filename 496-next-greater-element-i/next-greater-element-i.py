class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        stack = []
        for num in nums2 :
            while stack and num > stack[-1]:
                map[stack.pop()] = num
            stack.append(num)
        result = []
        for val in nums1 :
            result.append(map.get(val,-1))
        return result
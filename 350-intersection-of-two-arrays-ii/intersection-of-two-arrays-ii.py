class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts = collections.Counter(nums1)
        ans = []

        for num in nums2:
            if counts[num] > 0:
                ans += num,
                counts[num] -= 1

        return ans
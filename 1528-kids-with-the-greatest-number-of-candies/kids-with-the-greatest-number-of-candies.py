class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans=[]
        max_candies=max(candies)
        for i in candies:
            if i+extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans

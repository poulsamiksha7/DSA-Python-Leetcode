class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = sorted(score)[::-1]
        a = []
        for i in score:
            if n.index(i)==0:
                a.append("Gold Medal")
            elif n.index(i)==1:
                a.append("Silver Medal")
            elif n.index(i)==2:
                a.append("Bronze Medal")
            else:
                a.append(str(n.index(i)+1))
        return a
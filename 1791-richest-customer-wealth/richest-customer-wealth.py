class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth=0
        rows=len(accounts)
        columns=len(accounts[0])
        for i in range(0,rows):
            wealth=0
            for j in range(0,columns):
                wealth+=accounts[i][j]
            max_wealth=max(max_wealth,wealth)
        return max_wealth
        
        
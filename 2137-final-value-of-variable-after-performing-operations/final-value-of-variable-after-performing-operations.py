class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
#         Start with X = 0.

# Traverse each operation in the list.

# If the operation means increment, increase X by 1.

# If the operation means decrement, decrease X by 1.

# After processing all operations, return X.

        X=0
        for i in operations:
            if i=="X++":
                 X+=1
            elif i=="++X":
                 X+=1
            elif i=="--X":
                 X-=1
            elif i=="X--":
                 X-=1
            else:
                 X==0
        return X
        
            

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        found = []
        minimum_index_value = float("inf")
        value = 0
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    value = i + j
                    if value < minimum_index_value:
                        minimum_index_value = value
                        found = [list1[i]]
                    elif value == minimum_index_value:
                        found.append(list1[i])
        
        return found
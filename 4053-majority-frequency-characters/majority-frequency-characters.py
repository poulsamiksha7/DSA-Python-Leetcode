class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        hashmap = defaultdict(list)
        majority = 0
        
        for char in 'abcdefghijklmnopqrstuvwxyz':

            if char in s:
                hashmap[s.count(char)].append(char)

                majority = max(majority , len(hashmap[s.count(char)]))
            
        current_freq = 0
        
        for key in hashmap:

            if len(hashmap[key]) == majority:

                if current_freq < key:
                    
                    result = ''.join(hashmap[key])
                
                    current_freq = key
                
        return result
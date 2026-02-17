class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        t=0
        poisonedSeconds = duration * len(timeSeries)
        
        for time in range(1,len(timeSeries)):
            timeInterval=timeSeries[time]
            timeInterval_prev=timeSeries[time-1]
            poisonedSeconds -= max(t, duration - (timeInterval - timeInterval_prev))
            
        return poisonedSeconds
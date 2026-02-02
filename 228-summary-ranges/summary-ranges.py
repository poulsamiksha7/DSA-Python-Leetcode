class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return []
        list1 = []
        i = 0
        start = None
        end = None
        while i < len(nums) - 1:
            if nums[i] + 1 == nums[i+1]:
                start = nums[i]
                while nums[i] + 1 == nums[i+1]:
                    i += 1
                    if i < len(nums) - 1:
                        continue
                    else:
                        break
                end = nums[i]
                list1.append(str(start)+'->'+str(end))
            else:
                list1.append(str(nums[i]))
            i += 1
        if end != nums[-1]:
            list1.append(str(nums[-1]))
        return list1
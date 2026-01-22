# 169
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return statistics.mode(nums)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for item in nums:
            if item in d:
                d[item]+=1
            else:
                d[item] = 1
        max_key = max(d, key=d.get)
        return max_key

# 1 
# O(n^2)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        
        while l < len(nums) - 1:
            r = l + 1
            
            while r < len(nums):
                if nums[l] + nums[r] == target:
                    return [l, r]
                r += 1
            
            l += 1
        
        return []

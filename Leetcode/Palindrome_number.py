# 9 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        o = x 
        if x < 0 :
            return False 
        reverse = 0 
        while x > 0 :
            d = x % 10 
            reverse = reverse * 10 + d
            x = x // 10 
        if o == reverse :
            return True 
        else: 
            return False 

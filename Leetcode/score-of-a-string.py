# 3110
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0 
        for i in range(0,len(s)-1):
            result+=abs(int(ord(s[i]))-int(ord(s[i+1])))
        return result

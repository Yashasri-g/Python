# 58
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = s.strip()
        ans = b[::-1]
        count=0
        for i in ans:
            if i==" ":
                return count 
                break
            else:
                count+=1
        return count

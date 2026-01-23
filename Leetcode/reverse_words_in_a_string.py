# 151 
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        r = len(s) - 1 
        l = len(s) - 1
        ans = []
        while r>=0:
            while r >= 0 and s[r]!=" ":
                r-=1
            ans.append(s[r+1:l+1])
            while r >= 0 and s[r] == " ":
                r -= 1
            l=r
        res = " ".join(ans)
        return res

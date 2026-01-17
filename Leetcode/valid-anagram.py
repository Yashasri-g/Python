# 242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sort_s = sorted(s)
            sort_t = sorted(t)
            result_s = "".join(sort_s)
            result_t = "".join(sort_t)
            if result_s == result_t:
                return True
            else:
                return False
        else:
            return False


# Solution 2 
if len(s)!=len(t):
            return False
count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Decrease count using t
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True

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

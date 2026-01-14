# 2469
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        F = celsius * 1.80 + 32
        k = celsius = celsius + 273.15
        ans.append(k)
        ans.append(F)
        return ans

class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = {}
        
        # Count occurrences
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Build result from 1 to n
        result = []
        for i in range(1, n + 1):
            if i in freq:
                result.append(freq[i])
            else:
                result.append(0)
                
        return result

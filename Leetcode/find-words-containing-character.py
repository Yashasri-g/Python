# 2942

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result = []
        for index,word in enumerate(words):
            if x in word:
                result.append(index)
        return result

  # Uses `enumerate` to get index and word, checks if character exists, and stores matching indices.

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        indices = []
        for i, word in enumerate(words):
            if x in word:
                indices.append(i)

        return indices
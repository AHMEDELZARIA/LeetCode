class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        num_words = 0
        for sentence in sentences:
            num_words = sentence.count(" ") + 1
            if (num_words > max_words):
                max_words = num_words

        return max_words
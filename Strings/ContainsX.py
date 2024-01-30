class ContainsX(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        indices = []
        words_len = len(words)
        
        for i in range(words_len):
            if x in words[i]:
                indices.append(i)

        return indices
              

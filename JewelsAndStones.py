class JewelsAndStones(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        num = 0
        for stone in stones:
            if stone in jewels: num += 1

        return num

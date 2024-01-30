class DefangingAnIPAddress(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        a_split = address.split('.')
        
        return '[.]'.join(a_split)

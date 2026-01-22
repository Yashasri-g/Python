#1108 
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        r = address.replace(".","[.]")
        return r

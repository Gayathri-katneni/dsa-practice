class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        # Convert to string and compare with its reverse
        return str(x) == str(x)[::-1]

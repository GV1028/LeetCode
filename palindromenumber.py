class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if int(str(abs(x))[::-1]) == abs(x):
            return True
        else:
            return False

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = ['I','V','X','L','C','D','M']
        val = [1,5,10,50,100,500,1000]
        dic = dict(zip(roman,val))
        stemp = list(s)
        val = 0
        i = 0
        while i<len(stemp):
            if i+1<len(stemp) and dic[s[i]] < dic[s[i+1]]:
                val += dic[s[i+1]] - dic[s[i]]
                i = i + 2
            else:
                val += dic[s[i]]
                i = i + 1
        return val

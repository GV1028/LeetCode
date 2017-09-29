class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows == 1:
            return s
        cycle = []
        n = numRows*2-2
        while n>=2:
            cycle.append(n)
            n = n-2
        cycle = cycle*(len(s))
        temp = []   
        s = list(s)
        sind = range(len(s))
        d = dict(zip(sind,cycle))
        i = 0
        while i<numRows:
            j = i
            while j<len(s):
                temp.append(s[j])
                j = j + cycle[j]
            i = i + 1    
        ans = ''.join(temp)
        return ans

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        inp = list(s)
        stack = []
        ope = ['(','[','{']
        clo = [')',']','}']
        d = dict(zip(ope,clo))
        if len(inp)%2!=0:
            return False
        if inp[0] in clo:
            return False
        for i in range(len(inp)):
            if inp[i] in ope:
                stack.append(inp[i])
            elif inp[i] in clo:
                if d[stack.pop()]!=inp[i]:
                    return False
        if not stack:
            return True
        else:
            return False

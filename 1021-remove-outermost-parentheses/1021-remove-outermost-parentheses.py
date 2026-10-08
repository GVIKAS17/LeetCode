class Solution(object):
    def removeOuterParentheses(self, s):
        res = []
        d = 0
        for ch in s:
            if ch == '(':
                if d > 0:
                    res.append(ch)
                d += 1
            else:
                d -= 1
                if d > 0:
                    res.append(ch)
        return "".join(res)
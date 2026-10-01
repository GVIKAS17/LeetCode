class Solution(object):
    def myPow(self, x, n):
        neg = 0
        if n < 0:
            neg = 1
            n = -n
        ans = 1
        
        while n > 0:
            if n %2 == 1:
                ans = ans * x
            x *= x
            n //= 2
        if neg:
            return 1 / ans
        return ans
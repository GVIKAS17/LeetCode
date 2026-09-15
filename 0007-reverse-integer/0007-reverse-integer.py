class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        t = 0

        while x:
            y = x % 10
            x = x // 10

            if t > 214748364 or (t == 214748364 and y > 7):
                return 0
            t = t * 10 + y
        return t * sign
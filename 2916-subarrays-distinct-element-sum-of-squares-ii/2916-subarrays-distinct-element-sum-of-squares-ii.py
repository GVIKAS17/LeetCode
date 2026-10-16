class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def _add(b, i, v):
            while i <= n + 1:
                b[i] += v
                i += i & -i

        def range_add(l, r, v):  
            _add(B1, l, v)
            _add(B1, r + 1, -v)
            _add(B2, l, v * (l - 1))
            _add(B2, r + 1, -v * r)

        def prefix(i):  # sum of d[1..i]
            s1 = s2 = 0
            k = i
            while k > 0:
                s1 += B1[k]
                s2 += B2[k]
                k -= k & -k
            return s1 * i - s2

        last = {}
        cur = 0
        ans = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)

            S = prefix(j) - prefix(p + 1)
            cur = (cur + 2 * S + (j - p)) % MOD

            range_add(p + 2, j + 1, 1)
            ans = (ans + cur) % MOD
            last[x] = j
        return ans
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        bit_count = [0] * 31

        for num in nums:
            for b in range(31):
                if num & (1 << b):
                    bit_count[b] += 1
        ans = 0

        for _ in range(k):
            num = 0
            for b in range(31):
                if bit_count[b] > 0:
                    num |= (1 << b)
                    bit_count[b] -= 1
            ans = (ans + num * num) % MOD
        return ans
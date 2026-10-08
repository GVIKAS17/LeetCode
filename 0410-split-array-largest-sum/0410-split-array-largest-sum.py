class Solution(object):
    def splitArray(self, nums, k):

        def can_split(max_sum):
            pieces = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > max_sum:
                    pieces += 1
                    current_sum = num
                else:
                    current_sum += num

            return pieces <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
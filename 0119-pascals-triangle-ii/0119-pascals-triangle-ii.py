class Solution(object):
    def getRow(self, nums):
        res = []
        for i in range(nums+1):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res[nums]
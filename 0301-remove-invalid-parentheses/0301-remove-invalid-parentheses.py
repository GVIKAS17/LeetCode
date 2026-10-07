class Solution(object):
    def removeInvalidParentheses(self, s):

        n = len(s)
        have = [set() for _ in range(n + 1)]
        have[0].add("")
        def better(a, b):
            if not a:
                return False
            if not b:
                return True
            len_a = len(next(iter(a)))
            len_b = len(next(iter(b)))
            if len_a + 1 > len_b:
                b.clear()
                return True
            return len_a + 1 == len_b

        for i in range(n):
            if s[i] == '(':
                for j in range(i + 1, 0, -1):
                    if better(have[j - 1], have[j]):
                        for t in have[j - 1]:
                            have[j].add(t + "(")
            elif s[i] == ')':
                for j in range(0, i + 1):
                    if better(have[j + 1], have[j]):
                        for t in have[j + 1]:
                            have[j].add(t + ")")
            else:
                for j in range(0, i + 2):
                    temp = set()
                    for t in have[j]:
                        temp.add(t + s[i])
                    have[j] = temp
        answer = []
        for t in have[0]:
            answer.append(t)
        return answer
class Solution(object):
    def rotateString(self, s, goal):
        a = s + s
        if len(s) != len(goal):
            return False
        if goal in a:
            return True
        return False
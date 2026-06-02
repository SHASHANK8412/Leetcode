class Solution(object):
    def largestEven(self, s):
        last = s.rfind('2')

        if last == -1:
            return ""

        return s[:last + 1]
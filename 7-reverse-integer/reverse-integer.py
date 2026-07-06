class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        rev = ""

        for i in s:
            rev = i + rev

        result = sign * int(rev)

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
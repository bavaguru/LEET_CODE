class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0

        sign = 1
        i = 0

        if s[0] == "-":
            sign = -1
            i = 1
        elif s[0] == "+":
            i = 1

        num = 0

        for j in range(i, len(s)):
            if s[j] >= '0' and s[j] <= '9':
                num = num * 10 + (ord(s[j]) - ord('0'))
            else:
                break

        num = num * sign

        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647

        return num
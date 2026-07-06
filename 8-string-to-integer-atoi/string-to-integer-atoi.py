class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num = num * sign

        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num
        
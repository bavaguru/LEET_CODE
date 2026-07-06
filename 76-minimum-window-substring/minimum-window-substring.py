class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        window = {}

        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        have = 0
        needCount = len(need)
        left = 0
        res = ""
        minLen = float("inf")

        for right in range(len(s)):
            ch = s[right]

            if ch in need:
                if ch in window:
                    window[ch] += 1
                else:
                    window[ch] = 1

                if window[ch] == need[ch]:
                    have += 1

            while have == needCount:

                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    res = s[left:right + 1]

                leftChar = s[left]

                if leftChar in need:
                    window[leftChar] -= 1

                    if window[leftChar] < need[leftChar]:
                        have -= 1

                left += 1

        return res
        
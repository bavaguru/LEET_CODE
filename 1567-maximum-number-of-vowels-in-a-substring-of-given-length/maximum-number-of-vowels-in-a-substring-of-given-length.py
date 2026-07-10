class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maximum = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1

            if count > maximum:
                maximum = count

        return maximum
        
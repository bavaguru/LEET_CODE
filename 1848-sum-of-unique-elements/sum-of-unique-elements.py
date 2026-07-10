class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        total = 0

        for num in freq:
            if freq[num] == 1:
                total += num

        return total
        
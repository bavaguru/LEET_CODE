class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            current = 0
            need = 1

            for weight in weights:
                if current + weight > mid:
                    need += 1
                    current = 0
                current += weight

            if need <= days:
                right = mid
            else:
                left = mid + 1

        return left
        
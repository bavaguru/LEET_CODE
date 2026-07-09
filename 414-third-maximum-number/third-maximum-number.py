class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        if len(nums) >= 3:
            return nums[2]
        return nums[0]
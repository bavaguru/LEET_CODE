class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)

        if ones == 0 or ones == 1:
            return 0

        nums = nums + nums

        count = 0

        for i in range(ones):
            count += nums[i]

        maximum = count

        for i in range(ones, len(nums)):
            count += nums[i]
            count -= nums[i - ones]

            if count > maximum:
                maximum = count

        return ones - maximum
        
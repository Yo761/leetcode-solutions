class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)
                window_sum -= nums[left]
                left += 1

        if min_length == float("inf"):
            return 0
        return min_length
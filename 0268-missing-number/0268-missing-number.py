class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_sum=0
        total=0
        missing=None
        for num in nums:
            nums_sum+=num
        for i in range(len(nums)+1):
            total+=i
        missing=total-nums_sum
        return missing
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current=0
        max_one=0
        for num in nums:
            if num == 1:
                current+=1
                max_one=max(max_one,current)
            else:
                current = 0
        return max_one
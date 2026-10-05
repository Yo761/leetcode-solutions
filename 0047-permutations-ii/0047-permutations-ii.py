class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ans = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for i in range(len(nums)):

                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return ans
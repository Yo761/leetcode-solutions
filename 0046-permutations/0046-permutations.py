class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        path=[]
        ans=[]
        def backtrack():
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack()
                path.pop()
        backtrack()
        return ans


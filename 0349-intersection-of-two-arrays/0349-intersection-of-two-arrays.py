class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        res = set()

        for num in nums2:
            if num in seen:
                res.add(num)

        return list(res)
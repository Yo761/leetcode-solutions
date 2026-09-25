class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        child=0
        cookies=0
        while child<len(g) and cookies<len(s):
            if s[cookies]>=g[child]:
                child+=1
            cookies+=1
        return child

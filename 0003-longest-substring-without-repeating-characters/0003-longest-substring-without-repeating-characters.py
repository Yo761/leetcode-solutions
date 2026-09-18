class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        max_lenght=0
        for right,char in enumerate(s):
            if char in seen:
                while char in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(char)
            max_lenght=max(max_lenght,len(seen))
        return max_lenght
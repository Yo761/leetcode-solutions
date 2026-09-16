class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for letter in s:
            if letter.isalnum():
                res+=letter.lower()
        i=0
        j=len(res)-1
        while i < j:
            if res[i] != res[j]:
                return False
            i+=1
            j-=1
        return True


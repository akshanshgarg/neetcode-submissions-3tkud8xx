class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = ''
        for i in s:
            if i.isalnum():
                newS += i.lower()
        
        srt, lst = 0, len(newS)-1
        while srt<=lst:
            if newS[srt] != newS[lst]:
                return False
            srt +=1
            lst -=1
        
        return True


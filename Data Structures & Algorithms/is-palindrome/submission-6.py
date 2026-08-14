class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for i in range(0, len(s)):
            if s[i].isalnum():
                n += s[i].lower()

        j = len(n) - 1

        for i in range(0, len(n)):
            if n[i].lower() != n[j].lower():
                return False
            if i == j:
                break
            j -= 1
        
        return True
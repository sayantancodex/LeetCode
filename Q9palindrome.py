class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        if temp[::-1] == temp:
            return True
        else:
            return False
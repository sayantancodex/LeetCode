class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        total = 0
        k = 0
        for i in range(len(usageLimits)):
            total += usageLimits[i]
            if total >= ((k+1)*(k+2)/2):
                k += 1
        return k        
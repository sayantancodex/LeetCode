class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            n = len(nums)
            nums.insert(n+1, target)
            nums.sort()
            return nums.index(target)
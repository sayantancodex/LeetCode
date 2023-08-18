class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            def binary_search_left(nums, target):
                left, right = 0, len(nums) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return left

            def binary_search_right(nums, target):
                left, right = 0, len(nums) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return right

            left_pos = binary_search_left(nums, target)
            right_pos = binary_search_right(nums, target)

            if left_pos <= right_pos:
                return [left_pos, right_pos]
            else:
                return [-1, -1]
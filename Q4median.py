class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1+nums2
        num3.sort()
        sum =0
        if len(num3) % 2 == 0:
            sum = num3[int(len(num3)/2)-1] + num3[int((len(num3)/2))]
            sum = sum/2
            return sum
        else:
            a = int(len(num3)/2)
            return num3[a]  
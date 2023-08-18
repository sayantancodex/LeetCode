class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        flag = 0 
        for i in range(len(grid)):
            a = grid[i]
            for j in range(len(a)):
                if a[j] < 0:
                    flag += 1
        return flag
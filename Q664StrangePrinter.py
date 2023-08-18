class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for length in range(n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = length + 1

                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        return dp[0][n - 1]
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def ascii_sum(s):
            return sum(ord(c) for c in s)

        # Lengths of the input strings
        len1, len2 = len(s1), len(s2)

        # Create a 2D DP table to store the LCS length for each substring
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Fill in the DP table to find LCS length
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Calculate the ASCII sum of the characters that need to be deleted
        sum_deleted = ascii_sum(s1) + ascii_sum(s2) - 2 * ascii_sum(s1[i] for i in range(dp[len1][len2]))

        # Return the minimum ASCII sum to make two strings equal
        return sum_deleted
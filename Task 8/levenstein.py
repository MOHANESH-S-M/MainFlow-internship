# This is Task 8
""" 57. Edit Distance (Levenshtein Distance)
 Objective      : Find the minimum number of operations (insertions, deletions, and substitutions) required to convert one string into another.
 Input          : Two strings.
 Output         : The minimum edit distance.
 Hint           : Use dynamic programming to solve this problem
 """
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

# Example usage:
print(edit_distance("kitten", "sitting"))  # Output: 3

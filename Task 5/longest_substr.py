# This is Task 5
"""36. Longest Increasing Subsequence (LIS)
 Objective     : Find the length of the longest increasing subsequence in an array.
 Input         : A list of integers.
 Output        : The length of the LIS.
 Hint          : Use dynamic programming with an auxiliary array to store lengths"""
def longest_subsequence(a):
    if not a:
        return 0
    dp = [1]*len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j]  <a[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_subsequence(nums))
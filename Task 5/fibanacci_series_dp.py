# This is Task 5
""" 34. N-th Fibonacci Number (Dynamic Programming)
 Objective     : Find the nnn-th Fibonacci number using dynamic programming for efficiency.
 Input         : An integer nnn.
 Output        : The nnn-th Fibonacci number.
 Hint          : Use a bottom-up approach with a memoization array."""
def fibonacci_series(n):
    if n <= 1 :
        return n
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
print("the 10th fibanacci number : ",fibonacci_series(10))
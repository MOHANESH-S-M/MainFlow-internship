# This is Task 6
""" 41. Knapsack Problem (0/1)
 Objective   : Solve the 0/1 knapsack problem using dynamic programming.
 Input       : A list of weights, a list of values, and a maximum capacity.
 Output      : The maximum value that can be carried within the capacity.
 Hint        : Use a dynamic programming table to keep track of the maximum values at each capacity"""

def knapsack(weights,value, capacity):
    n = len(weights)
    dp = [[0]* (capacity + 1 ) for i in range(n+1)]

    for i in range( 1,n+1):
        for w in range(1,capacity+1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i-1][w],values[i-1] +  + dp[i - 1][w - weights[i - 1]])
            else :
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Maximum value:", knapsack(weights, values, capacity))

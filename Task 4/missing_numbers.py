# This is Task 4
""" 25. Find Missing Number
 Objective       : Find the missing number in an array of size nnn, containing numbers 111 to n+1n+1n+1.
 Input           : A list of integers.
 Output          : The missing integer.
 Hint            : Use the sum formula Sum(n)=n(n+1)2\text{Sum}(n) = \frac{n(n+1)}{2}Sum(n)=2n(n+1) and subtract the sum of given numbers."""
def missing_number(arr):
    n = arr[-1]
    complete_sum = (n*(n+1))/2
    incomplete_sum = 0
    for i in arr:
        incomplete_sum += i
    return complete_sum - incomplete_sum
arr = [1,2,3,4,6,7,8,9]
print(missing_number(arr))

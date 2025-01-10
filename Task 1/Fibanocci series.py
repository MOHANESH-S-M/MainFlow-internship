#this is Task 1 question 4
""" 4. Fibonacci Sequence
 Objective  : Generate the first n numbers in the Fibonacci sequence (e.g., 0, 1, 1, 2, 3,5, ...).
 Input      : Integer n.
 Output     : List of n Fibonacci numbers.
 Hint       : Use a loop where F(n)=F(n−1)+F(n−2)F(n) = F(n-1) + F(n-2)F(n)=F(n−1)+F(n−2)."""
def fibonacci_sequence(n):
    if n <= 0:
        return []
    fib_list = [0,1]
    while len(fib_list)< n:
        nxt_fib = fib_list[-1]+fib_list[-2]
        fib_list.append(nxt_fib)
    return fib_list
i = int(input("enter the number"))
print(fibonacci_sequence(i))
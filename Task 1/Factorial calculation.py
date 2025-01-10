# this is Task 1 question 3
""" 3. Factorial Calculation
 Objective : Compute the factorial of a given number n
 Input     : A single integer n.
 Output    : Integer value of n!
 Hint      : Use a loop or math.factorial library."""
import math
def Factorial_calculation(x):
    result = 1
    if  x == 0:
        return 1
    if x > 0 :
        for i in range(1,x+1):

            result *= i
        return result
    else:
        print ("the entered number is not valid")

a=int (input("enter the number to get the factorial"))
if (math.factorial(a)== Factorial_calculation(a)):
    print( Factorial_calculation(a))
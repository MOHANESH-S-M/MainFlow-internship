#this is task 1 question 2
"""2. OddorEven
 Objective : Determine whether a number is odd or even.
 Input     : A single integer.
 Output    : "Odd" or "Even".
 Hint      : Check the remainder when divided by 2 (number % 2 == 0 for even)."""
def OddorEven(x):
    if (x % 2 == 0):
        print("the Number is Even")
    else:
        print("the Number is odd")
i = int(input("enter the value tofinrd the oddor even"))
OddorEven(i)

# this is task 3 question18
"""18. Swap Two Numbers
 Objective: Swap two numbers without using a third variable.
 Input: Two integers aaa and bbb.
 Output: Swapped values of aaa and bbb.
 Hint: Use arithmetic operations like addition and subtraction or XOR (a, b = b, a)."""
def swap_numbers(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b
print(swap_numbers(12,34))
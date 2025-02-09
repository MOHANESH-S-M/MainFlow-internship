# this is task3 question 20
""" 20. Decimal to Binary
 Objective: Convert a decimal number to its binary representation.
 Input: An integer nnn.
 Output: A string representing the binary equivalent.
 Hint: Use the bin() function or repeatedly divide nnn by 2, storing remainders."""
def decimal_2_binary(x):
    binary_return =""
    while x!=0:
        rem = x%2
        binary_return += str(rem)
        x = x// 2
    return int(binary_return)
print(decimal_2_binary(10))
#this istask 1 question number 8
""" 8. Armstrong Number
 Objective  : Check if a number equals the sum of its digits raised to the power of the number of digits.
 Input      : An integer nnn.
 Output     : True or False.
 Example    : 153 is an Armstrong number because 13+33=53+153 1^3 + 5^3 + 3^3 = 153 13+53+33=153.
 Hint       : Convert to a string to calculate the length and power."""
def amstrong_number(x):
    len_of_num = len(str(x))
    a = x
    result = 0
    while a > 0:
        rem = a%10
        result = result+(rem**len_of_num)
        a = a//10
    return result == x
print(amstrong_number(153))
print(amstrong_number(370))
print(amstrong_number(371))
print(amstrong_number(27458))
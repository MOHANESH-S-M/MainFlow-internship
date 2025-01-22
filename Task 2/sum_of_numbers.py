# this is Task 2 question 10
""" 10. Sum of Digits
 Objective   : Find the sum of the digits in a number.
 Input       : An integer nnn.
 Output      : Single integer, the sum of digits.
 Hint        : Convert the number to a string, iterate through characters, and sum up the digits."""
def sum_of_digits(number):
    a = str(number)
    result = 0
    for i in a:
        i = int(i)
        result+= i
    return result
print(sum_of_digits(122333))
print(sum_of_digits(344))
print(sum_of_digits(79786))
print(sum_of_digits(13))
print(sum_of_digits(456663))
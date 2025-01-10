#this is task1 question no 7
""" 7. Leap Year Check
 Objective  : Determine whether a year is a leap year.
 Input      : An integer year (e.g., 2024).
 Output     : True if leap year, otherwise False.
 Hint       : A year is a leap year if divisible by 4 but not by 100 unless divisible by 400."""
def leap_year_check(year):
    if year % 400 ==0 :
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print( "the given leap year ",.leap_year_check(400))
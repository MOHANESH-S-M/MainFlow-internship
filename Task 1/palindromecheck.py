#this is task 1 question 6
""" 6. Palindrome Check
 Objective  : Check if a string reads the same backward as forward.
 Input      : A string.
 Output     : True or False.
 Hint       : Compare the string with its reversed version."""
def palindromecheck(x):
    x_rev =""
    n = len(x)
    for i in range( n-1 ,-1 ,-1 ):
        x_rev+= x[i]
    return x == x_rev
print(palindromecheck("1234567654321"))
print(palindromecheck("abdjdndijldl"))
print(palindromecheck("racecar"))
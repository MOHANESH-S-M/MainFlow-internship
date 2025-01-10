# this is task 1 question no
""" 5. Reverse a String
 Objective : Reverse the characters in a string.
 Input     : A string
 Output    : The reversed string.
 Hint      : Use slicing ([::-1]) or loop through characters."""
def method1(x):
    a= x[::-1]
    return a
def method2(x):
    empty_str =""
    for i in range ( len(x)-1 ,-1,-1):
        empty_str += x[i]
    return empty_str
print(method2("hello"))
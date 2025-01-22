# this is task 2 question 9
""" 9. Prime Number
 Objective  : Determine if a number is prime.
 Input      : A single integer nnn.
 Output     : True if prime, otherwise False.
 Hint       : A prime number has no divisors other than 1 and itself; check divisors up to n\sqrt{n}n  """
def prime_number(number):
    if number <= 1:
      return False
    for i in range(2,(number//2)+1):
      if number%i == 0 :
         return False
    return True
    
number = int(input("enter the number"))
print(prime_number(number))
        
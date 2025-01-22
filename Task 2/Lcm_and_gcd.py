#this is task 2 question 11
""" 11. LCM and GCD
 Objective    : Calculate the Least Common Multiple (LCM) and Greatest Common Divisor(GCD) of two integers.
 Input        : Two integers aaa and bbb.
 Output       : Two integers: LCM and GCD of aaa and bbb.
 Hint         : Use the relationship LCM(a,b)=∣a⋅b∣GCD(a,b)\text{LCM}(a, b) = \frac{|a \cdotb|}{\text{GCD}(a, b)}LCM(a,b)=GCD(a,b)∣a⋅b∣ . Python's math.gcd() function can
                simplify this."""
import math
def lcm_and_gcd(a,b):
    Gcd = math.gcd(a,b)
    Lcm = abs(a*b)//Gcd
    print("LCM and GCD is {},{}".format(Lcm,Gcd))

lcm_and_gcd(23,44)
lcm_and_gcd(3,-23)
lcm_and_gcd(1,2)
lcm_and_gcd(10,100)

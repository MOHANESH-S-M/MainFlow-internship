# This is Task 4
""" 29. Check Pythagorean Triplet
 Objective  : Determine if three numbers form a Pythagorean triplet (e.g., a2+b2=c2a^2 + b^2 = c^2a2+b2=c2).
 Input      : Three integers aaa, bbb, ccc.
Output      : True if they form a triplet, otherwise False.
Hint        : Ensure ccc is the largest, then verify the equation."""
def pythagorean_triplet(a,b,c):
    a,b,c = sorted([a,b,c])
    return a**2 + b**2 == c**2
print(pythagorean_triplet(2,3,4))
print(pythagorean_triplet(3,4,5))
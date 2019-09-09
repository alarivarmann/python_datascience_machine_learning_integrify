from functools import reduce
import inspect

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a


gcd(-6,12)

def high_dim_gcd(args = []):
    from functools import reduce
    if all(isinstance(el,(int,float)) for el in args):
        return reduce(gcd, args)
    else :
        return "Undefined"


print(high_dim_gcd([-2,4,6,3]))
# DEMONSTRATION OF REDUCE


gcd_tester = lambda a,b: "gcd(%s,%s)" % (a,b)
print(reduce(gcd_tester, range(0,5)))



def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)

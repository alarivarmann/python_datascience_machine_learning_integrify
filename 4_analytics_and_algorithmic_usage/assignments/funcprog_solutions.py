# FUNCTIONAL PROGRAMMING SOLUTIONS

## Task 1 : High-dim lowest common multiple
def high_dim_gcd(*args):
    from functools import reduce
    if all(isinstance(el,(int,float)) for el in args):
        return reduce(gcd, args)
    else :
        return "Undefined"


print(high_dim_gcd(-2,4,6,8))


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)

## Task 2 : Reversion

def reverseList(L):

    # Empty list
    if len(L) == 0:
        return

    # List with one element
    if len(L) == 1:

        # Check if that's a list
        if isinstance(L[0], list):
            return [reverseList(L[0])]
        else:
            return L

    # List has more elements
    else:
        # Get the reversed version of first list as well as the first element
        return reverseList(L[1:]) + reverseList(L[:1])





list2d = [[1,2],[3,4],[5,6],[7,8]]

list3d = [list2d, [[0,2],[3,4],[5,6],[7,8]]]

list4d = [list3d, list(reversed(list3d))]

## Task 3 : Decorator as a CLASS
class my_decorator(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()

## Task 5 : Simple Functional decorator
from functools import reduce
r = lambda x,y:x+y
def test(args,lambda_expr=r):
    print(reduce(lambda_expr,args))

## Task 5 : Delay DECORATORS
from functools import wraps
from time import sleep
from threading import Timer

def delay(timer,seconds):
    def inner(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fun.__name__))
            sleep(timer)
            fun(*args, **kwargs)
            print(f"Now sleeping again, now by {seconds} amount")
            t = Timer(seconds, fun, args, kwargs)
            return t.start()
        return wrapper
    return inner



@delay(4,2)
def print_first_four():
    x = range(3)
    print(x)

print_first_four()

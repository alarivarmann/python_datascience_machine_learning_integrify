


from time import sleep

# 
def inc(x):
    sleep(1)
    return x + 1

def add(x, y):
    sleep(1)
    return x + y


# TASK 1 : WRITE A DECORATOR TO MEASURE TIME of function execution. DO NOT USE GOOGLE.


# Introduce delayed decorator

# This takes three seconds to run because we call each function sequentially, one after the other

x = inc(1)
y = inc(2)
z = add(x, y)


Those two increment calls *could* be called in parallel, because they are totally independent of one-another.

We'll transform the `inc` and `add` functions using the `dask.delayed` function. When we call the delayed version by passing the arguments, exactly as before, but the original function isn't actually called yet - which is why the cell execution finishes very quickly.
Instead, a *delayed object* is made, which keeps track of the function to call and the arguments to pass to it.

from dask import delayed
# This runs immediately, all it does is build a graph

x = delayed(inc)(1)
y = delayed(inc)(2)
z = delayed(add)(x, y)

# and this command runs faster than the sequential version of the three commands separately
 z.compute()

z.visualize()

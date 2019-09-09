# learn about two libraries : itertools and collections

import itertools
list2d = [[1,2,3],[4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d))
merged2 = list(itertools.chain.from_iterable(list2d))
fl = lambda l: [item for sublist in list2d for item in sublist]
fl(list2d)

# goal is to write a program inputting two lists where the 2nd list element is an exponent to the first list element
power = lambda x,y : print(list(a**b for a,b in zip(x,y)))

# why does this work?
power({0:1,1:2,2:3},(2,3,0))

list2d.reverse()

# how to reverse lists recursively?
# inplace operation : doesn't return anything, changes the input data directly
fl = lambda l: print([sublist for sublist in list2d[::-1] for item in sublist[::-1]])
fl(list2d)

try_one = lambda list2d: list(reversed(sublist)for sublist in reversed(list2d))

try_two = lambda l : [list(reversed(el)) if isinstance(el,list) else el for el in reversed(l)]

co = lambda l: [i+1 if isinstance(i,int) else list(map(lambda j: j+1,i))for i in l]
bo = co(list2d)
list3d = [list2d,bo]

# use remove for removing element from list, but pop to remove an element at a specific index
a = [1,2,3]
lambda l : l.pop(0)

a = [1,2,3]
lambda l : l.remove(0)

# what's the difference ?

a.sorted()
print(a)

# sorted actually returns a list, but reversed returns a lambda expression
# verify:
reversed(a)

### DIFFERENT FROM LIST, TUPLE IS IMMUTABLE! ###
# Default behaviour of + is concatenation [1]+[1] is [1,1], same with tuples
c = tuple([1,2,3]) # doesnt behave the same way as ([1,2,3])
print(([1,2,3])==tuple([1,2,3])) # will print False

# to cast something into a tuple, use tuple(). () doesn't always convert the data type to tuple
type([(1)]*5) # will be a list

# So Tuple is actually defined by "(something,)" structure
# booleans can be used in power expressions
# lists and tuples can be interchanged
# strings cannot be exponentiated
#


def test(l):
    return [item for sublist in l for item in sublist],1,2

li,__, ___ = test(list2d)


d = {1:2}
d[1]=3 # setter

print(d)

# By default, when you loop through a dictionary, you will get the keys:
[print(k) for k in d] # will print the key but it will introduce some anomalies in the end
# never print inside a list

for k,v in d.items():
    print(v)

# del deletes a value, no return
# pop deletes a value at an index, returns it also
# remove doesn't exist in a dictionary, but pop removes the item associated with the key passed as argument to pop

# there is also a popitem method that pops the last item in the dictionary

import collections

d = {}
d['a'] = 'A'
d['b'] = 'B'
d['f'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

e = d
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['f'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

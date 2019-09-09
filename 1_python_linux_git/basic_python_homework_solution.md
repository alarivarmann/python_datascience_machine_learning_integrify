

```python
# 1
le_list = [1,2,3,4,5,6,7,8,9]

# 1.1
print(le_list[4])

# 1.2
print(le_list[-4])

# 1.3
print(le_list[::2])

# 1.4
print(le_list[3:6])
```

    5
    6
    [1, 3, 5, 7, 9]
    [4, 5, 6]



```python
# 2
le_dict = {'foo': {'name': 'Foo', 'lastname': 'Fooer'}, 'bar': {'name': 'Bar', 'lastname': 'Baer'}, 'Baz': None}

# 2.1
print(le_dict.keys())

# 2.2
print("Firstname is {}, and lastname is {}".format(le_dict.get('bar').get('name'), le_dict.get('bar').get('lastname')))

# 2.3
for k,v in le_dict.items():
    if v is not None:
        print("Firstname is {}, and lastname is {}".format(v.get('name'), v.get('lastname')))
```

    dict_keys(['foo', 'bar', 'Baz'])
    Firstname is Bar, and lastname is Baer
    Firstname is Foo, and lastname is Fooer
    Firstname is Bar, and lastname is Baer



```python
# 3
# 3.1
def summer(a, b):
    return a + b

# 3.2
def summer(a=1, b=2):
    return a + b

# 3.3
def summer(a=1, b=2, **kwargs):
    if 'negatove' in kwargs and kwargs.get('negatove') is True:
        return (a + b) * -1

    return a + b
```


```python
# 4
le_list = ['python', 'and', 'data', 'science', 'is', 'awesome']

# 4.1
new_list = [i for i in le_list if len(i) > 5]
# => ['python', 'science', 'awesome']

# 4.2
new_dict = {k: v for k,v in enumerate(le_list)}
# => {0: 'python', 1: 'and', 2: 'data', 3: 'science', 4: 'is', 5: 'awesome'}

# 4.3
new_dict.update({5: '!'})
# => {0: 'python', 1: 'and', 2: 'data', 3: 'science', 4: 'is', 5: '!'}
```


```python
# 5

def number_parser(list_param=[]):
    new_list = [i for i in list_param if isinstance(i, int) and i > 0 and not isinstance(i, bool)]

    return sorted(new_list, reverse=True)
```

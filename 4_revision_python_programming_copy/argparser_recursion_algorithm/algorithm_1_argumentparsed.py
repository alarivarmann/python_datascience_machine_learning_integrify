# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:28:03 2019

@author: alari
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import argparse
import sys
sys.setrecursionlimit(100)
# Mood: https://www.youtube.com/watch?v=2vjPBrBU-TM

def recursive_function(args):
    #n = int(args.start)
    n = args.start # because of argumentparser data type setting, we don't need type conversion here
    k = args.threshold # because of argumentparser data type setting, we don't need type conversion here
       
    if n >= k:
        print("\nNow the sub-program will be run")
        swing_n(args)

    elif n < k:
        print("\nThe current value of n is: {}".format(n))
        print(f"\n Now the value of n is increased with one recursive call by the amount {k-n},\n")
        n += k-n
        print(f"Now the value of n is {n}")
        args.start = n
        return recursive_function(args)


def swing_once(chandelier="chammak challo"):
    return f"from the \n {chandelier} \n"

def swing(chandelier = "chammak_make_me_more_sensible",line = "\n"):
    print(f"I wanna swiiiiing.... {swing_once(chandelier)}, {swing_once(chandelier)}, I....\n Want to take a new {line}, take a new {line} {line} I... ")

def swing_n(args,line = "\n"):  
    i = 0
    while i < args.start:
        print(f"How many times, or more accurately, {i+1} times do I have to tell you that \n")
        swing()
        i+=1

def self_handle(func):
    def wrapper(*args, **kwargs):
        print(func.__doc__)
        return func( *args, **kwargs)
        #return func(func, *args, **kwargs)
    return wrapper

@self_handle
def main():
    """ Recursion and Argumentparser Demo program. When user gives argument -r with the value y, the program will be run and
    the recursive increment for the input number, specified by -s value, will be increased up to -t value.
    Otherwise, if the value of -r is not y, the program will exit with the error code 1"""
    print(main.__doc__)
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--run", default="y", type=str,help="y for running the program, n for not")
    parser.add_argument("-c","--swing", default="chammak challo", type = str, help="Where you swing from")
    parser.add_argument("-s","--start",default = 5, type = int, help = "Value to start the program from")
    parser.add_argument("-t","--threshold", default = 8, type = int, help = "Threshold value for running the sub-program")
    args = parser.parse_args()
    print(args)
    
    if args.run == "y":
        recursive_function(args)
    else:
        sys.exit(1)
        # read more about the SYS module here : https://python101.pythonlibrary.org/chapter20_sys.html


if __name__ == "__main__":
    main()
    
    



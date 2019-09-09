# -*- coding: utf-8 -*-
import argparse
# Mood: https://www.youtube.com/watch?v=2vjPBrBU-TM

def recursive_function(n,k):

    if n >= k:
        print("Now the sub-program will be run")
        swing()

    elif n < k:
        print('The current value of n is: {}\n'.format(n))
        print(f"\n Now the value of n is increased with one recursive call by the amount {k-n}")
        n += k-n
        print(f"Now the value of n is {n}")
        return recursive_function(n,k)


def val_input(n,k):
    return isinstance(n, int) and isinstance(k, int)


def swing_once(chandelier="chammak challo"):
    return f"from the \n {chandelier} \n"

def swing(line = "\n"):
    print(f"I wanna swiiiiing.... {swing_once()}, {swing_once()}, I....\n Want to take a new {line}, take a new {line} {line} I... ")
    
def get_user_inputs_recursively():
    try:
        print("Please only enter two natural numbers between 0 and 10. \n \
              The first one is used as a starting value, and the other one as the threshold value for executing sub-program, \
              the other as the threshold value for executing the sub-program")
        line = input("Please only enter whole numbers between 0 and 10, separated by space ")
        unpacked = line.split(" ")
        n,k = list(map(lambda x : int(x),unpacked))
        while not val_input(n,k):
            line = input("Please only enter whole numbers between 0 and 10, separated by space ")
            unpacked = line.split(" ")
            n,k = list(map(lambda x : int(x),unpacked))
        return n,k
    except ValueError:
        print("Invalid entry, try again.")
        return get_user_inputs_recursively()


def main():

    should_i_run = input("Would you like to run the program? Y/N  ").lower()
    extracted = should_i_run[0]
    while (extracted == 'y' or extracted == 'n'):
        extracted = input("Please select whether you would like to continue. Enter \"Y\" or \"N\"  ").lower()
    if extracted == 'y':
        n,k = get_user_inputs_recursively()
        recursive_function(n,k)
    else:
        return 0


if __name__ == "__main__":
    """ Recursion and Argumentparser Demo program. When user gives argument -r with the value y, the program will be run and
    the recursive increment for the input number, specified by -s value, will be increased up to -t value.
    Otherwise, if the value of -r is not y, the program will exit with the error code 1"""
    main()
    
#TASK 1 : Introduce ArgumentParser into the program.
#
#The argumentparser asks the user for 4 arguments : 
#--run : y for running the program, n for not
#--swing : Where you swing from
#--start : Starting value argument
#--threshold : Threshold value. When the threshold value is met, the sub-program is run.



# =============================================================================
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('name',
# help='name of user'
# )
# parser.add_argument('-g', '--greeting',
# default='Hello',
# help='optional alternate greeting'
# )
# args = parser.parse_args()
# print("{greeting}, {name}!".format(
# greeting=args.greeting,
# name=args.name)
# )
# =============================================================================
        

#TASK 2 : Self-referencing decorator
    
#Write and apply a decorator `self_handle` that allows to print the documentation of main inside the main program


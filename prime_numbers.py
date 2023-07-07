#!/usr/bin/env python3

"""
Module to find prime numbers and write them
to a file 
"""

def is_prime(num):
    for n in range(1, num+1):
        if n != 1 and n != num and num % n == 0:
            return False
    return True


def find_prime_numbers(number):
    """
    find prime numbers between 0 and number
    Args:
        number (int): the maximum number + 1
    Returns:
        None
    """
    with open("results.txt", "w") as file:
        for number in range(1, number):
            if is_prime(number):
                file.write("{}\n".format(str(number)))

if __name__ == "__main__":
    find_prime_numbers(260)
    find_prime_numbers(250)
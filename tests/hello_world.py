#!/usr/bin/env python3

"""
Moduule to hold to learn
Introduction to progrogramming in python
"""


def say_hi(name):
    """
    function to say hi
    Args:
        name (str): name to say hi to
    Returns:
        string
    """
    return f"Hi {name}"
    
    
if __name__ == "__main__":
    print(say_hi('John Doe'))
    
    
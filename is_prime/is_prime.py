# Author : Asem Antar Abdesamee
# Problem Description:
"""
Define a function that takes an integer argument and returns logical value true or false 
depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 
that has no positive divisors other than 1 and itself.

#Examples:
is_prime(1)  --> false 
is_prime(2)  --> true  
is_prime(-1) --> false 
"""


"""
====================================
My Solution
====================================
"""




import math
def is_prime(num):
    if num <= 1:
        return False
    if num > 3:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
    return True


"""
====================================
Shorter Solution
====================================
"""


def is_prime2(num):
    return num > 1 and all(num % div for div in range(2, int(math.sqrt(num)) + 1))

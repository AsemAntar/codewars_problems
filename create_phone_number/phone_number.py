# Author: Asem Antar Abdesamee
# Problem Description:
"""
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

Example: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) --> (123) 456-7890
"""

'''
============================
My Solution
============================
'''


def create_phone_number(n):
    if len(n) > 10 or len(n) < 10:
        print('Please: enter 10 digit list only!')
        return False
    else:
        return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


'''
============================
Better Solutions
============================
'''


def create_phone_numbers(n):
    print('Constraints: Enter exactly 10 digits array')
    if len(n) > 10 or len(n) < 10:
        print('Please: enter 10 digit list only!')
        return False
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)


print(create_phone_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

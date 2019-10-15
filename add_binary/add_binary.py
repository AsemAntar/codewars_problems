def add_binary(a, b):
    sum = a + b
    return bin(sum)[2:]


'''
====================================================================================================
- writing the same function without the builtin bin method.
- Here we will follow a brute force approach.
- we follow the following method:
--> divide the sum by 2 and ignore the remainder and keep doing this for all the resulted numbers 
    until we reach 1
--> for the original sum and its following division numbers :
    --> add 1 if the number is odd.
    --> add 0 if the number is even.
====================================================================================================
'''


def addBinary(a, b):
    sum = a + b
    bi = ''
    while sum != 0:
        if sum % 2 == 0:
            bi = '0' + bi
            sum = sum // 2
        else:
            bi = '1' + bi
            sum = sum // 2
    return bi

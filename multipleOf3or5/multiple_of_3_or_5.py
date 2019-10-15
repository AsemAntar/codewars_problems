# Author : Asem Antar
# Date   : Oct-15-2019
# Problem Description:
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns 
the sum of all the multiples of 3 or 5 below the number passed in.
Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def solutions(number):
    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum


'''
============================
Shorter solution 
============================
'''


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


'''
the above solutions running time is O(n),
if found another solution which relied on math and its running time is O(1)
============================
Clever Math solution 
============================
'''


def math_solution(number):
    # count all the divisible by 3 numbers
    a3 = (number-1)//3
    # count all the divisible by 5 numbers
    a5 = (number-1)//5
    # count all the divisible by 15 numbers
    a15 = (number-1)//15

    # sum of all number divisble by 3
    sum_a3 = (a3*(a3+1)//2)*3
    # sum of all number divisble by 5
    sum_a5 = (a5*(a5+1)//2)*5
    # sum of all number divisble by 15
    sum_a15 = (a15*(a15+1)//2)*15

    # Numbers that are divisble by 15 are in common with those divisble by 3 and 5
    # so we need to subtract them as in the problem specification that stated
    # we need to include only one divisible
    result = sum_a3 + sum_a5 - sum_a15
    return result


'''
Where this formula comes from:
visit this link to see some explanation of a similar problem
https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000

Also see Arthimetric Progression Series on Khan Academy
'''

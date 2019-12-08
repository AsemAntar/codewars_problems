# Author : Asem Antar Abdesamee
# Problem Description:
"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters 
then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


"""
====================================
My Solution
====================================
"""




import re
def solution(s):
    sol = []
    while s:
        if len(s) % 2 == 0:
            sol.append(s[:2])
            s = s[2:]
        else:
            s += '_'
            sol.append(s[:2])
            s = s[2:]
    return sol


"""
====================================
Better Solution
====================================
"""


def solution2(s):
    return re.findall(".{2}", s + "_")


print(solution2('abcde'))

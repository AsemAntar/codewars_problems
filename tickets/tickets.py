# Author : Asem Antar Abdesamee
# Problem Description:
"""
The new "Avengers" movie has just been released! 
There are a lot of people at the cinema box office standing in a huge line. 
Each of them has a single 100, 50 or 25 dollar bill. 
An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. 
He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially 
has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change 
with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) => YES 
tickets([25, 100]) => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)


scenario 1 (Return Yes):
There is a queue contains 3 people, they have 25, 25 and 50 dollars,
now the first one will go to vasaya to buy a ticket, he will give him 25 dollars and get a ticket,
now vasaya has 25 dollars in the cashier, the next person pays also 25 dollars and get the ticket, 
now vasya has 50 dollars in the cahsier of 25 cuurency, the third person pays 50 dollars, get the ticket 
and recieves the change which is 25 dollars

consider another scenario (Return No):
[25, 50, 50]
first one pays 25 and get the ticket, second one pays 50 and get the ticket and the change,
third one can't pay 50 because now vasya has no money to give him back . 
"""


"""
====================================
My Solution
====================================
"""


def tickets(people):
    '''
    People: a list of bills people have in the queue
    '''
    casheir = {25: 0, 50: 0, 100: 0}

    for bill in people:
        if bill == 25:
            casheir[25] += 1
        elif bill == 50 and casheir[25] >= 1:
            casheir[50] += 1
            casheir[25] -= 1
        elif bill == 100 and casheir[25] >= 1 and casheir[50] >= 1:
            casheir[50] -= 1
            casheir[25] -= 1
        elif bill == 100 and casheir[25] >= 3:
            casheir[25] -= 3
        else:
            return 'NO'

    return 'YES'


print(tickets([25, 25, 25, 25, 50, 100, 50]))

"""
Algorithm Challenges 2/9/2018
520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Answer: 232,792,560


Checks for divisibility by range between 11 and 21

"""

def Div(number):
    for i in range(11, 21):
        if number % i != 0:
            return False
    return True

n = 2520

while not Div(n):
    n += 2520

print(n)

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
Answer: 906609 (993 x 913)"""

def Palin(c):
    return int(str(c)[::-1]) == c

largest_palin = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        product = a * b
        if Palin(product) and product > largest_palin:
            largest_palin = product

print(largest_palin)

"""
Write a program in Python that prints out all lines of 99 Bottles of Beer all the way down to zero.
Example: “99 Bottles of beer, take one down, pass it around, 98 bottles of beer on the wall”
However, for numbers that are multiples of 7, replace beer with Miller
And for numbers that are multiples of 5, replace beer with Lite beer
Lastly, for numbers that are multiples of 7 and 5, replace beer with Miller Lite
You are welcome to take creative liberty with the beer brands, or replace it with soft drinks."""


def Beer(number):
    if number % 7 == 0 and number % 5 == 0:
        return 'Miller Lite'
    elif number % 7 == 0:
        return 'Miller'
    elif number % 5 == 0:
        return 'Lite beer'
    else:
        return "beer"

i = 99

while i > 0:
    print(f"{i} bottles of {Beer(i)} on the wall, {i} bottles of {Beer(i)}, take one down pass it around,")
    i -= 1
for i in range(1):
    print("no more beer on the wall!")

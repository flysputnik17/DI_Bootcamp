# Exercise 1 : Double Dice
# Instructions
# Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.

# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).

# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# For example:

# If the results of the throws were as follows (your code would do 100 doubles, not just 3):
# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)

# Then my output would show something like this:
# Total throws: 8
# Average throws to reach doubles: 2.67.


import random
import functools


def throw_dice():
    return random.randrange(1, 6)


def throw_until_doubles():

    throw_arr = []
    counter = 0

    while True:
        r1 = throw_dice()
        r2 = throw_dice()

        counter += 1

        if r1 == r2:
            break

    return counter


def main(num=100):

    l1 = [throw_until_doubles() for i in range(0, num)]

    counter = functools.reduce(lambda a, b: a+b, l1)
    print("Average throws to reach doubles: %.2f" %
          round((counter / len(l1)), 2))

    return counter


print(f"Total throws: {main()}")

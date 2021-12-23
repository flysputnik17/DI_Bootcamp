# Exercise 1: Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
#
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
#
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
#
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
#
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


import random

def main():
     user_input = input('enter a season')
     if user_input == 'summer':
         print('at the moment ', get_random_temp())
     elif user_input == 'fall':
         print('at the moment ', get_random_temp())
     elif user_input == 'winter':
         print('at the moment ', get_random_temp())


    def get_random_temp():
       return random.randrange(-10, 40)

    if -10 < get_random_temp()<16:
        print('its winter')
    elif 16<get_random_temp()<24:
        print('its maybe spring or fall')
    else:
        print('its summer')
    get_random_temp()

    print('The temperature right now is' , get_random_temp(), 'degrees Celsius')

    if get_random_temp() < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0 < get_random_temp() < 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16 < get_random_temp() < 23:
        print('its nice put a jacket')
    elif 24 < get_random_temp() < 32:
        print('well the summer is in the town')
    elif 32 < get_random_temp() < 40:
        print('its hot like in hell drink water')


main()

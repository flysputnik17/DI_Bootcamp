# # Exercise 1 : What Are You Learning ?
# # Instructions
# # Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# # Call the function, and make sure the message displays correctly.
#
# def display_mess():
#     print('trying to learn how to make a funck in python')
#
#
# display_mess()



# # Exercise 2: What’s Your Favorite Book ?
# # Instructions
# # Write a function called favorite_book() that accepts one parameter called title.
# # The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# # Call the function, make sure to include a book title as an argument when calling the function.
#
# def favorite_book():
#     x = input('what is yor favorite_book title?  ')
#     print(f'my favorite_book is  {x}')
#
# favorite_book()


# # Exercise 3 : Some Geography
# # Instructions
# # Write a function called describe_city() that accepts the name of a city and its country as parameters.
# # The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# # Give the country parameter a default value.
# # Call your function.
#
#
# def describe_city():
#     city = input('enter the city name ')
#     country = input('enter the country name ')
#     print(f'the city {city} is in {country}')
#
# describe_city()


# # Exercise 4 : Random
# # Instructions
# # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# # Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
#
# import random
#
# def nummbers():
#     num = range(1,100)
#     for n in num:
#         print(num)
#     random_num = random.randint(1,100)
#     if num == random_num:
#         print('success')
#     else:
#         print('maybe nex time')
#
#
# print(nummbers())


# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.


# def make_shirt(size, shirttetx,big):
#     if big == 'big':
#         print('you order a big shirt size and the text is I LOVE PYTHON')
#     else:
#         print(f'your shirt size is  {size} and the text on it sayes {shirttetx}')
#
#
#
#
# # make_shirt(size = input('enter the size of the shirt you want'), shirttetx = input('enter the text you want on your shirt'))
# make_shirt(big=input(), size = input('enter the size of the shirt you want'), shirttetx = input('enter the text you want on your shirt'))



# # Exercise 6 : Magicians …
# # Instructions
# # Make a list of magician’s names.
# # Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# # Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# # Call the function make_great().
# # Call the funcyion show_magicians() to see that the list has actually been modified.
#
# magician = ['pavel','yana','sthich','gudini']
# def show_magicians():
#     print(magician)
# def make_great():
#     for x in magician:
#         print('the graet',x)
# make_great()
# show_magicians()
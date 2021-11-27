
# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_nummbers = [1, 2, 3, 4, 5, 6, 7]
my_fav_nummbers.append(9)
my_fav_nummbers.append(8)
print(my_fav_nummbers)
my_fav_nummbers.remove(5)
print(my_fav_nummbers)
friend_fav_numbers = [10, 12, 13, 14, 15, 16]
my_and_friend_fav_nummbers = friend_fav_numbers + my_fav_nummbers
print(my_and_friend_fav_nummbers)


# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# Answers. No, you can't because tuples are immutable and therefore the sum can not be modified. You will have to create a new tuple

# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

numbers = range(1, 20)
for numbers in numbers:
    print(numbers)

# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence)

# The Python float() method converts a number stored in a string or integer into a floating point number, or a number with a decimal point. Python floats are useful for any function that requires precision, like scientific notation. ... While floats can contain decimals, integers cannot
# Integers and floats are two different kinds of numerical data. An integer (more commonly called an int) is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place. Floats are used when more precision is needed.


# Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("kiwi")
basket.insert(0, "Apples")
# count num of appels in basket
count = basket.count("Apples")
print("the numbers of Apples in basket is:", count)
print(basket)
basket.clear()
print(basket)


# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = ""
while name != "PAVEL":
    name = input("please enter name")
print("thats the we are loooking for name")

# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.

elem = [1, 2, 3, "pavel", "godzila", "lary", 678]
while elem.index =
print(elem)   didnt make it \@ _@/

Exercise 8
Instructions
Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
nl = []
for x in range(1500, 2500):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
print(','.join(nl))


Exercise 9: Favorite Fruits
Instructions
Ask the user to input their favorite fruit(s)(one or several fruits).
Hint: Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list(convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_Fruits = input("please enter your fav Fruits")


def convert(fav_Fruits):
    return (fav_Fruits[0].split())


fav_Fruits = ["apple mango cherry"]
print(convert(fav_Fruits))


user_fruit = input("please enter any froiuit name")
if user_fruit == fav_Fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


pizza = input("please enter how much topping do you want")
while pizza == 5:
    print("my friend its the max of topping")
    if pizza == "quit":
        break
    print("ok")


# Exercise 1 : Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
combo_list = [*list_1, *list_2]
print(combo_list)


# Exercise 2: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.


numbers_1 = input("please enter  number")
numbers_2 = input("please enter  number")
numbers_3 = input("please enter  number")
if (numbers_1 >= numbers_2) and (numbers_1 >= numbers_3):
    largest = numbers_1
elif (numbers_2 >= numbers_1) and (numbers_2 >= numbers_3):
    largest = numbers_2
else:
    largest = numbers_2

print("The largest number is", largest)


# Exercise 4 :
# Instructions
# Using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("enter your name")
if (user_name == names):
    print("you cannot use this login for your cahrcter")


# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.

kid_ticket = 10
adult_ticket = 15
todler_ticket = "free entry for kids  under 3 years old"


while True:
    user_order_ticket = int(
        input("please enter how many tickets you want"))
    if user_order_ticket <= 1:
        print("okey only one ticket")
    elif user_order_ticket > 1:
        name_members = print(
            input("okey please enter the names of the members (enter done when done)"))
    elif name_members == "done":

kid_ticket = 10
adult_ticket = 15
todler_ticket = "free entry for kids  under 3 years old"
numbers_tickets = int(input("how many tickets are you want to order?"))
names_members = []

if numbers_tickets <= 1:
    print("okey only 1 ticket")
if numbers_tickets > 1:
    names_members = print(
        input("please enter the names of the members(enter done when done)"))
    continue

else:
    print("okey please enter the age's of the memmbers")

costumer_age = int(input("please enter your age to order a ticket"))
if 3 <= costumer_age <= 12:
    print(kid_ticket)
if 12 < costumer_age < 99:
    print(adult_ticket)
if costumer_age < 3:
    print(todler_ticket)


#         Exercise 1 : Concatenate Lists
Instructions
Write code that concatenates two lists together without using the + sign.

test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

# using naive method to concat
for i in test_list2:
    test_list1.append(i)

# Printing concatenated list
print("Concatenated list using naive method : "
      + str(test_list1))


# Exercise 2: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.

num_1 = input("enter yor number bettwen 0-99")
num_2 = input("enter yor number bettwen 0-99")
num_3 = input("enter yor number bettwen 0-99")
if num_1 > num_2 and num_1 > num_3:
    print(num_1+"is the biggest")
elif num_2 > num_1 and num_2 > num_3:
    print(num_2 + "is the biggest")
elif num_3 > num_1 and num_3 > num_2:
    print(num_3 + "is the biggest")


# Exercise 4 :
# Instructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.

# from os import name


names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
use_name = input("enter your name")
if use_name == names:
    print("this login is alradey in use ")


# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.

kid_ticket = 10
adult_ticket = 15
while True:
    age_of_custumer = int(input("pleas enter the age of the costumer: "))
    if age_of_custumer <= 3:
        print("the ticket if free ")
    if 3 < age_of_custumer <= 12:
        print("the ticket will cost", kid_ticket)
    if age_of_custumer > 12:
        print("the ticket will cost", adult_ticket)
    if age_of_custumer == 100:
        continue

    print("okey now we will colculate the tottal cost")
    total_order = sum(age_of_custumer)


def Convert(string):
    li = list(string.split(" "))
    return li


# Driver code
str1 = "34,67,55,33,12,98"
print(Convert(str1))

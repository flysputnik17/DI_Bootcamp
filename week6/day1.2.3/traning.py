fruits = ["Apple", "Banana", "Kiwi", "Mango"]

# various len functions
print(len(fruits))
fruits.append("Melon")
fruits.remove("Banana")
print(fruits)

numbers = range(1, 100000)
summ = sum(numbers)
print(summ)

numbers = [77, 55, 2, 3, 5, 0, 9999]
sor_num = sorted(numbers)
print(sor_num)

leters = ["q", "s", "a", "g", "b", "c", "d"]
sor_leter = sorted(leters)
print(sor_leter)

note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)


list1 = [5, 10, 15, 20, 25, 50, 20]
list1.remove(20)
list1.insert(3, 200)
print(list1)


frut = ["banna", "apple", "kiwi", "pear"]
for fruti in frut:
    print("i real like to eat", fruti)

numbers = range(4, 22)
for number in numbers:
    print(number)
numbers = list(range(4, 22))
print(numbers)


curent_number = 1
while curent_number < 5:
    print(curent_number)
    curent_number += 1

print("finished")

password = " "
while password != "hello-world-123":
    password = input("what is the top secret password?")

print("you gussed the right password!")
number = 1
while number < 11:
    print(number)
    number += 1


active = True

while active:
    city = input(
        "Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")

order = True
while order:
    number_of_orders = input(
        "what do you want to buy?(enter 'done' when you are finishd): ")
    if number_of_orders == "done":
        order = False
    elif number_of_orders == "zehu":
        order = False
    elif number_of_orders == "stop":
        order = False

print("your order is finishd")


while True:
    city = input(
        "Please enter the name of a city you have visited (enter 'stop'  when you are finished): ")
    if city == 'stop':
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")

while True:
    costum_order = input("enter your order(or press stop): ")
    if costum_order == "stop":
        break
    else:
        print("continiu shoping")
print("bey bye")


secret_number = 5
while True:
    user_num = input("enter a number :")
    if int(user_num) == secret_number:
        print("congrats!")
        break
    else:
        print("wrong guess...")


current_num = 0
while current_num < 12:
    current_num += 1
    if 4 < current_num < 8:
        continue
    print(current_num)

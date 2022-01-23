# Instructions
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Bonus : use some Buit-in exceptions of Python


def tyr_exept():
    x = int(input())
    y = int(input())
    try:
        res = x / y
    except ZeroDivisionError:
        print("cannot divide by 0")
        res = 0
    print(res)


tyr_exept()

while True:
    n = int(input("what's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Python")    


# this code makes the user input a number k and it keeps asking until the user inputs a positive number
# then it prints "Python" k times using a for loop this is a long way to do it but it is a good way to learn 
# lopos with functions and user input
# if a user put a negative number or zero it will keep asking up until a positive number is entered

def positive():
    number = get_number()
    Python(number)

def get_number():
    while True:
        k = int(input("What's k? "))
        if k > 0:
            break
    return k


def Python(k):
    for _ in range(k):
        print("Python")

positive()        
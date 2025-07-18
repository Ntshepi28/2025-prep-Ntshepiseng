def main():
    x = int(input("what's x? "))
    name = input("what's your name? ")
    name = name.capitalize()
    hello(name)
    print("x is:", square(x))

def square(n):
    return n * n

def hello(name):
    print("Hello," , name)

main()    
x = int(input("what's x ? "))
y = int(input("what's y ? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is graeter than y")
elif x == y:
    print("x is equal to y")    
else:
    print("none of the above")


# second example of if-else statement making use of or operator cutting it short
if x < y or x >y:
    print("x is not equal to y")
else:
    print("x is equal to y")        
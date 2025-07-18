name = input ("what's your name? ")
name = name.strip() 
name = name.capitalize()  
name = name.title()  
print("Hello,", name, end="")

# this is a simple program that takes the user's name as input, and removes any leading or trailing whitespace,
# capitalizes the first letter of the name, and then prints a greeting without a newline at the end.


name = input("what's your name? ")

if name == "Samantha" or name == "Jack":
    print("Smith")
elif name == "John" or name == "Maggie":
    print("Doe")
else:
    print("who?")
# this code checks the user's name against a few predefined names and prints a corresponding last name.
# If the name doesn't match any of the predefined names, it prints "who?" as it does not match any of name mentioned. 


#nother example without having to use the if-else statement

name = input("what's your name? ")

match name:
    case "Samantha" | "Jack":
        print("Smith")
    case "John" | "Maggie":
        print("Doe")
    case _:
        print("who?")

# this code uses a match-case statement to check the user's name against predefined names and prints a corresponding last name. 
# instead of using if-else satements, we are using match-case statement which is also simple and readable.       
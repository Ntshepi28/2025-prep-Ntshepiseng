x = input("what's x? ")
y = input("what's y? ")

w = int(x) + int(y) #here an integer is created by using the int() function to convert the input strings to integers 
#so integer is behaving like a function
print(w)

#step 2 a shorter version to do the same code above
x = int(input("what's x? "))
y = int(input("what's y? "))

print(x + y) #here we are printing the sum of the two integers x and y


#step3 here we are introdfucing the float() function so that we can work with decimal numbers 
# and be aable to round them to the nearest integer
x = float(input("what's x? "))
y = float(input("what's y? "))

z = round(x + y)
print(z) 
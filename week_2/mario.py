def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    print("#\n" * height)

def print_row(width):
    print("?" * width)    

def print_square(size): 
    # for each row in the square   
    for i in range(size):
        # for each brick in the row
        for j in range(size):
            # print a brick
            print("#", end="")
        print() # this moves to the next line after printing a row

main()    

# this code defines a main function that calls two other functions: print_column and print_row this is 
# from a game called mario it has bars that are vertical(height) and horizontal(width) along with a square
# that is made of bricks and it prints a square of a given size 

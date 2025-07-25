students = ["Anna", "Katlego", "Zola"]

for i in range (len(students)):
    print(students[i])

# we are using a for loop to iterate through the list of students and print each student's name
# this is a simple way to access each element in the list by its index

students = {"Anna": "Smith",
            "Katlego": "Mokoena",
            "Zola": "Nkosi"
}

for learner in students:
    print(learner, students[learner], sep=", ")

# we are doing dictionary that contains students' names as keys and their surnames as values and the 
# for loop iterates through the dictionary and prints each student's name along with their surname


students = [
    {"name": "Anna", "house": "Smith", "pet": "Dog"},
    {"name": "Katlego", "house": "Mokoena","pet": "pitbull"},  
    {"name": "Zola", "house": "Nkosi", "pet": None},
    {"name": "Lerato", "house": "Molefe", "pet": "cat"}
]

for student in students:
    print(student["name"], student["house"], student["pet"], sep=", ")

# this is a list of dictionaries where each dictionary represents a student with their name, house, and pet
# the for loop iterates through the list and prints each student's name, house, and pet
import ast

#open the list of student
#You can add whatever names you'd like
with open('Students.txt', 'r') as file:
    content = file.read()

list_str = content.split('=', 1)[1].strip()
students = ast.literal_eval(list_str)

active = True

#once everything is active then go into the search of students
while active:
    last_name = input("Enter your last name: ").title()

    if last_name.upper() == "ZZZ":
        print("Have a good day!")
        active = False
        continue

#goes in and pulls the students lasts names amongst the list of dictionaries
    matching_last = [student for student in students if student["last_name"] == last_name]

    if matching_last:
        print("Last name found!")
        first_name = input("Enter your first name: ").title()
#does the same thing for the first names once its passes through the last name
        match = next((student for student in matching_last if student["first_name"] == first_name), None)
        if match:
            print(f"Name: {match['first_name']} {match['last_name']}, GPA: {match['gpa']}")
            #creates a gpa variable from the following students gpa that then checks to see if the student qualifies for the deans list and honor roll
            gpa = match['gpa']
            if gpa >= 3.25:
                print(f"You have made the honor roll due to your gpa!")
            if gpa >= 3.5:
                print(f"You have also made the deans list due to your gpa!")
            else:
                continue
        else:
            print("First name not found under that last name.")
    else:
        print("Last name not found.")

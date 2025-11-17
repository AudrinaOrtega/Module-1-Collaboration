active = True
while active:
    grades = int(input("Please enter what grade you recieved on the test!: "))

    if grades < 60:
        print("Your grade is less than 60 meaning you recieve an F")
    elif grades >= 60 and grades <= 69:
        print("Your grade is between 60 and 69 meaning you recieved a D")
    elif grades >= 70 and grades <= 79:
        print("Your grade is between 70 and 79 meaning you recieved a C")
    elif grades >= 80 and grades <= 89:
        print("Your grade is between 80 and 89 meaning you recieved a B")
    elif grades >= 90:
        print("Your grade is a 90 or above meaning you recieved an A")
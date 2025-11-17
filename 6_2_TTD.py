secret = 7
active = True
while active:
    guess = int(input("Guess the secret number between 1-10: "))

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("oops.")
        active = False
    elif guess == secret:
        print("Just right")
        break
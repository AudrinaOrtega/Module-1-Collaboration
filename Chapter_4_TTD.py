secret = 5

while True:
    guess = int(input("Guess the secret number between 1-10: "))

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    elif guess == secret:
        print("Just right")
toy_story_morality = {
    "Good": {
        "Woody": 70,                 # 1950s pull-string cowboy doll
        "Buzz Lightyear": 30,        # Released in the mid-1990s
        "Jessie": 60,                # 1950s cowgirl from Woody's Roundup
        "Bullseye": 60,              # Same vintage as Jessie
        "Bo Peep": 30,               # Porcelain figure, likely 1990s
        "Slinky Dog": 70,            # Based on 1950s toy
        "Rex": 30,                   # 1990s plastic dinosaur
        "Hamm": 30,                  # 1990s piggy bank
        "Mr. Potato Head": 70,       # First sold in 1952
        "Mrs. Potato Head": 70,      # Introduced shortly after Mr. Potato Head
        "Aliens (Little Green Men)": 30, # 1990s arcade prize toys
        "Andy": 17,                  # Teenager in Toy Story 3
        "Bonnie": 5,                 # Young child in Toy Story 3 & 4
        "Forky": 0.1,                # Handmade in Toy Story 4
        "Duke Caboom": 40,           # 1970s Canadian stuntman toy
        "Trixie": 30,                # Modern plastic triceratops
        "Buttercup": 30,             # Plush unicorn, likely 1990s–2000s
        "Dolly": 30                  # Fabric doll, modern design
    },
    "Evil": {
        "Sid": 11,          # Child antagonist in Toy Story 1
        "Stinky Pete": 70, # 1950s collectible toy
        "Lotso": 40, # 1980s plush bear
        "Emperor Zurg": 30,          # 1990s sci-fi villain toy
        "Al McWhiggin": 40,          # Adult toy collector
        "Gabby Gabby": 60            # 1950s pull-string doll
    }
}



#While true keeps it in a loop so that it just doesn't stop running after one input
while True:

#asking for an input (hopefully from the list)
    name = input("Put in a character from Toy Story (type quit to exit): ").title()

#first if is to close the program if quit is entered
    if name == "Quit":
        print("have a good day!")
        break
#checking to see if the name is in their, first checking if it's in the good
#if it is, then it pulls the age from the name and prints it
#then (to add a boolean example) I had it check if it was under the age of 35
    if name in toy_story_morality["Good"]:
        age = toy_story_morality["Good"][name]
        print(f"{name} was found, they're good and {age}")
        print(f"in five years {name}")
        Under_Age = age < 35
        print(f"Is {name} under 35? {Under_Age}")
#then it checks if it's in the other category, if it can't find the name in the good
#basically the same code from the first check
    elif name in toy_story_morality["Evil"]:
        age = toy_story_morality["Evil"][name]
        print(f"{name} was found, they're good and {age}")
        Under_Age = age < 35
        print(f"Is {name} under 35? {Under_Age}")
#finally, if it can't find the name in either, it loops asking the person to retype it in
    else:
        print("Oops! try retyping it, or character wasn't found in system!")

#not my best work, but to be fair, I wasn't going to go into too much precision

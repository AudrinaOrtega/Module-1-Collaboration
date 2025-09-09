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



#Future refrence: Loop it when you have the chance
while True:

    name = input("Put in a character from Toy Story: ").title()

    if name == "Quit":
        print("have a good day!")
        break
    if name in toy_story_morality["Good"]:
        age = toy_story_morality["Good"][name]
        print(f"{name} was found, they're good and {age}")
    elif name in toy_story_morality["Evil"]:
        age = toy_story_morality["Evil"][name]
        print(f"{name} was found, they're good and {age}")
    else:
        print("Oops! try retyping it, or character wasn't found in system!")
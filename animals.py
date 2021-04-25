# import the python datetime module to help us create a timestamp
from datetime import date

# Walking
class Llama():

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Donkey():
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Goat():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Horse():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Chicken():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

new_llama = Llama("Lenny", "Llama")
new_donkey = Donkey("Dave", "Donkey")
new_goat = Goat("Glenda", "Goat")
new_horse = Horse("Harriet", "Horse")
new_chicken = Chicken("Chester", "Chicken")

print(new_llama, new_chicken, new_donkey, new_goat, new_horse)

# Slithering
class Snake():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Snail():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Leech():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
class Worm():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
class Salamander():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

new_snake = Snake("Sandy", "Snake")
new_snail = Snail("Susan", "Snail")
new_leech = Leech("Laura","Leech")
new_worm = Worm("Wanda", "Worm")
new_salamander = Salamander("Sal", "Salamander")

print(new_snake, new_snail, new_leech, new_worm, new_salamander)

# Swimming
class Fish():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Seal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
class Shark():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Eel():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Turtle():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

new_fish = Fish("Frank", "Fish")
new_seal = Seal("Sally", "Seal")
new_shark = Shark("Shelly", "Shark")
new_eel = Eel("Earl", "Eel")
new_turtle = Turtle("Tim", "Turtle")

print(new_fish, new_seal, new_shark, new_eel, new_turtle)
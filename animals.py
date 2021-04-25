from slithering import (Snake, Snail, Leech, Worm, Salamander)
from swimming import (Fish, Seal, Shark, Eel, Turtle)
from walking import (Llama, Donkey, Goat, Horse, Chicken)
from attractions import (PettingZoo, CritterCove, Terrarium)

# Walking
new_llama = Llama("Lenny", "Llama", "Morning", "llama food")
new_donkey = Donkey("Dave", "Donkey", "Morning", "donkey food")
new_goat = Goat("Glenda", "Goat", "Midday", "goat food")
new_horse = Horse("Harriet", "Horse", "Midday", "horse food")
new_chicken = Chicken("Chester", "Chicken", "Afternoon", "chicken food")

petting_zoo = PettingZoo("Varmint House", "Where walking animals are")
petting_zoo.add_to_petting_zoo(new_llama)
petting_zoo.add_to_petting_zoo(new_donkey)
petting_zoo.add_to_petting_zoo(new_horse)
petting_zoo.add_to_petting_zoo(new_goat)
petting_zoo.add_to_petting_zoo(new_chicken)

print(f'In the {petting_zoo.attraction_name} {petting_zoo.description}, we have:')
for animal in petting_zoo.animals:
    print(f'{animal}')

# Slithering
new_snake = Snake("Sandy", "Snake", "snake food")
new_snail = Snail("Susan", "Snail", "snail food")
new_leech = Leech("Laura","Leech", "leech food")
new_worm = Worm("Wanda", "Worm", "worm food")
new_salamander = Salamander("Sal", "Salamander", "salamander food")

new_cove = CritterCove("Critter Cove", "where the swimming animals live")
new_cove.add_to_cove(new_snake) 
new_cove.add_to_cove(new_snail) 
new_cove.add_to_cove(new_leech) 
new_cove.add_to_cove(new_worm) 
new_cove.add_to_cove(new_salamander) 

print(f'In the {new_cove.attraction_name} {new_cove.description}, we have:')
for animal in new_cove.animals:
    print(f'{animal}')

# Swimming
new_fish = Fish("Frank", "Fish", "fish food")
new_seal = Seal("Sally", "Seal", "seal food")
new_shark = Shark("Shelly", "Shark", "shark food")
new_eel = Eel("Earl", "Eel", "eel food")
new_turtle = Turtle("Tim", "Turtle", "turtle food")

print(new_fish, new_seal, new_shark, new_eel, new_turtle)
new_terrarium = Terrarium("Slyther Inn", "where the slythering animals live")
new_terrarium.add_animal_to_terrarium(new_fish)
new_terrarium.add_animal_to_terrarium(new_seal)
new_terrarium.add_animal_to_terrarium(new_shark)
new_terrarium.add_animal_to_terrarium(new_eel)
new_terrarium.add_animal_to_terrarium(new_turtle)

print(f'In the {new_terrarium.attraction_name} {new_terrarium.description}, we have:')
for animal in new_terrarium.animals:
    print(f'{animal}')

print(new_llama.feed())
print(new_chicken.feed())
print(new_donkey.feed())
print(new_goat.feed())
print(new_horse.feed())

print(new_snake.feed())
print(new_snail.feed())
print(new_leech.feed())
print(new_worm.feed())
print(new_salamander.feed())

print(new_fish.feed())
print(new_seal.feed())
print(new_shark.feed())
print(new_eel.feed())
print(new_turtle.feed())

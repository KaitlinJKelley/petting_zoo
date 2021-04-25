class PettingZoo():
    def __init__(self, attraction, description):
        self.attraction_name = attraction
        self.description = description
        self.animals = []

    def add_to_petting_zoo(self, animal):
        self.animals.append(animal)

class Terrarium():
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []
    
    def add_animal_to_terrarium(self, animal):
        self.animals.append(animal)
        
class CritterCove():
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def add_to_cove(self, animal):
        self.animals.append(animal)

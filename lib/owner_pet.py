class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        #validate pet type
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        all_pets = []
        for pet in Pet.all:
            if pet.owner == self:
                all_pets.append(pet)
        return all_pets
    
    def add_pet(self, pet):
        if type(pet) != Pet:
            raise Exception("Pet not of type Pet")
        pet.owner = self 

    def get_sorted_pets(self):
        owned_pets = self.pets()
        sorted_pets = sorted(owned_pets, key=lambda pet: pet.name)
        return sorted_pets
class Animal:
    def __init__(self, species):
        self.species = species

class Bird(Animal):
    def fly(self):
        print(f"The {self.species} is flying!")

eagle = Bird("Eagle")
eagle.fly()  # Output: The Eagle is flying!
  
  
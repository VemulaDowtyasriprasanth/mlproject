class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Bark") 
class Cat(Animal):
    def speak(self):
        print("Meow")
def Animal_Sound(animal):
    animal.speak()
dog=Dog()
cat=Cat()
Animal_Sound(dog)
Animal_Sound(cat)

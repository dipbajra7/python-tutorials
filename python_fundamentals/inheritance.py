class Animal:
    def walk(self):
        print("walking")

    def make_sound(self):
        pass


class Dog(Animal): # extends animal
    pass
    def make_sound(self):
        print("bark")


class Cat(Animal): # extends animal
    def walk(self): # method overriding
        print('jumping')

    def make_sound(self):
        print("meow")
    


dog = Dog()
dog.walk()
dog.make_sound()

cat = Cat()
cat.walk()
cat.make_sound()
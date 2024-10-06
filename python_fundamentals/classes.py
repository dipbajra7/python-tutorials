class Point:
    def move(self):
        print("moved")

    
    def draw(self):
        print("draw")

    def calc_position(self, x, y):
        print(x * y)



point = Point()
point.draw()
point.move()
point.calc_position(2,3)

############################################################
class Person:
    def print_name(self, firstname, lastname):
        print(f'hello {firstname} {lastname}')


person = Person() 
person.middlename = 'Smith' #instantly create anything on the fly. no need to define properties in the class
person.print_name('James', 'Hammond')
print(person.middlename)

############################################################

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def print_coordinates(self):
        print(f'{self.x}, {self.y}')



coordinate1 = Coordinates(10, 20)
coordinate1.print_coordinates()
        

class Coordinates2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_coordinates(self):
        pass



class Human:

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

      
    def printdetails(self, name, age, phone):
        print(name)
        print(age)
        print(phone)


    def printdetailsagain(self):
        print('_______________________')
        print(self.name)
        print(self.age)


human2 = Human('Soumya', '22', '321')
human2.printdetailsagain()

human3 = Human('test')



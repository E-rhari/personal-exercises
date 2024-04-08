# setattr() and getattr() are both utterly pointless!

class Person():
    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender[0].upper()

    def printInfo(self):
        for property, value in self.__dict__.items():
            print(f"{property.capitalize()}: {value}")
        print()


kumiko = Person("Oumae Kumiko", 15, "female")

print("First Year of High School:")
kumiko.printInfo()

kumiko.age = 16

print("Second Year of High School:")
kumiko.printInfo()

setattr(kumiko, "age", 17)

print("Third Year of High School:")
kumiko.printInfo()


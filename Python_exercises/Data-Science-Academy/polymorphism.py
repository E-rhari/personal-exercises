class Person():
    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender[0].upper()

    def printInfo(self):
        for property, value in self.__dict__.items():
            print(f"{property.capitalize()}: {value}")
        print()


class Musician(Person):
    def __init__(self, name: str, age: int, gender: str, instrument:str, yearsPlaying:int):
        super().__init__(name, age, gender) #Person.__init__(self, name, age, gender)
        self.instrument = instrument
        self.yearsPlaying = yearsPlaying

    def musicalExperience(self):
        return f"{self.name} has been playing the {self.instrument} for {self.yearsPlaying} years!"
    

class CoolPerson(Person):
    def printInfo(self):
        print(f"{self.name} is pretty cool, and that's all you gotta know")


evandro = CoolPerson("Evandro Rhari", 18, "Male")
evandro.printInfo()
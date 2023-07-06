import datetime
import abc

class Poultry(abc.ABC):
    def __init__(self, name, sound, specy):
        self.name = name
        self.sound = sound
        self.specy = specy
    def make_some_noise(self, time = 3):
        self.name = "Noisy" + self.name
        print(f"{self.specy}-{self.name} make noise: {self.sound * time}")

    def hatch(self):
        print("Baby comes out ASMP.")

    @abc.abstractmethod
    def eat(self):
        pass
    
class Duck(Poultry):
    def __init__(self, name, sound):
        super().__init__(name, sound, "Duck")

    def swim(self):
        print(f"Duck-{self.name} is swiming")

    def eat(self):
        print(f"{self.specy} eat anything")

class Chicken(Poultry):
    def __init__(self, name, sound):
        super().__init__(name, sound, "Chicken")

    def morningCall(self):
        t = datetime.datetime.now()
        print(f"It is {t} now")
    
    def eat(self):
        print(f"{self.specy} eat bugs")

class Goose(Poultry):
    def __init__(self, name, sound):
        super().__init__(name, sound, "Goose")
    
    def chase_and_bit(self):
        print(f"{self.specy} {self.name} is chasing you, RUN!!!")

    def eat(self):
        print(f"{self.specy} eat grass")

if __name__ == "__main__":

    duck_1 = Duck("Guck", "Gu")
    duck_2 = Duck("Quck", "Qu")
    duck_3 = Duck("Peter", "Pu")

    chick_1 = Chicken("Amy", "Gu")

    goose_1 = Goose("Aba","Quack")

    duck_1.eat()
    chick_1.eat()
    goose_1.eat()
    

    

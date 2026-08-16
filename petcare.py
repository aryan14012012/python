"""Pet Care Dashboard - OOP Demonstration"""

class Pet:
    def __init__(self, name, age, weight):
        self.name, self.age, self.weight = name, age, weight
        self.__health = self.__happiness = 100
    
    def get_health(self):
        return self.__health
    
    def set_health(self, value):
        if 0 <= value <= 100:
            self.__health = value
            print(f"{self.name}'s health: {self.__health}")
    
    def set_happiness(self, value):
        if 0 <= value <= 100:
            self.__happiness = value
    
    def feed(self):
        self.set_health(min(self.__health + 10, 100))
        self.set_happiness(min(self.__happiness + 5, 100))
        print(f"{self.name} fed! 🍖")
    
    def play(self):
        self.set_happiness(min(self.__happiness + 15, 100))
        print(f"{self.name} played! 🎾")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")


class Dog(Pet):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name}: Woof! Woof! 🐕")
    
    def check_status(self):
        print(f"\n🐕 {self.name} ({self.breed})")
        print(f"Health: {self.get_health()}/100 | Happiness: {self.__happiness}/100")


class Cat(Pet):
    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color
    
    def make_sound(self):
        print(f"{self.name}: Meow! Meow! 🐈")
    
    def check_status(self):
        print(f"\n🐈 {self.name} ({self.color})")
        print(f"Health: {self.get_health()}/100 | Happiness: {self.__happiness}/100")


def main():
    pets = [Dog("Buddy", 3, 25, "Golden Retriever"), Cat("Whiskers", 2, 5, "Orange"), Dog("Max", 5, 30, "German Shepherd")]
    print("🐾 PET CARE DASHBOARD 🐾\nTotal pets:", len(pets))
    
    while True:
        print("\n1. View pets\n2. Feed pet\n3. Play\n4. Status\n5. Sound demo\n6. Exit")
        choice = input("\nChoice: ")
        
        if choice == "1":
            for i, pet in enumerate(pets, 1):
                print(f"{i}. {pet.name} ({pet.__class__.__name__})")
        
        elif choice == "2":
            num = int(input("Pet #: ")) - 1
            if 0 <= num < len(pets):
                pets[num].feed()
        
        elif choice == "3":
            num = int(input("Pet #: ")) - 1
            if 0 <= num < len(pets):
                pets[num].play()
        
        elif choice == "4":
            num = int(input("Pet #: ")) - 1
            if 0 <= num < len(pets):
                pets[num].check_status()
        
        elif choice == "5":
            print("\n🎵 POLYMORPHISM DEMO 🎵")
            for pet in pets:
                pet.make_sound()
        
        elif choice == "6":
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
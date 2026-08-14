"""Robot Introduction Program - OOP Concepts Demo"""

from abc import ABC, abstractmethod

# Abstract base class
class Robot(ABC):
    count = 0
    
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.battery = 100
        Robot.count += 1
    
    @abstractmethod
    def introduce(self):
        pass
    
    def charge(self):
        self.battery = 100
        print(f"⚡ {self.name} charged!")

# Inheritance - Service Robot
class ServiceRobot(Robot):
    def __init__(self, name, model, service_type):
        super().__init__(name, model)
        self.service_type = service_type
    
    def introduce(self):
        print(f"\n🤖 {self.name} - {self.model}")
        print(f"   Type: {self.service_type} Service Robot")
        print(f"   Battery: {self.battery}%")
    
    def work(self):
        print(f"✓ {self.name} performing {self.service_type} task")

# Inheritance - Companion Robot
class CompanionRobot(Robot):
    def __init__(self, name, model, personality):
        super().__init__(name, model)
        self.personality = personality
    
    def introduce(self):
        print(f"\n👋 {self.name} - {self.model}")
        print(f"   Personality: {self.personality}")
        print(f"   Battery: {self.battery}%")
    
    def greet(self):
        print(f"💬 {self.name}: Hello! I'm your {self.personality} companion!")

# Inheritance - Industrial Robot
class IndustrialRobot(Robot):
    def __init__(self, name, model, zone):
        super().__init__(name, model)
        self.zone = zone
    
    def introduce(self):
        print(f"\n🏭 {self.name} - {self.model}")
        print(f"   Zone: {self.zone}")
        print(f"   Battery: {self.battery}%")
    
    def operate(self):
        print(f"⚙ {self.name} operating in {self.zone}")

# Multiple inheritance
class SmartRobot(ServiceRobot, CompanionRobot):
    def __init__(self, name, model, service_type, personality):
        Robot.__init__(self, name, model)
        self.service_type = service_type
        self.personality = personality
    
    def introduce(self):
        print(f"\n🧠 {self.name} - {self.model}")
        print(f"   Service: {self.service_type} | Personality: {self.personality}")
        print(f"   Battery: {self.battery}%")

# Main demonstration
def main():
    print("=" * 60)
    print("ROBOT INTRODUCTION - OOP CONCEPTS")
    print("=" * 60)
    
    # Create robot objects
    cleaner = ServiceRobot("CleanBot", "SR-1", "Cleaning")
    friend = CompanionRobot("Buddy", "CR-1", "Friendly")
    worker = IndustrialRobot("Titan", "IR-1", "Assembly")
    smart = SmartRobot("Atlas", "AI-1", "Healthcare", "Caring")
    
    print(f"\n✓ Created {Robot.count} robots\n")
    
    # Polymorphism - same method, different behavior
    print("INTRODUCTIONS:")
    print("-" * 60)
    for robot in [cleaner, friend, worker, smart]:
        robot.introduce()  # Polymorphic method call
    
    # Encapsulation - using methods
    print("\n\nACTIONS:")
    print("-" * 60)
    cleaner.work()
    friend.greet()
    worker.operate()
    smart.work()
    smart.greet()
    
    # Battery management
    print("\n\nBATTERY STATUS:")
    print("-" * 60)
    for robot in [cleaner, friend, worker, smart]:
        print(f"{robot.name}: {robot.battery}%")
    
    print("\n⚡ Charging all robots...")
    for robot in [cleaner, friend, worker, smart]:
        robot.charge()
    
    print("\n" + "=" * 60)
    print("OOP Concepts: Classes, Objects, Inheritance,")
    print("Polymorphism, Encapsulation, Abstraction")
    print("=" * 60)

if __name__ == "__main__":
    main()
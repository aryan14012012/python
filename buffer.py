from abc import ABC, abstractmethod 


# Abstract class

class Employee(ABC):
    
    
    @abstractmethod 
    def work(self): 
        pass
    
    
    def show_name(self, name):
        print("Employee Name:", name)
        
        
        # Child class 
class Developer(Employee): 
            
            
    def work(self):
        print("Developer writes code")
        
        
class Designer(Employee): 
            
    def work(self):
        print("Designer creates designs")
        
        
        
dev = Developer()
designer = Designer()


dev.show_name("Alice")
dev.work()

designer.show_name("Bob")
designer.work()
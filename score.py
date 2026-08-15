class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score =  score
    
    
    def info(self):
        return f"Cricket Player: {self.__player}, Score: {self.__score}"
    
    
    def play(self):
        print(f"{self.__player} hits a six!")
        
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")
            
class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
        
    def info(self):
        print(f"Football Player: {self.__player}, Score: {self.__score}")
        
    def play(self):
        print(f"{self.__player} scores a goal!")
        
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")

cricket = Cricket("dhoni", 120)
football = Football("ronaldo", 30)

print(" ==== Sports Scoreboard ====")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()

print("---- Direct change attempt ----")
cricket._Cricket__score = 999
print(f"get_score() still shows : {cricket.get_score()}")
cricket.set_score(-10)
      
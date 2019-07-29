# -------------------------------------------------
#        Name: Blake Shepherd and Liliana Lilian
#    Filename: Pokemon.py
#        Date: July 24th, 2019 
#
# Description: Making Pokemon fight
#               
# -------------------------------------------------

import random




class Pokemon:
    def __init__(self, name, pokemon_type):
        self.name = name
        self.pokemon_type = pokemon_type
        self.max_hp = random.randint(1,100)
        self.current_hp = self.max_hp
        self.attack_power = random.randint(0,self.max_hp)
        self.defensive_power = random.randint(0,self.max_hp)
        self.fainted = False

    def printStats(self):

        print("Name: " + self.name)
        print("Type: " + self.pokemon_type)
        print("Max HP:" , self.max_hp)
        print("Current HP:" , round(self.current_hp))
        print("Attack Power:" , self.attack_power)
        print("Defensive Power:" ,self.defensive_power)

    def defense(self, attack):

        self.current_hp = self.current_hp-(attack*(1-self.defensive_power/100))
        
        if self.current_hp <= 0:
            self.fainted = True
        return self.current_hp
            
    def attack(self , opponent):
        opponent.current_hp = opponent.defense(self.attack_power)

    def revive(self):
        while self.max_hp > 10: 
            if self.fainted == True:
                self.current_hp = self.max_hp/2
                self.max_hp = self.max_hp/2
                self.fainted = False
                return True
            else:
                return False

class Pikachu(Pokemon):

    # ------- Start Attributed Code Section------
    # Code created with the help of Hacker Earth
    #https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-ii-inheritance-and-composition/tutorial/
    # Tutorial Name: Classes and Objects 2 (Inheritance and Compostion)
    def __init__(self, name, pokemon_type):
        super().__init__( name, pokemon_type)
        self.pokemon_type  = "ELECTRIC"
    # ------- End Attributed Code Section ---------
    def attack(opponent):
        if opponent.pokemon_type == "Ground":
            opponent.current_hp = opponent.defense(self.attack_power*2)

        elif (opponent.pokemon_type == "ELECTRIC" or opponent.pokemon_type == "FLYING"):
            opponent.current_hp = opponent.defense(self.attack_power/2)

class Paint(Pokemon):
    # ------- Start Attributed Code Section------
    # Code created with the help of Hacker Earth
    #https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-ii-inheritance-and-composition/tutorial/
    # Tutorial Name: Classes and Objects 2 (Inheritance and Compostion)
    def __init__(self, name, pokemon_type):
        super().__init__(name, pokemon_type)
        self.pokemon_type = "FLYING"
    # ------- End Attributed Code Section ---------
    def attack(self, opponent):
        if opponent.pokemon_type == "ELECTRIC":
            opponent.current_hp = opponent.defense(self.attack_power*2)

        elif (opponent.pokemon_type == "GROUND" or opponent.pokemon_type == "FLYING"):
            opponent.current_hp = opponent.defense(self.attack_power/2)



class Crimson(Pokemon):
    # ------- Start Attributed Code Section------
    # Code created with the help of Hacker Earth
    #https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-ii-inheritance-and-composition/tutorial/
    # Tutorial Name: Classes and Objects 2 (Inheritance and Compostion)
    def __init__(self, name, pokemon_type):
        super().__init__(name, pokemon_type)
        self.pokemon_type  = "GROUND"
    # ------- End Attributed Code Section ---------
    def attack(self, opponent):
        if opponent.pokemon_type == "FLYING":
            opponent.current_hp = opponent.defense(self.attack_power*2)

        elif (opponent.pokemon_type == "GROUND" or opponent.pokemon_type == "ELECTRIC"):
            opponent.current_hp = opponent.defense(self.attack_power/2)


    


def battle(p1, p2):

    Ro=1

    Player1 = True

    while p1.current_hp>0 and p2.current_hp>0:
        if Player1 == True:
            p1.attack(p2)
            p2.revive()
            p2.printStats()


        else:
            p2.attack(p1)
            p1.revive()
            p1.printStats()

            x = input("Continue? ")


        Player1 = not Player1

    print("Round", Ro)

    Ro += 1


        
def main():


    
    Blue_nails = Pokemon("Blue Nails", "Normal")

    

    John = Paint("John", "Electric")

    Hats = Crimson("Hats", "Normal")
    
    while (John.current_hp>0 and Hats.current_hp>0):  

        battle(Blue_nails, Hats)

    print("The Game is Over!")


if __name__ == "__main__":
    main() 

# NameErrors in subclasses. Some problems with battle. 

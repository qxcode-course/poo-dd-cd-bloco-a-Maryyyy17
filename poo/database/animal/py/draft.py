class Animal :
    def__init__(self,species: str, sound: str):
        self.species : str = species
        self.sound : str = sound
        self.age : int = 0


def __str__(self) :
    return f"{self.species} : {self.sound} : {self.age}"

def ageBy(self, increment: int) -> None
    self.age += increment
    if self.age >= 4
        print ("warning: {species} morreu")
        self.age = 4

def makeSound (self) -> str:
    if self.age == 0 :
        return f"---"
    elif self.age == 4 :
        return f"RIP"
    else :
        return self.sound

def main()
    bichano = Animal("", "")
    while True:
        line : str = input()
        args : list [str] = line.split (" ")
        if args[0] == "end":
            break
        elif args[0] == "init" :
            species = args[1]
            sound = args[2]
            bichano = Animal(species,sound)

        elif args[0] = "show" :
            print(bichano)
        elif args[0] = "grow" :
            increment : int = int(args[0])
            bichano.age(increment)
        else:
            print("fail: código invalido")

main()





    

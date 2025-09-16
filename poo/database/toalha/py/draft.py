

class Toalha:
    def __init__(self, color:str, size:str): #construtor
        self.color = "red" #atributos
        self.size = "p"
        self.wetness = 0

    def __str__(self):
        return f"color:{self.color}, tam:{self.size}, hum{self.wetness}"

towel = Toalha("green", "G") #objetos
towel2 = Toalha("purple", "M")
towel.color = "white"
print(towel.color)
print(towel.size)
print(towel.wetness)
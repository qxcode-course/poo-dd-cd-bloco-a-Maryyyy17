class Calculadora :
    def __init__(self, batteryMax : int) :
        self.battery : int = 0
        self.batteryMax = batteryMax
        self.display : float = 0.00

    def __str__(self) -> str :
        return f"display = {self.display:,.2f}, battery = {self.battery}"
    
    def charge(self, value:int) :
        if self.battery < self.batteryMax :
            self.battery += value

        if self.battery == self.batteryMax :
            print("bateria completamemte carregada")
            self.battery -= 1

    def sum(self, a : float, b : float) -> None :
            if self.battery == 0 :
                print("fail: bateria insuficiente")            
            else :
                self.display = a + b
                self.battery -= 1

    def div(self, x : float, y : float) -> None :
        if self.battery == 0 :
                print("fail: bateria insuficiente")  
        elif y == 0 :
             print("fail: divisao por zero")
        else :
             self.display = x / y
             self.battery -= 1

def main():
    calculadora = Calculadora(0)

    while True:
        line: str = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            calculadora = Calculadora(int(args[1]))
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "charge":
            increment = int(args[1])
            calculadora.charge(increment)
        elif args[0] == "sum":
            calculadora.sum(int(args[1]), int(args[2]))
        elif args[0] == "div":
            calculadora.div(int(args[1]), int(args[2]))
        else:
            print("fail: comando desconhecido")
main()
               



    

    


        


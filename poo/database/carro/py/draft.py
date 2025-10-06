class Carro :
    def __init__ (self) :
        self.pasa : int = 0
        self.km : int = 0
        self.gas : int = 0

    def __str__ (self) :
        return f"pass: {self.pasa}, gas: {self.gas}, km: {self.km}"

    def enter(self) -> None :
        if self.pasa < 2 :
                self.pasa += 1
        else:
           print("fail: limite de pessoas atingido")
               
    def leave(self) -> None :
       if self.pasa > 0 :
             self.pasa -= 1
       else :
            print("fail: nao ha ninguem no carro")

    def fuel (self, increment : int) -> None :
        self.gas += increment
        if self.gas <= 0 :
                print ("fail: tanque vazio")
                self.gas = 0

        if self.gas >= 100 :
                self.gas = 100
            
    def drive (self, distance : int) -> None :
        if self.pasa == 0 :
            print ("fail: nao ha ninguem no carro")
            return
        if self.gas == 0 :
            print ("fail: tanque vazio")
            return
        if distance > self.gas :
            print (f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0
            return

        self.km += distance
        self.gas -= distance
        

def main():
    carro = Carro()  

    while True:
        try:
            line = input()
        except EOFError:
            break 
        line = line.strip()
        if not line:
            continue  

        print(f"${line}")  

        args = line.split()
        inp = args[0]

        if inp == "end":
            break

        elif inp == "show":
            print(carro)

        elif inp == "enter":
            quantidade = 1  
            if len(args) > 1:
                try:
                    quantidade = int(args[1])
                except ValueError:
                    print("fail: valor inválido")
                    continue
            carro.enter()

        elif inp == "leave":
            carro.leave()

        elif inp == "fuel":
            if len(args) > 1:
                try:
                    quantidade = int(args[1])
                    carro.fuel(quantidade)
                except ValueError:
                    print("fail: valor inválido")
            else:
                print("fail: falta argumento")

        elif inp == "drive":
            if len(args) > 1:
                try:
                    distancia = int(args[1])
                    carro.drive(distancia)
                except ValueError:
                    print("fail: valor inválido")
            else:
                print("fail: falta argumento")

        else:
            print("fail: código invalido")


if __name__ == "__main__":
    main()
        
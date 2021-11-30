class UISnake:

    def __init__(self,srv):

        self.__srv = srv
    
    def afisareMatrice(self):

        l = self.__srv.getMatrix()

        for lista in l:

            print("+",end="")
            for j in range(0,len(l)):
                print("---+",end="")
            
            print()
            
            for ind in range(0,len(l)):
                
                caracter = ""
                if lista[ind] == "A":
                    caracter = "."
                elif lista[ind] == "H":
                    caracter = "*"
                elif lista[ind] == "T":
                    caracter  = "+"
                else:
                    caracter = " "
                print("| " + caracter + " ",end="")
            
            print("|")

        print("+",end="")
        for j in range(0,len(l)):
            print("---+",end="")

        print()

    def moveSnake(self,counter=1):
        """
            move 2
            move
        """
        try:

            self.__srv.moveSnake(counter)
        
        except Exception:

            exit("Game over!")

    def run(self):

        while True:

            self.afisareMatrice()

            cmd = input(">>> ")

            cmd = cmd.split(" ")

            if cmd[0].lower() == "exit":

                print("Goodbye!")
                return
            
            elif cmd[0].lower() == "move":

                if len(cmd) == 2:

                    self.moveSnake(int(cmd[1]))
                
                else:

                    self.moveSnake()
            
            else:

                print("Invalid command!")



                
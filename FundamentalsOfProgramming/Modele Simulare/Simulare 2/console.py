from domain import Validator_bicicleta_exception

class Console():
    """
        Clasa console reuneste toate serviceurile din cod
    """

    def __init__(self,srv):
        """
            initializam aceasta clasa si meniul pe care o sa-l vada utilizatorul
        """

        self.__srv = srv
        self.__meniu = """
        1 - Stergere tip
        2 - Stergere max
        3 - Afisare
        4 - Stergere dupa id
        x - Exit

        """
    
    def delete_tip(self):
        """
            Metoda ce are rolul de a citi un tip si a apela functia ce sterge dupa tip
        """

        tip = input("Introduceti tipul pe care doriti sa-l stergeti: ")

        self.__srv.delete_tip(tip)
    
    def delete_max(self):
        """
            Metoda ce are rolul de a citi un tip si a apela functia ce sterge dupa pretul maxim
        """

        self.__srv.delete_max()
    
    def delete_id(self):
        """
            Metoda ce are rolul de a citi un tip si a apela functia ce sterge dupa id
        """

        id = int(input("Introduceti id: "))
        self.__srv.delete_by_id(id)

    def start(self):
        """
            Comenziile si functiile aferente comenziilor
        """

        while True:

            print(self.__meniu)

            cmd = input("Introduceti comanda: ")

            if cmd == "x":

                print("La revedere!")
                return
            
            elif cmd == "1":

                self.delete_tip()
            
            elif cmd == "2":

                self.delete_max()
            
            elif cmd == "3":

                l = self.__srv.getAll()

                for i in l:

                    print(str(i))

            elif cmd == "4":

                try:
                    self.delete_id()
                except ValueError:
                    print("Date de intrare invalide!")
                except Validator_bicicleta_exception as e:
                    print(e)
            
            else:

                print("Comanda gresita!")
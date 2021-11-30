from service import Service_muzica_exception
from domain import Validator_melodie_exception

class Console:
    """
        Clasa Console se ocupa cu asamblarea propriu-zisa a programului si realizarea legaturilor aferente
    """

    def __init__(self,srv):
        """
            Cu ajutorul acestei metode initializam legatura dintre ui si service, si totodata retinem meniul functiei
        """

        self.__srv = srv
        self.__meniu = """
                        Meniu
        
        1) Afisarea melodiilor care contin un anumit sir de caractere citit
        2) Sa se afiseze toate piesele ce au genul corespunzator unui id citit
        3) Exit

        """
    
    def afisare_melodii_sir(self):
        """
            Aceasta metoda se ocupa cu citirea unui sir de caractere si apelarea functiei corespunzatoare cerintei 1 din service
        """

        sir = input("Introduceti sirul de caractere dorit: ")
        l = self.__srv.afisare_melodii_sir(sir)
        for i in l:
            print(str(i))
    
    def afisare_melodii_gen(self):
        """
            Aceasta metoda se ocupa cu citirea unui id si apelarea functiei corespunzatoare cerintei 2 din service
        """

        id = int(input("Introduceti id-ul: "))
        l = self.__srv.afisare_piese_gen_corespunzator_id(id)
        for i in l:
            print(str(i))
    
    def start(self):
        """
            Cu ajutorul acestei metode pornim aplicatia propriu-zisa
        """

        while True:

            print(self.__meniu)

            cmd = input("Introduceti comanda dorita: ")

            if cmd == "3":

                print("La revedere!")
                return
            
            elif cmd == "1":

                try:
                    self.afisare_melodii_sir()
                except Service_muzica_exception as e:
                    print(e)
            
            elif cmd == "2":

                try:
                    self.afisare_melodii_gen()
                except ValueError:
                    print("Date de intrare invalide!")
                except Validator_melodie_exception as e:
                    print(e)
                except Service_muzica_exception as e:
                    print(e)
            
            else:

                print("Comanda invalida!")
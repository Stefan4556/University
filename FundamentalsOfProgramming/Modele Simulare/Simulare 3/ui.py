from service import Service_exception
from domain import Validator_arta_exception

class Console():
    """
        Clasa ce se ocupa cu imbinarea tutoror service-urilor
    """

    def __init__(self,srv):
        """
            Aceasta metoda are rolul de a initializa consola, de a realiza legatura catre service si de a retine meniul programului
        """

        self.__srv = srv
        self.__meniu = """
                    Meniu

        1) Afisarea tuturor operelor de arta ce contin un sir
        2) Afisarea tuturor autorilor ce au expuse lucrarile intr-o camera
        3) Exit

        """

    def afisare_arta_string(self):
        """
            Aceasta functie are rolul de a apela o metoda ce realizeaza afisarea artelor ce contin un anumit sir de caractere si ordonarea acestora descrescatoare
            dupa numele autorului
        """

        cuv = input("Introduceti sirul de caractere dorit: ")
        l = self.__srv.afisare_contin_sir_carac(cuv)
        for i in l:
            print(str(i))
    
    def afiseaza_autori_camere(self):
        """
            Aceasta functie are rolul de a apela o metoda ce realizeaza afisarea autorilor ce au artele expuse intr-o camera al carui numar este introdus de catre utilizator
        """

        nr = int(input("Introduceti numarul camerei: "))
        l = self.__srv.afisare_autori_din_camera(nr)
        print("Camera",nr,": ",end="")
        for i in range(0,len(l)):
            print(l[i],end="")
            if i != len(l) - 1:
                print(", ",end="")

    def run(self):
        """
            Aceasta metoda reprezinta pornirea programului
        """

        while True:

            print(self.__meniu)
            cmd = input("Introduceti comanda: ")

            if cmd == "3":

                print("La revedere!")
                return
            
            elif cmd == "1":
                
                try:
                    self.afisare_arta_string()
                except Service_exception as e:
                    print(e)
            
            elif cmd == "2":

                try:
                    self.afiseaza_autori_camere()
                except ValueError:
                    print("Date de intrare invalide!")
                except Validator_arta_exception as e:
                    print(e)
                except Service_exception as e:
                    print(e)
            
            else:

                print("Comanda invalida!")

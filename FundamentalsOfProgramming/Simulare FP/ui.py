from service import Exceptii_service_vacante

class Console:
    """
        Clasa consola se ocupa cu legarea ui-ului de service si cu interfata aplicatiei
    """

    def __init__(self,srv):
        """
            In aceasta metoda initializam legatura dintre ui si service, respectiv meniul aplicatiei
        """

        self.__srv = srv
        self.__meniu = """
                        Meniu
        
        1) Afisarea tuturor destinatiilor ce contin un anumit sir
        2) Grupare dupa cuvinte cheie
        3) Exit

        """
    
    def afisare_destinatii_sir(self):
        """
            Aceasta metoda are scopul de a apela functia din service ce se ocupa cu cerinta numarul 1, cea daca se gaseste un sir in numele locatiei
        """

        sir = input("Introduceti sirul: ")
        l = self.__srv.afisare_destinatii_sir_caractere(sir)

        for i in l:

            print(str(i))
    
    def afisare_grupari(self):
        """
            Rolul acestei metode este de a apela functia din service ce se ocupa cu realizarea cerintei numarul 2, anume cea cu gruparea dupa cuvinte cheie si efecturea pretului mediu
        """

        l = self.__srv.grupare_cuvinte_cheie()

        for i in range(0,len(l)):

            print("- ",l[i][0],end=": ")
            print(l[i][1])

    def start(self):
        """
            Aceasta ultima metoda din consola se ocupa cu primirea comenzilor de la utilizator si apelarea functiilor
        """

        while True:

            print(self.__meniu)

            cmd = input("Introduceti comanda: ")

            if cmd == "3":

                print("La revedere!")
                return
            
            elif cmd == "1":

                try:
                    self.afisare_destinatii_sir()
                except Exceptii_service_vacante as e:
                    print(e)
            
            elif cmd == "2":

                self.afisare_grupari()
            
            else:

                print("Comanda invalida!")
"""
    Acest modul se ocupa cu ui, adica cu interfata grafica pe care utilizatorul o vede, acesta fiind strans legat de service
"""

from service import EroriService

class Console:
    """
        Aceasta este clasa ce se ocupa cu interfata utilzaitorului si cu pucntul de pornire al apelurilor utilziatorului in momentul in care introduce o comanda
    """

    def __init__(self,srv):
        """
            Cu ajutorul acestei metode initializam legatura dintre consola si service si meniul aplciatiei
        """

        self.__meniu = """
                        Meniu
            
            1) Afisare destinatii
            2) Afisare destinatii ce contin sir de caractere
            3) Pretul mediu pe cuvinte cheie
            4) Exit

        """
        self.__srv = srv
    
    def afisare_clienti(self):
        """
            Aceasta este metoda ce se ocupa cu afisarea tuturor destinatiilor din fisierul nostru
        """

        l = self.__srv.getLista()
        for i in l:
            print(str(i))
    
    def afisare_destinatii_contin_Caractere(self):
        """
            Aceasta este metoda ce se ocupa cu afisarea destinatiilor ce contin un anumit sir de caractere sortate descrescator dupa numele destinatiei
        """

        sir = input("Introduceti sirul de caractere dorit: ")
        l = self.__srv.destinatii_ce_contin_sir_caractere(sir)
        for i in l:
            print(str(i))
    
    def afisare_pretul_mediu_cuvinte_cheie(self):
        """
            Aceasta este metoda ce apeleaza alta metoda din service, metoda ce se ocupa cu realizarea mediei aritmetice pentru fiecare cuvant cheie din sirul de cuvinte al fiecarei
            destinatii
        """

        l = self.__srv.grupare_cuvinte_cheie()
        for i in range(0,len(l)):
            print("- ",l[i][0],end=": ")
            print(l[i][1])

    def start(self):
        """
            Aceasta este metoda ce primeste comenzile introduse de catre utilizator si apelul celorlalte functii din acest modul
        """

        while True:

            print(self.__meniu)
            cmd = input("Introduceti comanda: ")
            
            if cmd == "4":

                print("La revedere!")
                return 0
            
            if cmd == "1":
                
                self.afisare_clienti()

            elif cmd == "2":

                try:
                    self.afisare_destinatii_contin_Caractere()
                except EroriService as e:
                    print(e)
            
            elif cmd == "3":

                self.afisare_pretul_mediu_cuvinte_cheie()

            else:

                print("Comanda invalida!")


            
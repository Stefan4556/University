"""
    Acest modul se ocupa cu retinerea unei singure clase si anume clasa Consola ce reprezinta interfata grafica a aplicatiei
"""

from domain import ValidatorCarteException
from repository_carti import RepositoryException
from service import ServiceException

class Console:
    """
        Aceasta clasa retine metodele aferente consolei
    """

    def __init__(self,srv):
        """
            Intializam legatura dintre consola si service, meniul si elementele filtrului
        """

        self.__srv = srv
        self.__meniu = """
                        Meniu
            
            1) Adaugare carte
            2) Modifca carti
            3) Undo
            4) Modificare filtru
            5) Afisare carti
            6) Exit

        """
        self.sir = ""
        self.an = -1
    
    def adaugare_carte(self):
        """
            Aceasta metoda adauga in lista de carti o carte introdusa de catre utilziator
        """

        id = int(input("Introduceti id-ul cartii: "))
        titlu = input("Introduceti titlul cartii: ")
        autor = input("Introduceti autorul cartii: ")
        an_aparitie = int(input("Introduceti anul aparitiei: "))
        self.__srv.adaugare_carte(id,titlu,autor,an_aparitie)
    
    def afisare_carti(self):
        """
            Aceasta metoda afiseaza lista de carti
        """

        l = self.__srv.afisare_carti()

        for carte in l:

            print(str(carte))
        
    
    def modfica_carti(self):
        """
            Rolul acestei metode este de a modifica autorii cartilor ce contin o anumita cifra in id
        """

        cifra = int(input("Introduceti o cifra: "))
        autor = input("Introduceti un autor: ")
        self.__srv.modifica_carti(cifra,autor)
    
    def undo_lista(self):
        """
            Rolul acestei metode este de a apela functia undo
        """

        self.__srv.undo_lista()
    
    def modificare_filtru(self):
        """
            Aceasta metoda reprezinta unicul mod de a modifica filtrul
        """

        sir_filtru = input("Introduceti noul sir din filtru: ")
        self.sir = sir_filtru
        an_filtru = int(input("Introduceti noul an din filtru: "))
        self.an = an_filtru
    
    def afisare_elemente_filtru(self):
        """
            Aceasta metoda afiseaza elementele ce corespund filtrului
        """

        l = self.__srv.afisare_elemente_filtru(self.sir,self.an)

        print ("Filtrul este: Sir - ",self.sir,"An - ",self.an)
        for i in l:
            print(str(i))
    
    def run(self):
        """
            Cu ajutorul acestei metode primi comenzile de la utilziator si realziam apelurile de functii
        """

        self.afisare_elemente_filtru()

        while True:

            print(self.__meniu)

            cmd = input("Introduceti comanda: ")

            if cmd == "6":

                print("La revedere!")
                return
            
            elif cmd == "1":

                try:
                    self.adaugare_carte()
                except ValueError:
                    print("Date de intrare invalide!")
                except ValidatorCarteException as e:
                    print(e)
                except RepositoryException as e:
                    print(e)
            
            elif cmd == "2":

                try:
                    self.modfica_carti()
                except ValueError:
                    print("Date de intrare invalide!")
                except ValidatorCarteException as e:
                    print(e)
                except RepositoryException as e:
                    print(e)
            
            elif cmd == "3":

                try:
                    self.undo_lista()
                except RepositoryException as e:
                    print(e)

            elif cmd == "4":

                try:
                    self.modificare_filtru()
                except ValueError:
                    print("Date de intrare invalide!")

            elif cmd == "5":

                    self.afisare_carti()
            
            else:

                print("Comanda invalida!")
            
            try:
                self.afisare_elemente_filtru()
            except ServiceException as e:
                print(e)
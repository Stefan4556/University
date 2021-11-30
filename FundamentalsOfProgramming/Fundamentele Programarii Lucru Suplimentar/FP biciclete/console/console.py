"""
    Acest modul contine clasa Console, clasa ce reprezinta interfata grafica a aplicatiei si legatura dintre utilizator si cod
"""

from repository.repository import RepositoryException

class Console:
    """
        Aceasta clasa reprezinta clasa ce tine de interfata grafica a functiei si de apelurile celorlalte module
    """

    def __init__(self,srv):
        """
            In aceasta metoda este initializata legatura dintre consola si service si este realizat meniul
        """

        self.__srv = srv
        self.__meniu = """
                        Meniu

            1 - Sterge tip
            2 - Sterge max
            3 - Afisare biciclete
            x - Exit

        """
    
    def sterge_tip(self):
        """
            Scopul acestei metode este de citi si sterge toate bicicletele de un anumit tip
        """

        tip = input("Introduceti tipul pe care doriti sa l stergeti: ")
        self.__srv.stergere_tip(tip)
    
    def sterge_max(self):
        """
            Scopul acestei metode este de a sterge toate bicicletele ce au pret maxim
        """

        self.__srv.stergere_max()
    
    def afisare_bicicelte(self):
        """
            Rolul acestei metode este de a afisa bicicletele
        """

        l = self.__srv.afisare_bicicelte()

        for b in l:

            print(str(b))
    
    def start(self):
        """
            Aceasta metoda porneste intreaga aplicatie, primind comenzi de la utilziator apeleaza alte functii 
        """

        while True:

            print(self.__meniu)
            cmd = input("Introduceti comanda: ")

            if cmd == "x":

                print("La revedere!")
                return 
            
            elif cmd == "1":
                
                try:
                    self.sterge_tip()
                except RepositoryException as e:
                    print(e)
            
            elif cmd == "2":
                
                try:
                    self.sterge_max()
                except RepositoryException as e:
                    print(e)
            
            elif cmd == "3":

                self.afisare_bicicelte()
            
            else:

                print("Comanda invalida!")
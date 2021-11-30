from service import Service_spa_exception

class Console:
    """
        Clasa consola reprezinta interfata de o vede utilizatorul, aceasta continand mai multe metode
    """

    def __init__(self,srv):
        """
            Aceasta metoda are rolul de a realiza legatura dintre ui si service si de a retine meniul aplicatiei
        """

        self.__srv = srv
        self.__meniu = """
                        Meniu
        
        1) Afisarea tuturor serviciilor care contin un anumit abonament citit de la tastatura
        2) Afisarea tipurilor de abonamente
        3) Exit

        """
    
    def afisare_clienti_abonament(self):
        """
            Rolul acestei metode este de a apela functia din service ce filtreaza lista de servicii dupa tip si o sorteaza descrescator dupa pret
        """

        abonament = input("Introduceti abonamentul: ")
        l = self.__srv.afisare_servicii_ce_contin_tip(abonament)
        for i in l:

            print (str(i))
    
    def afisare_tipuri_abonamente(self):
        """
            Rolul acestei metode este de a apela functia din service ce afiseaza toate tipurile de abonamente disponibile si ce denumiri au serviciile ce au aceste abonamente
        """

        l = self.__srv.afisare_tipuri_abonamente()
        for i in range(0,len(l)):

            print("- ",l[i][0],end=": ")
            for j in range(1,len(l[i])):
                print(l[i][j],end="")
                if j != len(l[i])-1:
                    print(", ",end="")
            print("")

    def start(self):
        """
            Aceasta metoda are rolul de a porni aplicatia, primii comenziile utilizatorului si de a da sarcina mai departe celorlalte functii din program
        """

        while True:

            print(self.__meniu)
            cmd = input("Introduceti comanda: ")

            if cmd == "3":

                print("La revedere!")
                return
            
            elif cmd =="1":

                try:
                    self.afisare_clienti_abonament()
                except Service_spa_exception as e:
                    print(e)
            
            elif cmd == "2":

                self.afisare_tipuri_abonamente()
            
            else:

                print("Comanda invalida!")



"""
    Acest modul se ocupa cu concatenarea functiilor programului
"""

from domain_clienti import Validator_client_exception
from domain_carti import Validator_carti_exception
from domain_inchirieri import Validator_inchirieri_exception

from service_clienti import Service_client
from service_carti import Service_carte
from service_inchirieri import Service_inchirieri

from repository_clienti import Exception_Repository_Clienti
from repository_carti import Exception_Repository_Carti
from repository_inchirieri import Exception_Repository_Inchirieri

from service_clienti import Exception_service_client
from service_carti import Exception_service_carte
from service_inchirieri import Exception_service_inchirieri

class Consola:
    """
        Clasa consola asambleaza intreg programul 
    """
    def __init__(self,service_clienti,service_carti,service_inchirieri):
        """
            Realizam conexiunea dintre ui si service_clienti si realizam interfata grafica a meniului
        """

        self.__service_clienti = service_clienti
        self.__service_carti = service_carti
        self.__service_inchirieri = service_inchirieri
        self.__meniu = """
                        Meniu principal

----> Adauga client...................................Adaugare client
----> Afisare clienti.................................Afisare clienti
----> Stergere client dupa id.........................Stergere client
----> Cautare client dupa id..........................Cauta client
----> Modifica numele clientului dupa id..............Modifica client
----> Genereaza n clienti random......................Genereaza clienti random
----> Adauga carte....................................Adaugare carte
----> Modifica titlul cartii dupa id..................Modifica carte
----> Afisare carti...................................Afisare carti
----> Cautare carte dupa id...........................Cauta carte
----> Stergere carte dupa id..........................Stergere carte
----> Genereaza n carti random........................Genereaza carti random
----> Adaugare inchiriere.............................Adaugare inchiriere
----> Returnare carte.................................Returnare inchiriere
----> Afisare inchirieri..............................Afisare inchirieri
----> Afisare cele mai inchiriate carti...............Raport cele mai inchiriate carti
----> Raport clienti cu carti inchiriate dupa nume....Raport clienti nume
----> Raport clienti dupa numarul de inchirieri.......Raport clienti inchirieri
----> Raport cei mai activi 20% clienti...............Raport clienti activi
----> Raport autori ordonati descrescator.............Raport autori ordonati descrescator
----> Pentru iesire...................................Exit
        """
    
    def ui_adaugare_client(self):
        """
            Metoda ce citeste si realizeaza legatura dintre ui - service_clienti - repository_clienti - domain_clienti
            cu scopul de a adauga un client
        """

        id = int(input("Introduceti id: "))
        nume = input("Introduceti nume: ")
        cnp = int(input("Introduceti cnp: "))
        self.__service_clienti.adauga_client(id,nume,cnp)

    def ui_adaugare_carte(self):
        """
            Metoda ce citeste si realizeaza legatura dintre ui - service_carti - repository_carti - domain_carti
            cu scopul de a adauga o carte
        """
        
        id = int(input("Introduceti id: "))
        titlu = input("Introduceti titlul cartii: ")
        descriere = input("Introduceti descrierea cartii: ")
        autor = input("Introudceti autorul cartii: ")
        self.__service_carti.adauga_carte(id,titlu,descriere,autor)
    
    def ui_adaugare_inchiriere(self):
        """
            Metoda ce citeste si realizeaza legatura dintre ui - service_inchirieri - repository_inchirieri - domain_inchirieri
            cu scopul de a adauga o inchiriere
        """
        
        id_inchiriere = int(input("Introudceti id-ul inchirierii: "))
        id_client = int(input("Introduceti id-ul clientului: "))
        id_carte = int(input("Introduceti id-ul cartii: "))
        self.__service_inchirieri.adauga_inchiriere(id_inchiriere,id_client,id_carte)

    def ui_cauta_client(self):
        """
            Metoda ce citeste si realizeaza legatura dintre ui - service_clienti - repository_clienti - domain_clienti
            cu scopul de a cauta un client
        """

        id = int(input("Introudceti id: "))
        valoare = self.__service_clienti.cautare_client_existent(id)
        print(valoare)

    def ui_cauta_carte(self):
        """
            Metoda ce citeste si realizeaza legatura dintre ui - service_carti - repository_carti - domain_carti
            cu scopul de a cauta o carte
        """
        
        id = int(input("Introduceti id: "))
        valoare = self.__service_carti.cautare_carte_existenta(id)
        print(valoare)

    def ui_modifica_client(self):
        """
            Metoda ce primeste de la utilziator un id si un nume_nou pentru a ii modifica numele clientului cu id-ul respectiv
        """

        id = int(input("Introduceti id: "))
        nume = input("Introduceti numele nou: ")
        self.__service_clienti.modifica_client(id,nume)

    def ui_modifica_carte(self):
        """
            Metoda ce primeste de la utilizator un id si un tilu_nou pentru a ii modifica titlul cartii cu id-ul repsectiv
        """
        
        id = int(input("Introduceti id: "))
        titlu = input("Introduceti noul titlu al cartii: ")
        self.__service_carti.modifica_carte(id,titlu)

    def ui_stergere_client(self):
        """
            Metoda ce citeste si realizeaza legatura dintre ui - service_clienti - repository_clienti cu scopul de a sterge
            un client dupa id daca acesta exista
        """

        id = int(input("Introduceti id: "))
        self.__service_clienti.stergere(id)
        self.__service_inchirieri.stergere_inchiriere_id_client(id)
        print("A fost sters clientul!")
    
    def ui_stergere_carte(self):
        """
            Metoda ce citeste si realizeaza legtura dintre ui - service_carti - repository_carti cu scopul de a sterge o carte
            dupa id daca aceasta exista
        """
        
        id = int(input("Introduceti id: "))
        self.__service_carti.stergere(id)
        self.__service_inchirieri.stergere_inchiriere_id_carte(id)
        print("A fost stearsa cartea!")
    
    def ui_stergere_inchiriere(self):
        """
            Metoda ce citeste si realizeaza legatura dintre ui - service_inchiriere - repository_carti cu scoup de a sterge o inchiriere
            dupa id_client si id_carte daca aceasta exista
        """

        id_client = int(input("Introduceti id-ul clientului: "))
        id_carte = int(input("Introduceti id-ul cartii: "))
        self.__service_inchirieri.stergere_inchiriere(id_client,id_carte)
        print("A fost returnata cartea!")
    
    def ui_generare_clienti_random(self):
        """
            Metoda ce se ocupa cu generarea unui numar introdus de catre utilizator de clienti random
        """

        n = int(input("Introduceti numarul de clienti pe care doriti sa-l generati: "))
        self.__service_clienti.generare_clienti_random(n)
    
    def ui_generare_carti_random(self):
        """
            Metoda ce se ocupa cu generarea unui numar introdus de catre utilizator de carti random
        """

        n = int(input("Introduceti numarul de carti pe care doriti sa-l generati: "))
        self.__service_carti.generare_carti_random(n)
    
    def adauga_carti_clienti(self):

        self.__service_clienti.adauga_client(1,"Stefan Farcasanu",1231231231231)
        self.__service_clienti.adauga_client(2,"Popa Alex",1234567891234)
        self.__service_clienti.adauga_client(3,"Dumitru George",1111111111111)
        self.__service_clienti.adauga_client(4,"Pop Vicentiu",2222222222222)
        self.__service_clienti.adauga_client(5,"Azorica Kevin",3333333333333)

        self.__service_carti.adauga_carte(1,"Tata Bogat","Ed","Robert Kiyosaki")
        self.__service_carti.adauga_carte(2,"Cadranul banilor","Fin","Robert Kiyosaki")
        self.__service_carti.adauga_carte(3,"Think and grow rich","Bus","Autor")
        self.__service_carti.adauga_carte(4,"Banii","Ed fin","Tony Robbins")
        self.__service_carti.adauga_carte(5,"Fii tu insuti","dez","Autor roman")

        self.__service_inchirieri.adauga_inchiriere(1,1,1)
        self.__service_inchirieri.adauga_inchiriere(2,1,2)
        self.__service_inchirieri.adauga_inchiriere(3,2,2)
        self.__service_inchirieri.adauga_inchiriere(4,3,3)
        self.__service_inchirieri.adauga_inchiriere(5,4,4)
        self.__service_inchirieri.adauga_inchiriere(6,5,5)

    def run(self):
        """
            Functia de ruleaza si porneste aplicatia
        """

        #self.adauga_carti_clienti() # adauga 5 clienti/carti/inchirieri

        while True:

            print(self.__meniu)
            cmd = input("Introduceti comanda: ")

            if cmd == "Exit":
                print("La revedere!")
                return

            elif cmd == "Adaugare client":
                try:
                    self.ui_adaugare_client()
                except ValueError:
                    print("Date de intrare invalide")
                except Exception_Repository_Clienti as e:
                    print(e)
                except Validator_client_exception as e:
                    print(e)
            
            elif cmd == "Adaugare carte":
                try:
                    self.ui_adaugare_carte()
                except ValueError:
                    print("Date de intrare invalide!")
                except Exception_Repository_Carti as e:
                    print(e)
                except Validator_carti_exception as e:
                    print(e)
            
            elif cmd == "Adaugare inchiriere":
                try:
                    self.ui_adaugare_inchiriere()
                except ValueError:
                    print("Date de intrare invalide!")
                except Exception_Repository_Inchirieri as e:
                    print(e)
                except Validator_inchirieri_exception as e:
                    print(e)
                except Validator_client_exception as e:
                    print(e)
                except Validator_carti_exception as e:
                    print(e)
                except Exception_Repository_Clienti as e:
                    print(e)
                except Exception_Repository_Carti as e:
                    print(e)

            elif cmd == "Afisare clienti":
                try:
                    l = self.__service_clienti.afiseaza()
                    for elem in l:
                        print(str(elem))
                except Exception_Repository_Clienti as e:
                    print(e)
            
            elif cmd == "Afisare carti":
                try:
                    l = self.__service_carti.afiseaza()
                    for elem in l:
                        print(str(elem))
                except Exception_Repository_Carti as e:
                    print(e)
            
            elif cmd == "Afisare inchirieri":
                try:
                    l = self.__service_inchirieri.afisare_inchirieri()
                    for elem in l:
                        print(str(elem))
                except Exception_Repository_Inchirieri as e:
                    print(e)

            elif cmd == "Cauta client":
                try:
                    self.ui_cauta_client()
                except ValueError:
                    print("Date de intrare invalide")
                except Exception_Repository_Clienti as e:
                    print(e)
                except Validator_client_exception as e:
                    print(e)
            
            elif cmd == "Cauta carte":
                try:
                    self.ui_cauta_carte()
                except ValueError:
                    print("Date de intrare invalide!")
                except Exception_Repository_Carti as e:
                    print(e)
                except Validator_carti_exception as e:
                    print(e)

            elif cmd == "Stergere client":
                try:
                    self.ui_stergere_client()
                except ValueError:
                    print("Date de intrare invalide!")
                except Exception_Repository_Clienti as e:
                    print(e)
                except Validator_client_exception as e:
                    print(e)
            
            elif cmd == "Stergere carte":
                try:
                    self.ui_stergere_carte()
                except ValueError:
                    print("Date de intrare invalide!")
                except Exception_Repository_Carti as e:
                    print(e)
                except Validator_carti_exception as e:
                    print(e)
            
            elif cmd == "Returnare inchiriere":
                try:
                    self.ui_stergere_inchiriere()
                except ValueError:
                    print("Date de intrare invalide!")
                except Exception_Repository_Inchirieri as e:
                    print(e)
                except Validator_inchirieri_exception as e:
                    print(e)
                except Validator_client_exception as e:
                    print(e)
                except Validator_carti_exception as e:
                    print(e)
                except Exception_Repository_Clienti as e:
                    print(e)
                except Exception_Repository_Carti as e:
                    print(e)
                
            elif cmd == "Modifica client":
                try:
                    self.ui_modifica_client()
                except ValueError:
                    print("Date de intrare invalide")
                except Exception_Repository_Clienti as e:
                    print(e)
                except Validator_client_exception as e:
                    print(e)
            
            elif cmd == "Modifica carte":
                try:
                    self.ui_modifica_carte()
                except ValueError:
                    print("Date de intrare invalide!")
                except Exception_Repository_Carti as e:
                    print(e)
                except Validator_carti_exception as e:
                    print(e)
            
            elif cmd == "Genereaza clienti random":
                try:
                    self.ui_generare_clienti_random()
                except ValueError:
                    print("Date de intrare invalide")
                except Exception_service_client as e:
                    print(e)
            
            elif cmd == "Genereaza carti random":
                try:
                    self.ui_generare_carti_random()
                except ValueError:
                    print("Date de intrare invalide")
                except Exception_service_carte as e:
                    print(e)
            
            elif cmd == "Raport cele mai inchiriate carti":
                try:
                    l = self.__service_inchirieri.rapoarte_cele_mai_inchiriate_carti()
                    ct = 1
                    for i in l:
                        print(ct,") ",str(i))
                        ct += 1
                except Exception_Repository_Inchirieri as e:
                    print(e)
            
            elif cmd == "Raport clienti nume":
                try:
                    l = self.__service_inchirieri.raport_clienti_carti_ordonat_nume()
                    ct = 1
                    for i in l:
                        print(ct,") ",str(i))
                        ct += 1
                except Exception_Repository_Inchirieri as e:
                    print(e)
            
            elif cmd == "Raport clienti inchirieri":
                try:
                    l = self.__service_inchirieri.raport_clienti_carti_ordonat_inchirieri()
                    ct = 1
                    for i in l:
                        print(ct,") ",str(i))
                        ct += 1
                except Exception_Repository_Inchirieri as e:
                    print(e)

            elif cmd == "Raport clienti activi":
                try:
                    l = self.__service_inchirieri.raport_clienti_activi()
                    ct = 1
                    for i in l:
                        print(ct,") ",str(i))
                        ct += 1
                except Exception_Repository_Inchirieri as e:
                    print(e)
                except Exception_service_inchirieri as e:
                    print(e)
            
            elif cmd == "Raport autori ordonati descrescator":
                try:
                    l = self.__service_inchirieri.autori_ordonati_descrescator()
                    ct = 1
                    for i in range(0,len(l)):
                        print(ct,") ",str(l[i][0]),l[i][1])
                        ct += 1
                except Exception_Repository_Inchirieri as e:
                    print(e)

            else:
                print("Comanda invalida!")





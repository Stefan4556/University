"""
    Service clienti ce reprezinta legatura dintre ui si repository
    Acest modul apeleaza functii din repository_clienti si domain_clienti
"""

from domain_clienti import Client
from domain_clienti import Validator_client
from repository_clienti import Repository_clienti
from repository_clienti import Exception_Repository_Clienti
from domain_clienti import Validator_client_exception
import string
import random

class Exception_service_client(Exception):
    """
        Clasa ce se ocupa cu erorile ce pot aparea in serivce_client
    """

    pass

class Service_client:
    """
        Clasa service clienti ce contine toate metodele ce realizeaza
        legatura dintre ui si repository_clienti
    """

    def __init__(self,repo,validator):
        """
            Initializam cele doua componente ale service-ului clienti:
            repo - face legatura dintre service_clienti si repository_clienti
            validator - face legatura dintre service_clienti si domain_clienti
        """

        self.__repo = repo
        self.__validator = validator
    
    def adauga_client(self,id,nume,cnp):
        """
            Functia ce se ocupa cu adaugarea unui client, primeste id, nume si tip
            dupa care le valideaza si in momentul in care vrea sa adauge verifica daca
            id-ul este unic, in caz afirmativ este adaugat clientul 
        """ 

        client_curent = Client(id,nume,cnp)

        self.__validator.valideaza_client(client_curent)

        self.__repo.salveaza_client(client_curent)
    
    def cauta(self,id):
        """
            #Aceasta metoda verifica daca exista un client cu id-ul pe care il primeste,
            #in caz afirmativ este returnat clientul, altfel este ridicata o eroare
        """

        client = Client(id,"A",1231231231231)

        self.__validator.valideaza_client(client)

        return self.__repo.cauta_client(id)
    
    def afiseaza(self):
        """
            Realizeaza legatura dintre ui si functia de afisare ce se afla in repostory_clienti
        """

        return self.__repo.afisare_clienti()
    
    def stergere(self,id):
        """
            Realizeaza legatura dintre ui si functia de stergere ce se afla in repository_clienti
        """
        self.verifica_id(id)
        self.__repo.sterge_client_id(id)
    
    def modifica_client(self,id,nume):
        """
            Realizeaza legatura dintre ui si functia de modificare ce se afla in repository_clienti
        """

        self.verifica_id_si_nume(id,nume)
        self.__repo.cauta_client_id_modifica(id,nume)

    def verifica_nume(self,nume):
        """
            Realzieaza legatura dintre ui si functia de validare din domain pentru a valida un nume
        """

        client = Client(21,nume,1234567891234)

        self.__validator.valideaza_client(client)
    
    def verifica_id(self,id):
        """
            Realizeaza legatura dintre ui si functia de validare din domain pentru a verifica un id
        """

        client = Client(id,"A",1234567891234)

        self.__validator.valideaza_client(client)
    
    def verifica_id_si_nume(self,id,nume):
        """
            Realzieaza legatura dintre ui si functia de validare din domain pentru a verifica un id 
            si un nume
        """

        client = Client(id,nume,1234567891234)

        self.__validator.valideaza_client(client)
    
    def cautare_client_existent(self,id):
        """
            Aceasta metoda verifica daca exista un client cu id-ul pe care il primeste,
            in caz afirmativ este returnat clientul, altfel este ridicata o eroare
        """

        self.verifica_id(id)
        return self.__repo.cauta_client_id_gasit(id)
    
    def conversie(self,id):
        """
            Functia ce returneaza obiectul de tip client corespunzator unui id-primit.
            Aceasta apeleaza o functie din repo unde se realizeaza conversia propriu-zisa
        """

        return self.__repo.returneaza_obiect_client(id)
    
    def genereaza_date_client(self):
        """
            Functia se ocupa cu generarea unui singur client random
        """

        #numere = string.digits
        litere = string.ascii_lowercase
        #id_client = ''.join(random.choice(numere) for i in range(3))
        id_client = random.randint(1,999)
        prenume = ''.join(random.choice(litere) for i in range(6))
        nume_familie = ''.join(random.choice(litere) for i in range(6))
        """
        cnp_1 = ''.join(random.choice(numere) for i in range(1))
        while int(cnp_1) == 0:
            cnp_1 = ''.join(random.choice(numere) for i in range(1))
        cnp_2 = ''.join(random.choice(numere) for i in range(12))
        cnp = str(cnp_1 + cnp_2)
        """
        cnp = random.randrange(1000000000000,9999999999999)
        nume = str(nume_familie + prenume)
        return Client(int(id_client),nume,int(cnp)) # pastram int pentru cazul in care folosim ceea ce e comentat

    def generare_clienti_random(self,n):
        """
            Metoda se ocupa cu generarea a n clienti random, n fiind un numar dat de catre utilizator
        """

        if n <= 0:

            raise Exception_service_client("Numarul de clienti pe care doriti sa-i generati este mai mic sau egal cu 0")

        while n != 0:
            try:
                valid_client = Validator_client()
                client = self.genereaza_date_client()
                valid_client.valideaza_client(client)
                self.__repo.salveaza_client(client)
                n -= 1
            except Exception_Repository_Clienti:
                pass

def Teste_service_clienti():

    repo = Repository_clienti()
    vali = Validator_client()
    serv = Service_client(repo,vali)

    # test pentru adaugare
    serv.adauga_client(1,"Dumitru George",1234567891234)
    serv.adauga_client(2,"Gheorghe Dorin",2345678914321)
    serv.adauga_client(3,"Ion Matei",1234567890000)

    try:
        serv.adauga_client(-1,"",123)
        assert False
    except Validator_client_exception:
        assert True

    #test pentru afisare
    lista = serv.afiseaza()
    assert (len(lista)) == 3

    # test pentru stergere
    serv.stergere(1)
    assert (len(lista)) == 2

    try:
        serv.stergere(20)
        assert False
    except Exception_Repository_Clienti:
        assert True

    # test pentru modifica si cauta
    serv.modifica_client(2,"Matei")
    assert serv.cautare_client_existent(2) == "Id: 2, Nume: Matei, CNP: 2345678914321"

    try:
        serv.cautare_client_existent(20)
        assert False
    except Exception_Repository_Clienti:
        assert True

Teste_service_clienti()
    



    
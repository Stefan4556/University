"""
    Service carti reprezinta legatura dintre ui si repository
    Acest modul apeleaza functii din repository_carti si domain_carti
"""

from domain_carti import Carte
from domain_carti import Validator_carte
from repository_carti import Repository_carti
from repository_carti import Exception_Repository_Carti
from domain_carti import Validator_carti_exception
import string
import random

class Exception_service_carte(Exception):
    """
        Clasa ce se ocupa cu stocarea tuturor erorilor ce pot aparea la nivelul service_carti
    """

    pass

class Service_carte:
    """
        Clasa service carti ce contine toate metodele ce realizeaza
        legatura dintre ui si repository_carti
    """

    def __init__(self,repo,validator):
        """
            Initializam cele doua componente ala service-ului carti:
            repo - face legatura dintre service_carti si repository_carti
            validator - face legatura dintre service_carti si domain_carti
        """

        self.__repo = repo
        self.__validator = validator
    
    def adauga_carte(self,id,titlu,descriere,autor):
        """
            Functia ce se ocupa cu adaugarea unei carti, primeste id, titlu, descriere si un autor
            dupa care valideaza aceste date si in momentul in care vrea sa adauge verifica daca 
            id-ul este unic, iar in caz afirmativ este adaugata cartea
        """

        carte_curenta = Carte(id,titlu,descriere,autor)

        self.__validator.valideaza_carte(carte_curenta)

        self.__repo.salveaza_carte(carte_curenta)
    
    def cauta(self,id):
        """
            #Aceasta metoda verifica daca exista o carte cu id-ul pe care-l primeste, in caz afirmativ
            #este returnata cartea, altfel este ridicata o eroare
        """

        carte = Carte(id,"A","B","C")

        self.__validator.valideaza_carte(carte)

        return self.__repo.cauta_carte(id)
    
    def afiseaza(self):
        """
            Realizeaza legatura dintre ui si functia de afisare ce se afla in repository_carti
        """

        return self.__repo.afisare_carti()
    
    def stergere(self,id):
        """
            Realizeaza legatura dintre ui si functia de stergere ce se afla in repository_carti
        """

        self.verifica_id(id)
        
        self.__repo.sterge_carte_id(id)
    
    def modifica_carte(self,id,titlu):
        """
            Realizeaza legatura dintre ui si functia de modificare ce se afla in repository_carti
        """

        self.verifica_id_si_titlu(id,titlu)
        self.__repo.cauta_carte_id_modifica(id,titlu)
    
    def verifica_titlu(self,titlu):
        """
            Realizeaza legatura dintre ui si functia de validare din domain pentru a valida un titlu
        """

        carte = Carte(21,titlu,"A","B")

        self.__validator.valideaza_carte(carte)
    
    def verifica_id(self,id):
        """
            Realizeaza legatura dintre ui si functia de validare din domain pentru a verifca un id
        """

        carte = Carte(id,"A","B","C")

        self.__validator.valideaza_carte(carte)
    
    def verifica_id_si_titlu(self,id,titlu):
        """
            Realizeaza legatura dintre ui si functia de validare din domain pentru a verifica in acelasi timp un id
            si un titlu
        """

        carte = Carte(id,titlu,"A","A")

        self.__validator.valideaza_carte(carte)
    
    def cautare_carte_existenta(self,id):
        """
            Aceasta metoda verifica daca exista o carte cu id-ul pe care-l primeste, in caz afirmativ
            este returnata cartea, altfel este ridicata o eroare
        """

        self.verifica_id(id)
        return self.__repo.cauta_carte_id_gasit(id)
    
    def genereaza_date_carte(self):
        """
            Functia se ocupa cu generarea unei singure carti random
        """

        litere = string.ascii_lowercase
        id_carte = random.randint(1,999)
        titlu = ''.join(random.choice(litere) for i in range(5))
        descriere = ''.join(random.choice(litere) for i in range(5))
        prenume_autor = ''.join(random.choice(litere) for i in range(5))
        nume_autor = ''.join(random.choice(litere) for i in range(5))
        autor = str(nume_autor + prenume_autor)
        return Carte(id_carte,titlu,descriere,autor)

    def generare_carti_random(self,n):
        """
             Metoda se ocupa cu generarea a n carti random, n fiind un numar dat de catre utilizator
        """

        if n <= 0:

            raise Exception_service_carte("Numarul de carti pe care doriti sa le generati este mai mic sau egal cu 0")

        while n != 0:
            try:
                valid_carte = Validator_carte()
                carte = self.genereaza_date_carte()
                valid_carte.valideaza_carte(carte)
                self.__repo.salveaza_carte(carte)
                n -= 1
            except Exception_Repository_Carti:
                pass
    
    def conversie(self,id):
        """
            Functia ce returneaza obiectul de tip carte corespunzator unui id-primit.
            Aceasta apeleaza o functie din repo unde se realizeaza conversia propriu-zisa
        """

        return self.__repo.returneaza_obiect_carte(id)

def Teste_service_carti():

    repo = Repository_carti()
    vali = Validator_carte()
    serv = Service_carte(repo,vali)

    # test pentru adaugare
    serv.adauga_carte(1,"Tata Bogat","Educatie financiara","Robert Kyiosaki")
    serv.adauga_carte(2,"De la idee la bani","Antreprenoriat","Napoleon Hill")
    serv.adauga_carte(3,"Banii stapaneste jocul","Independenta financiara","Tony Robbins")

    try:
        serv.adauga_carte(30,"","","")
        assert False
    except Validator_carti_exception:
        assert True
    
    # test pentru afisare
    lista = serv.afiseaza()
    assert (len(lista)) == 3

    # test pentru stergere
    serv.stergere(1)
    assert (len(lista)) == 2

    try:
        serv.stergere(20)
        assert False
    except Exception_Repository_Carti:
        assert True
    
    # test pentru modifica si cauta

    serv.modifica_carte(2,"Think and grow rich")
    assert serv.cautare_carte_existenta(2) == "Id: 2, Titlu: Think and grow rich, Descriere: Antreprenoriat, Autor: Napoleon Hill"

    try:
        serv.cautare_carte_existenta(20)
        assert False
    except Exception_Repository_Carti:
        assert True

Teste_service_carti()

    
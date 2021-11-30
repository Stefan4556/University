"""
    Service inchirieri ce reprezianta legatura dintre ui si repository inchirieri
    Acest modul reuneste toate cele trei serviceuri, reprezentand clasa de legatura
"""

from domain_inchirieri import Inchiriere
from domain_inchirieri import Validator_inchiriere

from domain_clienti import Client
from domain_clienti import Validator_client

from domain_carti import Carte
from domain_carti import Validator_carte

from repository_inchirieri import Repository_inchirieri
from repository_carti import Repository_carti
from repository_clienti import Repository_clienti

from service_clienti import Service_client
from service_carti import Service_carte

from domain_inchirieri import Validator_inchirieri_exception
from domain_carti import Validator_carti_exception
from domain_clienti import Validator_client_exception

from repository_inchirieri import Exception_Repository_Inchirieri
from repository_carti import Exception_Repository_Carti
from repository_clienti import Exception_Repository_Clienti

from operator import itemgetter
from sortari import BubbleSort,ShellSort,cmp_nume_clienti,cmp_nume_nr_carti,cmp_lista_de_liste,BubbleSortCopie

class Exception_service_inchirieri(Exception):
    """
        Clasa ce se ocupa cu erorile ce pot aparea in service_inchirieri
    """

    pass

class Service_inchirieri:
    """
        Clasa service ce contine toate metodele ce realizeaza legatura dintre cele 3 service-uri si
        legatura dintre ui si repository inchirieri si validatori inchirieri
    """

    def __init__(self,repo_inchirieri,validator_inchirieri,service_clienti,service_carti):
        """
            Initializam cele 4 componente ale service-ului inchirieri:
            repo - face legatura dintre service_inchirieri si repository_inchirieri
            vali - face legatura dintre service_inchirieri si validator_inchirieri
            srv_clienti - face legatura dintre service_inchirieri si service_clienti
            srv_carti - face legatura dintre service_inchirieri si service_carti
        """

        self.__repo = repo_inchirieri
        self.__vali = validator_inchirieri
        self.__srv_clienti = service_clienti
        self.__srv_carti = service_carti
    
    def adauga_inchiriere(self,id_inchiriere,id_client,id_carte):
        """
            Functia ce se ocupa cu adaugarea unei inchirieri, primeste 3 id-uri, id_client pe care-l
            verifica daca exista sau nu in lista de clienti, id_carte pe care-l verifica daca exista
            sau nu in lista de carti si id_inchiriere pe care-l verifica inainte de salvare daca a mai 
            fost folosit
        """

        i = Inchiriere(id_inchiriere,id_client,id_carte)

        self.__vali.valideaza_inchiriere(i)

        self.__srv_clienti.cautare_client_existent(id_client)

        self.__srv_carti.cautare_carte_existenta(id_carte)
        
        self.__repo.salveaza_inchiriere(i)
    
    def id_to_object_client(self,id_client):
        """
            Aceasta metoda se ocupa cu returnarea obiectului de tip client corespunzator unui id primit
        """

        return self.__srv_clienti.conversie(id_client)
    
    def id_to_object_carte(self,id_carte):
        """
            Aceasta metoda se ocupa cu returnarea obiectului de tip carte corespunzator unui id primit
        """

        return self.__srv_carti.conversie(id_carte)

    def afisare_inchirieri(self):
        """
            Functie ce se ocupa cu convertirea listei si returnarea acesteia sub forma de lista de dictionare,
            dictionar format din 3 campuri:
            id_inchiriere - contine id-ul inchirierii
            client - contine obiectul client corespunzator id_client
            carte - contine obiectul carte corespunzator id_carte
        """

        l = []

        lista = self.__repo.returneaza_inchirieri()

        for i in lista:

            #ll = {
                    #'id_inchiriere' : i['id_inchiriere'],
                    #'client': i.id_to_object_client(i['id_client']),
                    #'carte': i.id_to_object_carte(i['id_carte'])
                 #}

            #l.append(ll)

            ll = {
                    'id_inchiriere' : i.getId_inchiriere(),
                    'client': str(self.id_to_object_client(i.getId_client())),
                    'carte': str(self.id_to_object_carte(i.getId_carte()))
                 }

            l.append(ll)
        
        return l

    def stergere_inchiriere(self,id_client,id_carte):
        """
            Functia ce se ocupa cu stergerea unei inchirieri, primeste un id_client si id_carte, dupa care verifica
            daca cele 2 id-uri primite apartin listei de clienti, respectiv listei de carti, daca totul este ok se incearca 
            stergerea, in cazul in care este gasita inchirierea este stearsa, altfel este ridicata o eroare prin care este
            anuntat utilizatorul
        """

        self.__srv_clienti.cautare_client_existent(id_client)
        
        self.__repo.verifica_id_client_exista(id_client)

        self.__srv_carti.cautare_carte_existenta(id_carte)

        self.__repo.verifica_id_carte_exista(id_carte)

        self.__repo.sterge(id_client,id_carte)
    
    def stergere_inchiriere_id_client(self,id_client):
        """
            Functie ce se ocupa cu actualizarea listei de inchirieri in cazul in care este sters un client
        """

        self.__repo.stergere_id_client(id_client)
    
    def stergere_inchiriere_id_carte(self,id_carte):
        """
            Functie ce se ocupa cu actualizarea listei de inchirieri in cazul in care este stearsa o carte
        """

        self.__repo.stergere_id_carte(id_carte)
    
    def rapoarte_cele_mai_inchiriate_carti(self):
        """
            Functia ce realizeaza raportul legat de cele mai inchiriate carti
        """

        l = self.__repo.returneaza_inchirieri()

        lista = []

        for i in range(0,len(l)):

            gasit = 0

            for j in range(0,len(lista)):
                if lista[j][0] == l[i].getId_carte():
                    gasit = 1
                    break

            if gasit == 1:
                for j in range(0,len(lista)):
                    if l[i].getId_carte() == lista[j][0]:
                        lista[j][1] += 1
                        break
            else: 
                ll = []
                ll.append(l[i].getId_carte())
                ll.append(1)
                lista.append(ll)
        
        #lista = sorted(lista, key=itemgetter(1), reverse=True)

        #lista = BubbleSort(lista,cmp_lista_de_liste,rev=True)

        lista = BubbleSort(lista,rev=True)

        lista_noua = []

        for i in range(0,len(lista)):

            lista_noua.append(self.id_to_object_carte(lista[i][0]))

        return lista_noua
    
    def raport_clienti_carti_ordonat_nume(self):
        """
            Functia ce realizeaza raportul legat de ordonarea clientilor in ordine alfabetica ce au cel putin o inchiriere
        """

        l = self.__repo.returneaza_inchirieri()

        lista = []

        for i in range(0,len(l)):

            if l[i].getId_client() not in lista:
                lista.append(l[i].getId_client())
        
        for i in range(0,len(lista)):

            lista[i] = self.id_to_object_client(lista[i])
       
        ''' for i in range(0,len(lista)-1):
            for j in range(i+1,len(lista)):

                if lista[i].getNume() > lista[j].getNume():

                    lista[i],lista[j] = lista[j],lista[i] '''
        
        #lista = ShellSort(lista,cmp_nume_clienti)

        lista = ShellSort(lista)

        return lista
    
    def raport_clienti_carti_ordonat_inchirieri(self):
        """
            Functia ce realizeaza raportul legat de ordonarea clientilor dupa numarul de inchirieri
        """

        l = self.__repo.returneaza_inchirieri()

        lista = []

        for i in range(0,len(l)):

            gasit = 0

            for j in range(0,len(lista)):

                if lista[j][0] == l[i].getId_client():
                    gasit = 1
                    break
            
            if gasit == 1:

                for j in range(0,len(lista)):

                    if lista[j][0] == l[i].getId_client():
                        lista[j][1] += 1
                        break 

            else:

                ll = []
                ll.append(l[i].getId_client())
                ll.append(1)
                lista.append(ll)
        
        #lista = sorted(lista, key=itemgetter(1), reverse=True)

        #lista = BubbleSort(lista,cmp_lista_de_liste,rev=True)

        lista = BubbleSort(lista,rev=True)

        lista_noua = []

        for i in range(0,len(lista)):

            lista_noua.append(self.id_to_object_client(lista[i][0]))
        
        return lista_noua
    
    def raport_clienti_activi(self):
        """
            Functia ce realizeaza raportul legat de cei mai activi 20% din clienti ordonati dupa numarul de inchirieri si ordonati alfabetic
        """

        l = self.__repo.returneaza_inchirieri()

        lista = []

        for i in range(0,len(l)):

            gasit = 0

            for j in range(0,len(lista)):
    
                if lista[j][0] == l[i].getId_client():
                    gasit = 1
                    break
            
            if gasit == 1:

                for j in range(0,len(lista)):

                    if lista[j][0] == l[i].getId_client():
                        lista[j][1] += 1
                        break 

            else:

                ll = []
                ll.append(l[i].getId_client())
                ll.append(1)
                lista.append(ll)
        
        if len(lista) < 5:

            raise Exception_service_inchirieri("Nu sunt suficienti clienti cu carti inchiriate pentru a putea fi afisati primii 20%!")

        for i in range(0,len(lista)):

            lista[i][0] = self.id_to_object_client(lista[i][0])

        ''' for i in range(0,len(lista)-1):
            for j in range(i+1,len(lista)):

                if lista[i][1] < lista[j][1]:
                    lista[i],lista[j] = lista[j],lista[i]
                
                elif lista[i][1] == lista[j][1]:

                    if lista[i][0].getNume() < lista[j][0].getNume():

                        lista[i],lista[j] = lista[j],lista[i] '''
        
        #lista = ShellSort(lista,cmp_nume_nr_carti,rev=True) # aceasta este tema

        lista = BubbleSortCopie(lista,rev=True) # cerinta lab

        lista_noua = []

        for i in range(0,len(lista)): # trebuie sa fie //5 pentru a afisa primii 20%, dar pentru a se vedea ca merge sortarea este sters

            lista_noua.append(lista[i][0])
        
        return lista_noua
    
    def autori_ordonati_descrescator(self):
        """
            Cerinta pentru lab: ordonare autori descrescator dupa nr de inchirieri
        """

        l = self.__repo.returneaza_inchirieri()

        lista = []

        copie = list(l)

        for i in range(0,len(copie)):

            copie[i] = self.id_to_object_carte(copie[i].getId_carte())

            copie[i] = copie[i].getAutor()

            gasit = 0

            for j in range(0,len(lista)):
                if lista[j][0] == copie[i]:
                    gasit = 1
                    break
            
            if gasit == 1:
                for j in range(0,len(lista)):
                    if copie[i] == lista[j][0]:
                        lista[j][1] += 1
                        break
            else:
                ll = []
                ll.append(copie[i])
                ll.append(1)
                lista.append(ll)
        
        #lista = sorted(lista, key=itemgetter(1), reverse=True)

        lista = BubbleSort(lista,cmp_lista_de_liste,rev=True)

        return lista

def Teste_service_inchirieri():

    repo = Repository_inchirieri()
    vali = Validator_inchiriere()

    repo_clienti = Repository_clienti()
    vali_clienti = Validator_client()
    srv_clienti = Service_client(repo_clienti,vali_clienti)

    repo_carti = Repository_carti()
    vali_carti = Validator_carte()
    srv_carti = Service_carte(repo_carti,vali_carti)

    srv_clienti.adauga_client(1,"Stefan Farcasanu",1234567891234)
    srv_clienti.adauga_client(2,"Andrei Grig",1234567891299)
    srv_clienti.adauga_client(3,"Dumitru Gheorghe",1234327891299)
    srv_clienti.adauga_client(4,"Alex Popescu",2323232323232)
    srv_clienti.adauga_client(5,"Rares Stanga",1212121212121)

    srv_carti.adauga_carte(1,"Tata Bogat","Educatie financiara","Robert Kyiosaki")
    srv_carti.adauga_carte(2,"De la idee la bani","Antreprenoriat","Napoleon Hill")
    srv_carti.adauga_carte(3,"Banii stapaneste jocul","Independenta financiara","Tony Robbins")
    srv_carti.adauga_carte(4,"Secretele succesului","Dezvoltare personala","Carnegie")
    srv_carti.adauga_carte(5,"Unshakeable","Business","Tony Robbins")

    serv = Service_inchirieri(repo,vali,srv_clienti,srv_carti)

    # test pentru adaugare
    serv.adauga_inchiriere(1,1,1)
    serv.adauga_inchiriere(2,2,2)
    serv.adauga_inchiriere(3,3,3)

    # test pentru afisare
    lista = serv.afisare_inchirieri()
    assert(len(lista)) == 3

    try:
        serv.adauga_inchiriere(-1,1,1)
        assert False
    except Validator_inchirieri_exception:
        assert True
    
    # test id_to_object_client
    assert(str(serv.id_to_object_client(1))) == "Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234"
    assert(str(serv.id_to_object_client(2))) == "Id: 2, Nume: Andrei Grig, CNP: 1234567891299"

    # test id_to_object_carte
    assert(str(serv.id_to_object_carte(1))) == "Id: 1, Titlu: Tata Bogat, Descriere: Educatie financiara, Autor: Robert Kyiosaki"
    assert(str(serv.id_to_object_carte(2))) == "Id: 2, Titlu: De la idee la bani, Descriere: Antreprenoriat, Autor: Napoleon Hill"

    # test pentru stergere inchiriere
    serv.stergere_inchiriere(1,1)
    lista = serv.afisare_inchirieri()
    assert(len(lista)) == 2

    try:
        serv.stergere_inchiriere(20,2)
        assert False
    except Exception_Repository_Clienti:
        assert True
    
    try:
        serv.stergere_inchiriere(2,20)
        assert False
    except Exception_Repository_Carti:
        assert True

    # test pentru stergere_inchiriere_id_client
    serv.stergere_inchiriere_id_client(2)
    lista = serv.afisare_inchirieri()
    assert (len(lista)) == 1
    serv.stergere_inchiriere_id_client(5)
    assert (len(lista)) == 1

    # test pentru stergere_inchiriere_id_carte
    serv.stergere_inchiriere_id_carte(3)
    try:
        lista = serv.afisare_inchirieri()
        assert False
    except Exception_Repository_Inchirieri:
        assert True
    
    serv.adauga_inchiriere(1,1,1)
    serv.adauga_inchiriere(2,2,2)
    serv.adauga_inchiriere(3,3,3)

    # test pentru rapoarte cele mai inchiriate carti

    lista = serv.rapoarte_cele_mai_inchiriate_carti()
    assert(len(lista)) == 3
    serv.stergere_inchiriere(2,2)
    serv.stergere_inchiriere(3,3)
    serv.adauga_inchiriere(2,2,1)
    lista = serv.rapoarte_cele_mai_inchiriate_carti()
    assert(len(lista)) == 1
    assert(str(lista[0])) == "Id: 1, Titlu: Tata Bogat, Descriere: Educatie financiara, Autor: Robert Kyiosaki"

    # test pentru rapoarte clienti ordonati dupa nume
    serv.stergere_inchiriere(2,1)
    serv.adauga_inchiriere(2,2,2)
    serv.adauga_inchiriere(3,3,3)
    lista = serv.raport_clienti_carti_ordonat_nume()
    assert(len(lista)) == 3
    assert(str(lista[0])) == "Id: 2, Nume: Andrei Grig, CNP: 1234567891299"

    # test pentru rapoarte clienti ordonati dupa nr de inchirieri
    serv.stergere_inchiriere(1,1)
    serv.stergere_inchiriere(2,2)
    serv.stergere_inchiriere(3,3)
    serv.adauga_inchiriere(1,1,1)
    serv.adauga_inchiriere(2,1,2)
    serv.adauga_inchiriere(3,3,3)
    lista = serv.raport_clienti_carti_ordonat_inchirieri()
    assert(len(lista)) == 2
    assert(str(lista[0])) == "Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234"

    # test pentru rapoarte clienti activi
    try:
        lista = serv.raport_clienti_activi()
        assert False
    except Exception_service_inchirieri:
        assert True
    
    serv.adauga_inchiriere(4,4,4)
    serv.adauga_inchiriere(5,5,5)
    serv.adauga_inchiriere(6,2,2)
    lista = serv.raport_clienti_activi()
    assert(str(lista[0])) == "Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234"

Teste_service_inchirieri()





        
       


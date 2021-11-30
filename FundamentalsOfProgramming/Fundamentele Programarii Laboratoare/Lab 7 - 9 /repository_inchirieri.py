"""
    Repository inchirieri cu rolul de a retine lista de carti si operatiile ce se fac pe aceasta
"""

from domain_inchirieri import Inchiriere

class Exception_Repository_Inchirieri(Exception):
    """
        Clasa ce retine erorile ce pot aparea la nivelul repository-ului
    """

    pass

class Repository_inchirieri():
    """
        Clasa ce se ocupa cu retinerea listei de inchirieri si operatiile ce se pot efectua la niveul acesteia
    """

    def __init__(self):
        """
            Initializam lista de inchirieri ca fiind vida
        """

        self.__lista_inchirieri = []
    
    def __len__(self):
        """
            Definim lungimea listei 
        """

        return len(self.__lista_inchirieri)
    
    def salveaza_inchiriere(self,i):
        """
            Functie ce este apelata de catre service pentru a verifica daca inchirierea este valida si poate fi
            salvata, daca este buna aceasta este salvata, altfel este ridicata o eroare specifica
        """

        if self.cauta_id(i.getId_inchiriere()) == 0:

            raise Exception_Repository_Inchirieri("Exista deja o inchiriere cu acest id!")
        
        if self.cauta_inchiriere(i) == 0:

            raise Exception_Repository_Inchirieri("Clientul a inchiriat deja aceasta carte!")

        #l = {
                #'id_inchiriere': i.getId_inchiriere(),
                #'client': i.getId_client(),
                #'carte': i.getId_carte()
            #}
        #self.__lista_inchirieri.append(l)
        self.__lista_inchirieri.append(i)

    def cauta_id(self,id_inch):
        """
            Functia se ocupa cu verificarea daca exista sau nu id-ul respectiv, in caz afirmativ este returnat 0
            pentru a spune ca exista, altfel este returnat 1 pentru a spune ca nu exista
        """

        for i in self.__lista_inchirieri:

            if i.getId_inchiriere() == id_inch:

                return 0
        
        return 1

    def cauta_inchiriere(self,i):
        """
            Functia se ocupa cu verificarea daca exista sau nu o inchiriere, in caz afirmativ este returnat 0
            pentru a spune ca exista, altfel este returnat 1 pentru a spune ca nu exista
        """

        for el in self.__lista_inchirieri:

            if el.getId_carte() == i.getId_carte() and el.getId_client() == i.getId_client():

                return 0

        return 1 

    def returneaza_inchirieri(self):
        """
            Aceasta functie returneaza lista de inchirieri daca aceasta nu este vida, iar in cazul in care este 
            vida aceasta ridica o eroare prin care spune acest lucru, altfel este returnata lista de obiecte
        """

        if len(self.__lista_inchirieri) > 0:
            return self.__lista_inchirieri
        else:
            raise Exception_Repository_Inchirieri("Nu au fost realizate inchirieri!")
    
    def sterge(self,id_client,id_carte):
        """
            Cu ajutorul acestei functii stergem o inchiriere a unui client, in cazul in care aceasta inchiriere
            exista, este stearsa, altfel exista doua cazuri, unul este ca lista de inchirieri este goala, iar 
            celalalt este ca nu exista o inchiriere cu acele id-uri primite
        """

        if len(self.__lista_inchirieri) > 0:
            for i in range(len(self.__lista_inchirieri)):
                if self.__lista_inchirieri[i].getId_client() == id_client and self.__lista_inchirieri[i].getId_carte() == id_carte:
                    self.__lista_inchirieri.pop(i)
                    return
            raise Exception_Repository_Inchirieri("Clientul nu a inchiriat aceasta carte!") 
        else:
            raise Exception_Repository_Inchirieri("Nu au fost realizate inchirieri!")
    
    def verifica_id_client_exista(self,id):
        """
            Aceasta functie verifica daca clientul a inchirat sau nu vreo carte
        """

        for i in self.__lista_inchirieri:

            if i.getId_client() == id:

                return 
        
        raise Exception_Repository_Inchirieri("Clientul nu a inchiriat vreo carte!")

    def verifica_id_carte_exista(self,id):
        """
            Aceasta functie verifica daca o cartea a fost inchirata sau nu
        """
    
        for i in self.__lista_inchirieri:

            if i.getId_carte() == id:

                return 
        
        raise Exception_Repository_Inchirieri("Cartea nu a fost inchiriata de vreun client!")

    def stergere_id_client(self,id_client):
        """
            Aceasta functie este folosita pentru actualizarea listei de inchirieri in cazul in care
            este sters un client din lista de clienti pentru a nu exista inregistrari a unor clienti 
            ce nu exista
        """

        for i in range(len(self.__lista_inchirieri)-1,-1,-1):

            if self.__lista_inchirieri[i].getId_client() == id_client:

                self.__lista_inchirieri.pop(i)
    
    def stergere_id_carte(self,id_carte):
        """
            Aceasta functie este folosita pentru actualizarea listei de inchirieri in cazul in care
            este stearsa o carte din lista de carti pentru a nu exista inregistrari a unor carti ce 
            nu exista
        """
    
        for i in range(len(self.__lista_inchirieri)-1,-1,-1):

            if self.__lista_inchirieri[i].getId_carte() == id_carte:

                self.__lista_inchirieri.pop(i)

class Extended_repository_inchirieri(Repository_inchirieri):
    """
        Clasa ce este realizata prin mostenire si are rolul de a adauga optiunea de a lua date din fisier, scrie date din fisier si de a modifica date din fisier
    """

    def __init__(self,file):
        """
            Aceasta metoda initializeaza lista de inchirieri si stocheaza in ea inchirierile ce se afla in fisier
        """

        self.__file = file
        Repository_inchirieri.__init__(self)
        self.__load_from_file()
    
    def __load_from_file(self):
        """
            Rolul acestei metode este de a converti un sir de stringuri intr-o inchiriere datele acesteia fiind stocate intr-un fisier
        """

        try:
            f = open(self.__file,"r")
        except IOError:
            return
    
        line = f.readline().strip()
        while line != "":
            valori = line.split(",")
            i = Inchiriere(int(valori[0]),int(valori[1]),int(valori[2]))
            Repository_inchirieri.salveaza_inchiriere(self,i)
            line = f.readline().strip()
        f.close()
    
    def __write_to_file(self):
        """
            Aceasta metoda se ocupa cu scrierea in fisier, in cazul in care apare vreo modificare/adaugare/sterere din lista aceasta functie este apelata
        """

        try:
            lista = self.returneaza_inchirieri()
        except Exception_Repository_Inchirieri:
            lista = []
        f = open(self.__file,"w")
        if len(lista) > 0:
            for inc in lista:

                inchiriere = str(inc.getId_inchiriere()) + "," + str(inc.getId_client()) + "," + str(inc.getId_carte()) + "\n"
                f.write(inchiriere)
        else:
            f.write("")
        f.close()
    
    def salveaza_inchiriere(self,i):
        """
            Metoda salveaza_inchiriere se ocupa cu apelarea functiei din clasa mama pentru salvarea unei inchirieri, dupa care se ocupa cu actualizarea fisierului
        """

        super().salveaza_inchiriere(i)
        self.__write_to_file()
    
    def sterge(self,id_client,id_carte):
        """
            Aceasta functie se ocupa cu apelarea functiei mostenite din clasa mama si cu actualizarea listei de carti in cazul in care este stearsa o inchiriere
        """

        super().sterge(id_client,id_carte)
        self.__write_to_file()
    
    def stergere_id_client(self,id):
        """
            Aceasta functie este folosita pentru mentenanta listei de inchirieri si este apelata in cazul in care este sters un client din lista de clienti, pe scurt
            apeleaza functia de clasa mama dupa care actualizeaza fisierul de inchirieri
        """

        super().stergere_id_client(id)
        self.__write_to_file()
    
    def stergere_id_carte(self,id):
        """
            Aceasta functie este folosita pentru mentenanta listei de inchirieri si este apelata in cazul in care este stearsa o carte din lista de carti, pe scurt
            apeleaza functia de clasa mama dupa care actualizeaza fisierul de inchirieri
        """

        super().stergere_id_carte(id)
        self.__write_to_file()

def Teste_repository_inchirieri():

    test = Repository_inchirieri()

    # test pentru salveaza
    i = Inchiriere(1,2,3)
    test.salveaza_inchiriere(i)
    assert(len(test)) == 1

    # test pentru cauta_id
    assert(test.cauta_id(0)) == 1
    assert(test.cauta_id(1)) == 0

    # test pentru cauta_inchiriere
    i = Inchiriere(1,2,3)
    assert(test.cauta_inchiriere(i)) == 0
    i = Inchiriere(1,3,3)
    assert(test.cauta_inchiriere(i)) == 1

    # test pentru sterge
    test.sterge(2,3)
    assert(len(test)) == 0

    # test pentru verifica id_client_exista
    i = Inchiriere(1,2,3)
    test.salveaza_inchiriere(i)
    assert(test.verifica_id_client_exista(2)) == None

    # test pentru verifica id_carte_exista
    assert(test.verifica_id_carte_exista(3)) == None

    # test pentru stergere_id_client
    i = Inchiriere(2,2,4)
    test.salveaza_inchiriere(i)
    test.stergere_id_client(2)
    assert(len(test)) == 0

    # test pentru stergere_id_carte
    i = Inchiriere(1,1,2)
    test.salveaza_inchiriere(i)
    i = Inchiriere(2,2,2)
    test.salveaza_inchiriere(i)
    test.stergere_id_carte(2)
    assert(len(test)) == 0

    # test pentru returnare lista inchirieri
    i = Inchiriere(1,1,1)
    test.salveaza_inchiriere(i)

    try:
        test.returneaza_inchirieri()
        assert True
    except Exception_Repository_Inchirieri:
        assert False
    
    test.sterge(1,1)
    assert(len(test)) == 0

    try:
        test.returneaza_inchirieri()
        assert False
    except Exception_Repository_Inchirieri:
        assert True
        

Teste_repository_inchirieri()

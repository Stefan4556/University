"""
    Repository carti cu rolul de a retine lista de carti si operatiile ce se fac pe aceasta
"""

from domain_carti import Carte

class Exception_Repository_Carti(Exception):
    """
        Clasa ce retine erorile ce pot aparea la niveul repository-ului
    """

    pass

class Repository_carti():
    """
        Clasa ce se ocupa cu retinerea listei de clienti si operatiile ce se pot efectua la nivelul acesteia
    """

    def __init__(self):
        """
            Initializam lista de carti ca fiind vida
        """

        self.__lista_carti = []
    
    def __len__(self):
        """
            Definim lungimea listei
        """

        return len(self.__lista_carti)
    
    def salveaza_carte(self,c):
        """
            Functie ce este apelata de catre service pentru a verifica daca id-ul este unic, pentru ca toate celelalte
            date sunt validate deja, daca id-ul e unic, elementul este adaugat, in caz contrar este ridicata o eroare
        """
        try:
            l = self.afisare_carti()
        except Exception_Repository_Carti:
            l = []

        #if self.cauta_carte(c.getId_carte()) != None:
        if self.cauta_carte_recursiv(c.getId_carte(),l) != None:

            raise Exception_Repository_Carti("Exista deja o carte cu acest ID!")
        
        self.__lista_carti.append(c)
    
    def cauta_carte(self,id_carte):
        """
            Functia se ocupa cu cautarea unei carti al carei id il stim
        """

        for i in self.__lista_carti:

            if i.getId_carte() == id_carte:

                return str(i)
        
        return None
    
    def cauta_carte_recursiv(self,id_carte,lista):
        """
            Functia ce cauta recursiv o carte dupa id si returneaza str de carte daca aceasta exista si none daca nu exista
        """

        if len(lista) == 0:

            return None
        
        if lista[0].getId_carte() == id_carte:

            return str(lista[0])
        
        return self.cauta_carte_recursiv(id_carte,lista[1:])
    
    def sterge_carte_id(self,id_carte):
        """
            Cu ajutorul acestei functii stergem o carte al carui id il primim, in cazul in care nu
            exista o carte cu acest id este ridicata o exceptie ce spune ca nu exista o carte cu 
            id-ul respectiv

            Iar in cazul in care lista este vida, dar totusi datele introduse de catre utilizator 
            sunt corecte, programul o sa ridice o eroare prin care o sa-l anunte pe acesta faptul 
            ca lista este vida
        """

        if len(self.__lista_carti) == 0:
            raise Exception_Repository_Carti("Lista de carti este goala!")

        for i in range(0, len(self.__lista_carti)):

            if self.__lista_carti[i].getId_carte() == id_carte:

                self.__lista_carti.pop(i)
                return 
        
        raise Exception_Repository_Carti("Nu a fost gasita o carte cu id-ul citit!")

    def afisare_carti(self):
        """
            Aceasta functie returneaza lista de carti daca aceasta nu este vida, iar in cazul in care
            este vida ridica o eroare prin care il anunta pe utilizator ca lista este goala
        """

        if len(self.__lista_carti) > 0:
            return self.__lista_carti
        else:
            raise Exception_Repository_Carti("Lista de carti este goala!")
    
    def modifica_carte_titlu(self,id_carte,nume_carte):
        """
            Aceasta functie modifica titlul unei carti
        """

        for i in range(0,len(self.__lista_carti)):
            if self.__lista_carti[i].getId_carte() == id_carte:
                self.__lista_carti[i].setTitlu(nume_carte)
                return 
    
    def cauta_carte_id_gasit(self,id):
        """
            Aceasta functie are rolul de a verifica daca o carte exista sau nu in lista, avand un id dat
            in cazul in care se gaseste, cartea este returnata sub forma de string, iar in cazul in care
            nu este gasita este ridica o exceptie prin care utilizatorul este anuntat ca nu exista o carte
            cu id-ul dat

            Totodata este verificat daca lista de carti este vida sau nu
        """

        if(len(self.__lista_carti)) == 0:
            raise Exception_Repository_Carti("Lista de carti este goala!")
            
        #valoare = self.cauta_carte(id)
        l = self.afisare_carti()
        valoare = self.cauta_carte_recursiv(id,l)

        if valoare != None:
            return valoare
        else:
            raise Exception_Repository_Carti("Nu a fost gasita o carte cu id-ul dat!")
    
    def cauta_carte_id_modifica(self,id,titlu):
        """
            Rolul functiei este de a cauta si modifica daca exista o carte cu id-ul primit in lista, in caz afirmativ
            titlul cartii este mdoficiat cu cel primit, iar in cazul in care nu exista, este ridicata o eroare ce are 
            rolul de a-l informa pe utilziator ca nu exista cartea pe care vrea sa o modifice

            Totodata este verificat daca lista de carti este vida sau nu
        """

        if len(self.__lista_carti) == 0:
            raise Exception_Repository_Carti("Lista de carti este goala!")

        #valoare = self.cauta_carte(id)
        l = self.afisare_carti()
        valoare = self.cauta_carte_recursiv(id,l)

        if valoare != None:
            self.modifica_carte_titlu(id,titlu)
        else:
            raise Exception_Repository_Carti("Nu exista cartea cautata!")
    
    def returneaza_obiect_carte(self,id):
        """
            Aceasta returneaza obiectul de tip carte cu id-ul primit
        """

        for i in self.__lista_carti:

            if i.getId_carte() == id:
                return i

class Extended_repository_carti(Repository_carti):
    """
        Clasa ce este realizata prin mostenire si are rolul de a adauga optiunea de a lua date din fisier, scrie date din fisier si de a modifica date din fisier
    """

    def __init__(self,file):
        """
            Aceasta metoda initializeaza lista de carti si stocheaza in ea cartile ce se afla in fisier
        """

        self.__file = file
        Repository_carti.__init__(self)
        self.__load_from_file()
    
    def __load_from_file(self):
        """
            Rolul acestei metode este de a converti un sir de stringuri intr-o carte, datele acesteia fiind stocate intr-un fisier
        """

        try:
            f = open(self.__file,"r")
        except IOError:
            return
        
        line = f.readline().strip()
        while line != "":
            valori = line.split(",")
            c = Carte(int(valori[0]),valori[1],valori[2],valori[3])
            Repository_carti.salveaza_carte(self,c)
            line = f.readline().strip()
        f.close()
    
    def __write_to_file(self):
        """
            Aceasta metoda se ocupa cu scrierea in fisier, in cazul in care apare vreo modificare/adaugare/sterere din lista aceasta functie este apelata
        """
        try:
            lista = self.afisare_carti()
        except Exception_Repository_Carti:
            lista = []
        f = open(self.__file,"w")
        if len(lista) > 0:
            for ca in lista:
                carte = str(ca.getId_carte()) + "," + ca.getTitlu() + "," + ca.getDescriere() + "," + ca.getAutor() + "\n"
                f.write(carte)
        else:
            f.write("")
        f.close()
    
    def salveaza_carte(self,c):
        """
            Metoda salveaza_carte se ocupa cu apelarea functiei din clasa mama pentru salvarea unei carti, dupa care se ocupa cu actualizarea fisierului
        """

        super().salveaza_carte(c)
        self.__write_to_file()
    
    def sterge_carte_id(self,id):
        """
            Aceasta functie se ocupa cu apelarea functiei mostenite din clasa mama si cu actualizarea listei de carti in cazul in care este stearsa o carte
        """

        super().sterge_carte_id(id)
        self.__write_to_file()
    
    def modifica_carte_titlu(self,id,nume):
        """
            Metoda scrisa are rolul de a apela functia de modificare din clasa mama si de a actualiza fisierul in cazul in care apare vreo modificare in lista
        """

        super().modifica_carte_titlu(id,nume)
        self.__write_to_file()


def Teste_repository_carti():

    test = Repository_carti()

    c = Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")

    # test pentru salveaza
    test.salveaza_carte(c)
    assert(len(test) == 1) == True

    # test pentru functia finala cauta carte dupa id
    assert(test.cauta_carte(0)) == None
    assert(test.cauta_carte(1)) == "Id: 1, Titlu: Tata Bogat Tata Sarac, Descriere: Educatie financiara, Autor: Robert Kiyosaki"

    # test pentru stergere carte dupa id
    test.sterge_carte_id(1)
    assert(len(test)) == 0

    # test functia finala modifica carte titlu
    c = Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")
    test.salveaza_carte(c)
    assert(len(test)) == 1
    test.cauta_carte_id_modifica(1,"Schimbat")
    assert(test.cauta_carte(1)) == "Id: 1, Titlu: Schimbat, Descriere: Educatie financiara, Autor: Robert Kiyosaki"

    # test pentru functia cauta
    assert(test.cauta_carte_id_gasit(1)) == "Id: 1, Titlu: Schimbat, Descriere: Educatie financiara, Autor: Robert Kiyosaki"
    c = Carte(2,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")
    test.salveaza_carte(c)
    assert(test.cauta_carte_id_gasit(2)) == "Id: 2, Titlu: Tata Bogat Tata Sarac, Descriere: Educatie financiara, Autor: Robert Kiyosaki"

    # test pentru functia cauta recursiv
    l = test.afisare_carti()
    assert(test.cauta_carte_recursiv(1,l) == "Id: 1, Titlu: Schimbat, Descriere: Educatie financiara, Autor: Robert Kiyosaki")
    assert(test.cauta_carte_recursiv(2,l) == "Id: 2, Titlu: Tata Bogat Tata Sarac, Descriere: Educatie financiara, Autor: Robert Kiyosaki")
    assert(test.cauta_carte_recursiv(100,l) == None)
    
Teste_repository_carti()
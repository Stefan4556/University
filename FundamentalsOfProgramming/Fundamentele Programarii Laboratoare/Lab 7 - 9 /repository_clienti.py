"""
    Repository clienti cu rolul de a retine lista de clienti si operatiile ce se fac pe lista
"""

from domain_clienti import Client

class Exception_Repository_Clienti(Exception):
    """
        Clasa ce retine erorile ce pot aparea la nivelul repository-ului
    """

    pass

class Repository_clienti():
    """
        Clasa ce se ocupa cu retinerea listei de clienti si operatiile ce se pot efectua la nivelul acesteia
    """

    def __init__(self):
        """
            Initializam lista ca fiind vida
        """
        self.__lista_clienti = []
    
    def __len__(self):
        """
            Definim lungimea listei
        """

        return len(self.__lista_clienti)

    def salveaza_client(self,c):
        """
            Functie ce este apelata de service pentru a verifica daca id-ul este unic, pentru ca toate celelalte
            date sunt validate deja, daca este bun elementul este adaugat, in caz contrar este ridicata o eroare
        """
        try:
            l = self.afisare_clienti()
        except Exception_Repository_Clienti:
            l = []

        #if self.cauta_client(c.getId_client()) != None:
        if self.cauta_client_recursiv(c.getId_client(),l) != None:

            raise Exception_Repository_Clienti("Exista deja un client cu acest ID!")

        self.__lista_clienti.append(c)
    
    def cauta_client(self,id_client):
        """
            Functia se ocupa cu cautarea in lista a unui client al carui id il stim
        """

        for i in self.__lista_clienti:

            if i.getId_client() == id_client:

                return str(i)       
        
        return None

    def cauta_client_recursiv(self,id_client,lista):
        """
            Functia ce cauta recursiv un client dupa id si returneaza str de client daca acesta exista si none daca nu exista
            Analizam complexitatea acestei functii:
                Best case - se gaseste pe prima pozitie => Theta(1) - complexitate constanta
                Worst case - nu exista => Theta(n) - complexitate liniara
                Average case - S = 1 * P(1) + 2 * P(2) + ... + n * P(n) + (n+1) * P(n+1) => S = 1 / (n+1) + 2 / (n+1) + ... + n / (n+1) + (n+1) / (n+1) => S = (n + 1) * (n + 2) / (2 * (n + 1)) =>
                             - S = (n + 2) / 2 care apartine complexitatii Theta (n)
                Overall case - O(n) - este limita superioara in grafic 
        """

        if len(lista) == 0:

            return None

        if lista[0].getId_client() == id_client:

            return str(lista[0])

        return self.cauta_client_recursiv(id_client,lista[1:]) 
    
    def sterge(self,lista,id_client,i):
        """
            Functia recursiva ce se ocupa cu stergerea unui client din lista de clienti
        """

        if len(lista) == i:

            raise Exception_Repository_Clienti("Nu a fost gasit un client cu id-ul citit!")
        
        if lista[i].getId_client() == id_client:

            self.__lista_clienti.pop(i)
            return

        return self.sterge(lista,id_client,i+1) 

    def sterge_client_id(self,id_client):
        """
            Cu ajutorul acestei functii stergem un client al carui id il primim, in cazul in care nu
            exista un client cu acest id este ridicata o exceptie ce spune ca nu exista un client cu 
            id-ul primit

            Iar in cazul in care lista este vida, dar totusi datele introduse de catre utilizator 
            sunt corecte, programul o sa ridice o eroare prin care o sa-l anunte pe acesta faptul 
            ca lista este vida
        """

        if len(self.__lista_clienti) == 0:
            raise Exception_Repository_Clienti("Lista de clienti este goala!")

        ''' for i in range(0, len(self.__lista_clienti)):

            if self.__lista_clienti[i].getId_client() == id_client:

                self.__lista_clienti.pop(i)
                return

        raise Exception_Repository_Clienti("Nu a fost gasit un client cu id-ul citit!") '''
        lista = self.afisare_clienti()
        self.sterge(lista,id_client,0)

    def afisare_clienti(self):
        """
            Aceasta functie returneaza lista de clienti daca aceasta nu este vida, iar in cazul in care
            este vida ridica o eroare prin care ii aduce la cunostinta utilziatorului faptul ca lista e 
            vida
        """

        if len(self.__lista_clienti) == 0:
            raise Exception_Repository_Clienti("Lista de clienti este goala!")
        else:
            return self.__lista_clienti
    
    def modifica_client_nume(self,id_client,nume_client):
        """
            Aceasta functie modifica numele unui client 
        """
        for i in range(0,len(self.__lista_clienti)):
            if self.__lista_clienti[i].getId_client() == id_client:
                self.__lista_clienti[i].setNume(nume_client)
                return 

    def cauta_client_id_gasit(self,id):
        """
            Aceasta functie are rolul de a verifica daca un client exista sau nu in lista, avand un id dat,
            in cazul in care se gaseste, clientul este returnat sub forma de string, iar in cazul celalalt 
            este ridicata o exceptie prin care utilizatorul este anuntat ca nu exista un client cu id-ul dat

            Tototdata este verificat daca lista de clienti este vida sau nu
        """

        if len(self.__lista_clienti) == 0:
            raise Exception_Repository_Clienti("Lista de clienti este goala!")

        #valoare = self.cauta_client(id)
        l = self.afisare_clienti()
        valoare = self.cauta_client_recursiv(id,l)

        if valoare != None:
            return valoare
        else:
            raise Exception_Repository_Clienti("Nu a fost gasit un client cu id-ul dat!")
    
    def cauta_client_id_modifica(self,id,nume):
        """
            Rolul functiei este de a cauta si modifica daca exista un client cu id-ul primit in lista, in caz afirmativ
            numele clientului este modificat cu cel primit, iar in cazul in care nu exista, este ridicata o eroare ce are 
            rolul de a-l informa pe utilizatoru ca nu exista clientul pe care vrea sa-l modifice

            Tototdata este verificat daca lista de clienti este vida sau nu
        """

        if len(self.__lista_clienti) == 0:
            raise Exception_Repository_Clienti("Lista de clienti este goala!")
    
        #valoare = self.cauta_client(id)
        l = self.afisare_clienti()
        valoare = self.cauta_client_recursiv(id,l)
        
        if valoare != None:
            self.modifica_client_nume(id,nume)
        else:
            raise Exception_Repository_Clienti("Nu exista clientul cautat!")
    
    def returneaza_obiect_client(self,id):
        """
            Aceasta returneaza obiectul de tip client cu id-ul primit
        """

        for i in self.__lista_clienti:

            if i.getId_client() == id:
                return i

class Extended_repository_clienti(Repository_clienti):
    """
        Clasa ce este realizata prin mostenire si are rolul de a adauga optiunea de a lua date din fisier, scrie date din fisier si de a modifica date din fisier
    """

    def __init__(self, file):
        """
            Aceasta metoda initializeaza lista de clienti si stocheaza in ea clientii ce se afla in fisier
        """

        self.__file = file
        Repository_clienti.__init__(self)
        self.__load_from_file()
    
    def __load_from_file(self):
        """
            Rolul acestei metode este de a converti un sir de stringuri intr-un client, datele acestuia fiind stocate intr-un fisier
        """

        try:
            f = open(self.__file,"r")
        except IOError:
            return
        line = f.readline().strip()
        while line != "":
            valori = line.split(",")
            c = Client(int(valori[0]),valori[1],int(valori[2]))
            Repository_clienti.salveaza_client(self,c)
            line = f.readline().strip()
        f.close()
    
    def __write_to_file(self):
        """
            Aceasta metoda se ocupa cu scrierea in fisier, in cazul in care apare vreo modificare/adaugare/sterere din lista aceasta functie este apelata
        """

        try:
            lista = self.afisare_clienti()
        except Exception_Repository_Clienti:
            lista = []
        f = open(self.__file,"w")
        if len(lista) > 0:
            for cl in lista:
                client = str(cl.getId_client()) + "," + cl.getNume() + "," + str(cl.getCnp()) + "\n"
                f.write(client)
        else:
            f.write("")
        f.close()
    
    def salveaza_client(self,c):
        """
            Metoda salveaza_client se ocupa cu apelarea functiei din clasa mama pentru salvarea unui client, dupa care se ocupa cu actualizarea fisierului
        """

        super().salveaza_client(c)
        self.__write_to_file()
    
    def sterge_client_id(self,id):
        """
            Aceasta functie se ocupa cu apelarea functiei mostenite din clasa mama si cu actualizarea listei de clienti in cazul in care este sters un client
        """

        super().sterge_client_id(id)
        self.__write_to_file()

    def modifica_client_nume(self,id,nume):
        """
            Metoda scrisa are rolul de a apela functia de modificare din clasa mama si de a actualiza fisierul in cazul in care apare vreo modificare in lista
        """
        
        super().modifica_client_nume(id,nume)
        self.__write_to_file()

class RepoNouClienti:

    def __init__(self,fisier):

        self.file_name = fisier
    
    def verifica_id_daca_exista(self,id):

        file = open(self.file_name,"r")

        for line in file:

            if line.strip() == "":
                continue
            else:
                linie = line.strip()
                date = linie.split(",")
                if int(date[0]) == id:
                    file.close()
                    return True

        file.close()
        return False 

    def salveaza_client(self,c):

        if self.verifica_id_daca_exista(c.getId_client()) == False:
            file = open(self.file_name,"a")
            file.write(str(c.getId_client()))
            file.write(",")
            file.write(c.getNume())
            file.write(",")
            file.write(str(c.getCnp()))
            file.write("\n")
            file.close()
        
        else:

            raise Exception_Repository_Clienti("Exista un client cu acest id!")

    def cauta_client_id_modifica(self,id,nume): 

        if self.verifica_id_daca_exista(id) == True:
            file = open(self.file_name,"r")
            aux = open("aux.txt","w")
            aux.write("")
            aux.close()
            aux = open("aux.txt","a")

            for line in file:

                if line.strip() == "":
                    continue
                else:
                    linie = line.strip()
                    date = linie.split(",")
                    if int(date[0]) == id:
                        date[1] = nume
                    c = str(str(date[0]) + "," + str(date[1]) + "," + str(date[2]) + "\n")
                    aux.write(c)

            aux.close()
            aux = open("aux.txt","r")
            file.close()
            file = open(self.file_name,"w")
            file.write("")
            file.close()
            file = open(self.file_name,"a")

            for line in aux:

                if line.strip() == "":
                    continue
                else:
                    linie = line.strip()
                    date = linie.split(",")
                    c = str(str(date[0]) + "," + str(date[1]) + "," + str(date[2]) + "\n")
                    file.write(c)
            
            file.close()
            aux.close()
        
        else:

            raise Exception_Repository_Clienti("Nu exista un client cu id-ul dat!")

    def afisare_clienti(self):

        file = open(self.file_name,"r")

        lista = []

        for line in file:

            if line.strip() == "":
                continue
            else:
                linie = line.strip()
                date = linie.split(",")
                c = Client(int(date[0]),date[1],int(date[2]))
                lista.append(c)
        
        file.close()
        return lista
                
    def cauta_client_id_gasit(self,id):

        if self.verifica_id_daca_exista(id) == True:
            file = open(self.file_name,"r")

            for line in file:

                if line.strip() == "":
                    continue
                else:
                    linie = line.strip()
                    date = linie.split(",")
                    c = Client(int(date[0]),date[1],int(date[2]))
                    if c.getId_client() == id:
                        rez = c
            
            file.close()
            return rez
        
        else:

            raise Exception_Repository_Clienti("Nu exista un client cu id-ul dat!")

    def sterge_client_id(self,id):

        if self.verifica_id_daca_exista(id) == True:
            file = open(self.file_name,"r")

            aux = open("aux.txt","w")
            aux.write("")
            aux.close()
            aux = open("aux.txt","a")

            for line in file:

                if line.strip() == "":
                    continue
                else:
                    linie = line.strip()
                    date = linie.split(",")
                    if int(date[0]) != id:
                        c = str(str(date[0]) + "," + str(date[1]) + "," + str(date[2]) + "\n")
                        aux.write(c)
            
            aux.close()
            aux = open("aux.txt","r")
            file.close()
            file = open(self.file_name,"w")
            file.write("")
            file.close()
            file = open(self.file_name,"a")

            for line in aux:

                if line.strip() == "":
                    continue
                else:
                    linie = line.strip()
                    date = linie.split(",")
                    c = str(str(date[0])+","+str(date[1])+","+str(date[2])+'\n')
                    file.write(c)
            
            file.close()
            aux.close()

        else:

            raise Exception_Repository_Clienti("Nu exista un client cu id-ul dat!")  

def Teste_repository_clienti(): # de schimbat putin la teste

    test = Repository_clienti()
    
    # test pentru salveaza
    c = Client(1,"Mihai Eminescu", 1234567891234)
    test.salveaza_client(c)
    assert(len(test)==1) == True

    # test pentru functia finala cauta client dupa id
    assert(test.cauta_client(0)) == None
    assert(test.cauta_client(1)) == "Id: 1, Nume: Mihai Eminescu, CNP: 1234567891234"

    # test pentru stergere client dupa id
    test.sterge_client_id(1)
    assert(len(test)) == 0

    # test pentru functia finala modifica client nume
    c = Client(1,"Mihai Eminescu", 1234567891234)
    test.salveaza_client(c)
    assert(len(test)==1) == True
    test.modifica_client_nume(1,"Mihai Dumitru")
    assert(test.cauta_client(1)) == "Id: 1, Nume: Mihai Dumitru, CNP: 1234567891234"

    # test pentru functia cauta
    assert(test.cauta_client_id_gasit(1)) == "Id: 1, Nume: Mihai Dumitru, CNP: 1234567891234"
    c = Client(2,"Mihai Eminescu", 1234567891234)
    test.salveaza_client(c)
    assert(test.cauta_client_id_gasit(2)) == "Id: 2, Nume: Mihai Eminescu, CNP: 1234567891234"

    # test pentru functia cauta_recursiv
    l = test.afisare_clienti()
    assert(test.cauta_client_recursiv(1,l) == "Id: 1, Nume: Mihai Dumitru, CNP: 1234567891234")
    assert(test.cauta_client_recursiv(2,l) == "Id: 2, Nume: Mihai Eminescu, CNP: 1234567891234")
    assert(test.cauta_client_recursiv(200,l) == None)

Teste_repository_clienti()


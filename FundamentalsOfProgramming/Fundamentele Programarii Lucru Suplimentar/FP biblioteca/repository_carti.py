"""
    Acest modul se ocupa cu retinerea a 2 clase:
        - RepositoryException - ce retine erorile ce pot aparea la nivelul repository-ului
        - Repository - ce retine toate metodele aferente listei de carti
"""

from domain import Carte
from lista_globala import lista_undo
import copy

class RepositoryException(Exception):
    """
        Clasa ce se ocupa cu stocarea de erori ce pot aparea la nivelul repository-ului
    """

    pass

class Repository:
    """
        Clasa ce retine toate metodele aferente listei de carti
    """

    def __init__(self,file_name):
        """
            Cu ajutorul acestei metode realizam initializarea listei de carti din fisier
        """

        self.__file = file_name
        self.__lista = []
        self.read_from_file()
    
    def read_from_file(self):
        """
            Aceasta este metoda ce transforma datele din fisier in obiecte de tip carte si le stocheaza intr-o lista
        """

        try:
            f = open(self.__file,"r")
        except IOError:
            pass
            
        line = f.readline().strip()
        while line != "":

            line = line.split("; ")
            c = Carte(int(line[0]),line[1],line[2],int(line[3]))
            self.__lista.append(c)
            line = f.readline().strip()
        
        f.close()
    
    def getAll(self):
        """
            Metoda ce returneaza lista de carti
        """

        return self.__lista

    def write_to_file(self):
        """
            Metoda ce scrie in fisier elementele din lista
        """

        try:
            f = open(self.__file,"w")
        except IOError:
            pass

        l = self.getAll()
        for elem in l:

            f.write(str(elem.getId()) + "; " + elem.getTitlu() + "; " + elem.getAutor() + "; " + str(elem.getAn_aparitie()) + "\n")
        
        f.close()

    def cauta_id(self,id):
        """
            Metoda ce returneaza adevarat sau fals daca nu exista sau exista o carte cu id-ul primit
        """

        l = self.getAll()
        for elem in l:

            if elem.getId() == id:

                return True
            
        return False

    def adaugare_carte(self,c):
        """
            Metoda ce realizeaza adaugare unei carti in lsita de carti
        """

        if self.cauta_id(c.getId()) == True:

            raise RepositoryException("Exista deja o carte cu id-ul dat!")
        
        lista_undo.append(list(self.__lista))

        self.__lista.append(c)

        self.write_to_file()
    
    def id_contine_cifra(self,id,cifra):
        """
            Functie ce verifica daca un id contine o anumita cifra
        """

        if id == cifra:

            return True
        
        while id != 0:

            cifra_id = id % 10

            if cifra_id == cifra:
                return True

            id //= 10
        
        return False
    
    def modifica_carti(self,cifra,autor):
        """
            Rolul acestei metode este de a modifica autorul cartilor ce contin in id o anumita cifra
        """

        caz_particular = 0

        l = copy.deepcopy(self.__lista)

        lista_undo.append(l)

        for i in range (0,len(self.__lista)):

            if self.id_contine_cifra(self.__lista[i].getId(),cifra) == True:

                caz_particular = 1
                self.__lista[i].setAutor(autor)
        
        if caz_particular == 0:

            lista_undo.pop()
            raise RepositoryException("Cifra nu apare in niciun id!")
            
        self.write_to_file()
    
    def undo(self):
        """
            Functia undo ce realizeaza intoarcerea la lista precedenta inainte de a suferii modificari adica
        """

        if len(lista_undo) == 0:

            raise RepositoryException("Nu au fost realizate modificari asupra listei!")

        self.__lista = []

        for i in lista_undo[len(lista_undo)-1]:

            self.__lista.append(i)

        lista_undo.pop()

        self.write_to_file()

def teste_repo():

    try:
       f = open("biblioteca_test.txt","w")
    except IOError:
        return
    f.write("1; Harap Alb; dadaaa; 1974\n2; Carte; Autor; 2012\n3; Mov; Hautor; 2013\n10; da; dadaaa; 10\n")
    f.close()
    
    repo = Repository("biblioteca_test.txt")

    l = repo.getAll()
    assert len(l) == 4

    try:
        repo.undo()
        assert False
    except RepositoryException:
        assert True

    assert repo.cauta_id(200) == False
    assert repo.cauta_id(1) == True

    try:
        repo.adaugare_carte(Carte(1,"a","a",1))
        assert False
    except RepositoryException:
        assert True
    
    repo.adaugare_carte(Carte(111,"b","b",111))
    l = repo.getAll()
    assert len(l) == 5

    repo.undo()
    l = repo.getAll()
    assert len(l) == 4

    assert repo.id_contine_cifra(0,0) == True
    assert repo.id_contine_cifra(999,1) == False

    repo.modifica_carti(1,"mers")
    l = repo.getAll()
    assert l[0].getAutor() == "mers"

    try:
        repo.modifica_carti(9,"dadada")
        assert False
    except RepositoryException:
        assert True

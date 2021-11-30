"""
    Acest modul are rolul de a retine 2 clase:
        - RepoException - ce se ocupa cu stocarea erorilor ce pot aparea la nivelul repository-ului
        - Magazin - ce se ocupa cu retinerea obiectelor de tip Produs si cu metodele ce pot aparea la nivelul listei
"""

from domain.domain_magazin import Produs
from lista_undo import lista_undo
import copy

class RepoException(Exception):
    """
        Rolul acestei clase este de a retine erorile ce pot aparea la niveul repository-ului
    """

    pass

class Magazin:
    """
        Clasa magazin se ocupa cu initializarea listei de produse si cu retinerea metodelor aferente acesteia
    """

    def __init__(self,file_name):
        """
            Metoda init initializeaza lista de produse ca fiind vida, retine intr-o variabila numele fisierului din care citeste date si scrie si apeleaza read from file
        """

        self.__lista = []
        self.__file_name = file_name
        self.read_from_file()
    
    def read_from_file(self):
        """
            Aceasta metoda cum ii spune si numele, are rolul de a transforma si adauga in lista datele citite din fisier
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            return
        
        line = f.readline().strip()
        while line != "":

            line = line.split(" ")
            p = Produs(int(line[0]),line[1],float(line[2]))
            self.__lista.append(p)
            line = f.readline().strip()
        
        f.close()

    def getAll(self):
        """
            Rolul acestei metode este de a returna lista de obiecte de tipul Produs
        """

        return self.__lista

    def write_to_file(self):
        """
            Metoda aceasta cum ii spune si numele are rolul de a scrie in fisier obiectele de tipul produs sub un anumit format, pentru a putea fi recitite ulterior, astfel creeandu-se o mini baza
            de date
        """

        try:
            f = open(self.__file_name,"w")
        except IOError:
            return
        
        l = self.getAll()
        for produs in l:

            f.write(str(produs.getId()) + " " + produs.getDenumire() + " " + str(produs.getPret()) + "\n")
        
        f.close()
    
    def cauta_id(self,id_cautat):
        """
            Aceasta metoda returneaza True sau False daca id-ul trimis ca si parametru apare sau nu in lista de produse
        """

        l = self.getAll()
        for produs in l:

            if produs.getId() == id_cautat:
                return True
        
        return False
    
    def adauga_produs(self,p):
        """
            Menirea acestei metode este de a adauga un produs in lista dupa ce aceste este validat in service si verificat daca are id unic
        """

        if self.cauta_id(p.getId()) == True:

            raise RepoException("Mai exista un produs cu acest id!")
        
        l = copy.deepcopy(self.__lista)
        lista_undo.append(l)

        self.__lista.append(p)
        self.write_to_file() 
    
    def verifica_cifra_in_id(self,id,cifra):
        """
            Rolul acestei functii este de a verifica daca un id contine o anumita cifra, ambii operanzi fiind trimisi ca si parametru
        """

        if cifra == id:

            return True
        
        while id != 0:

            cif = id % 10
            if cif == cifra:
                return True
            id = id // 10

        return False

    def sterge_produse(self,cifra):
        """
            Scopul acestei metode este de a sterge produsele ce contin in id-ul lor o anumita cifra 
        """

        numar_produse = 0

        l = copy.deepcopy(self.__lista)

        lista_undo.append(l)

        for i in range(len(self.__lista)-1,-1,-1):

            if self.verifica_cifra_in_id(self.__lista[i].getId(),cifra) == True:

                self.__lista.pop(i)
                numar_produse += 1
        
        if numar_produse == 0:

            lista_undo.pop()
            raise RepoException("Nu au fost gasite produse cu id-ul ce sa contina cifra introdusa!")
        
        self.write_to_file()
        return numar_produse
    
    def undo(self):
        """
            Functia undo reface ultima operatie efectuata in cazul in care lista a suferit modificari, daca aceasta nu a suferit o sa se afiseze un mesaj corespunzator
        """

        if len(lista_undo) == 0:

            raise RepoException("Nu au fost realizate modificari asupra listei de produse!")

        self.__lista = lista_undo[-1]
        lista_undo.pop()
        self.write_to_file()
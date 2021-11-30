"""
    Modulul repositorylab.py se ocoupa cu retinerea a 2 clase, una ce stocheaza erorile ce pot aparea la nivelul repository-ului si alta ce se ocupa cu metodele ce au loc asupra
    listei de laboratoare
"""

from domain.lab import Lab

class LabRepositoryException(Exception):
    """
        Cu ajutorul acestei clase sunt stocate erorile ce pot aparea la nivelul Lab Repository
    """

    pass

class LabRepository:
    """
        Aceasta clasa retine lista de laboratoare si metodele aferente acesteia
    """

    def __init__(self,file_name):
        """
            Rolul acestei metode este de a initializa lista de laboratoare, de a citii din fisier si stoca intr o lista, laboratoarele ce se afla in fisierul labs.txt
        """

        self.__lista_laboratoare = []
        self.__file_name = file_name
        self.read_from_file()
    
    def read_from_file(self):
        """
            Aceasta este metoda efectiva ce realizeaza citirea datelor din fisier, convertirea acestora in obiecte si stocarea intr o lista
        """
    
        try:
            f = open(self.__file_name,"r")
        except IOError:
            pass

        line = f.readline().strip()
        
        while line != "":

            line = line.split(", ")
            l = Lab(int(line[0]),int(line[1]),line[2])
            self.__lista_laboratoare.append(l)
            line = f.readline().strip()
        
        f.close()
    
    def write_to_file(self):
        """
            Aceasta metoda se ocupa cu actualizarea fisierului de fiecare data cand lista de laboratoare este modificata
        """

        try:
            f = open(self.__file_name,"w")
        except IOError:
            pass
            
        l = self.getAll()

        for elem in l:

            f.write(str(elem.getIdStudent()) + ", " + str(elem.getLabNr()) + ", " + str(elem.getProblemNr()) + "\n")
        
        f.close()

    def getAll(self):
        """
            Rolul acestei metode este de a returna lista de laboratoare
        """

        return self.__lista_laboratoare
    
    def cauta_nr_lab(self,nr,nr_pr):
        """
            Metoda verifica daca mai exista laboratorul respectiv si daca are aceeasi problema asignata
            in caz afirmativ returneaza True, altfel False
        """

        l = self.getAll()

        for lab in l:

            if lab.getLabNr() == nr and lab.getProblemNr() != nr_pr:

                return False
        
        return True

    def add(self,lab):
        """
            Cu ajutorul acestei metode ii asignam unui student un laborator
        """ 

        if self.cauta_nr_lab(lab.getLabNr(),lab.getProblemNr()) == True:

            self.__lista_laboratoare.append(lab)

            self.write_to_file()
        
        else:

            raise LabRepositoryException("Acest laborator are deja asignata o problema!")
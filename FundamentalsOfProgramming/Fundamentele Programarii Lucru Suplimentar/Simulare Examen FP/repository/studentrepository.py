"""
    Modulul studentrepository.py se ocoupa cu retinerea a 2 clase, una ce stocheaza erorile ce pot aparea la nivelul repository-ului si alta ce se ocupa cu metodele ce au loc asupra
    listei de studenti
"""

from domain.student import Student

class StudentRepository:
    """
        Aceasta clasa retine lista de studenti si metodele aferente acesteia
    """

    def __init__(self,file_name):
        """
            Rolul acestei metode este de a initializa lista de studenti, de a citii din fisier si stoca intr o lista, studentii ce se afla in fisierul student.txt
        """

        self.__lista_studenti = []
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
            s = Student(int(line[0]),line[1])
            self.__lista_studenti.append(s)
            line = f.readline().strip()
        
        f.close()
    
    def findById(self,id):
        """
            Aceasta metoda cauta un student dupa id, daca il gaseste returneaza studentul, atlfel None
        """

        l = self.getAll()

        for st in l:

            if st.getId() == id:

                return st
        
        return None

    def getAll(self):
        """
            Rolul acestei metode este de a returna lista de studenti
        """

        return self.__lista_studenti
    
    def id_to_obj_st(self,id):
        """
            Aceasta metoda are rolul de a returna studentul corespunzator unui id primit
        """

        l = self.getAll()

        for st in l:

            if st.getId() == id:

                return st

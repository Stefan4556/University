""" 
    Rolul acestui modul este de a retine 2 clase, uan ce retine rorile ce pot aparea la nivelul repository-ului si una ce se ocupa cu retinerea metodelor aferente listei de biciclete
"""

from domain.domain import Bicicleta

class RepositoryException(Exception):
    """
        Aceasta este clasa ce retine erorile ce pot aparea la nivelul repository-ului
    """
    
    pass

class Repository:
    """
        Clasa repository se ocupa cu retinerea listei de biciclete si cu metodele aferente acesteia 
    """

    def __init__(self,file_name):
        """
            In aceasta metoda initializam lista de biciclete incarcand mai multe date dintr un fisier
        """

        self.__file_name = file_name
        self.__lista_biciclete = []
        self.read_from_file()
    
    def read_from_file(self):
        """
            Cu ajutorul acestei metode transformam datele intr un obiect de tip bicicleta dupa care l adaugam la lista
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            pass
            
        line = f.readline().strip()
        while line != "":

            line = line.split(", ")
            b = Bicicleta(int(line[0]),line[1],float(line[2]))
            self.__lista_biciclete.append(b)
            line = f.readline().strip()
        
        f.close()
    
    def getAll(self):
        """
            Rolul acestei metode este de a returna lista de biciclete
        """

        return self.__lista_biciclete

    def write_to_file(self):
        """
            Rolul acestei metode este de a actualzia fisierul in momentul in care lista de biciclete sufera modificari
        """

        try:
            f = open(self.__file_name,"w")
        except IOError:
            pass

        l = self.getAll()

        for bic in l:

            f.write(str(bic.getId()) + ", " + bic.getTip() + ", " + str(bic.getPret()) + "\n")
        
        f.close()
    
    def cauta_id(self,id):
        """
            Rolul acestei metode este de a cauta dupa id un obiect si de a ii returna pozitia acestuia
        """

        l = self.getAll()
        for i in range(0,len(l)):

            if l[i].getId() == id:

                return i

    def delete(self,id):
        """
            Rolul acestei functii este de a sterge un obiect dupa id si de a actualiza atat lista cat si fisierul
        """

        indice = self.cauta_id(id)

        self.__lista_biciclete.pop(indice)

        self.write_to_file()
    
    def pret_maxim(self):
        """
            Cu ajutorul acestei metode determinam pretul maxim din fisier
        """

        l =self.getAll()

        if len(l) == 0:

            raise RepositoryException("Lista de bicicelte este goala!")

        maxim = 0

        for bic in l:

            if bic.getPret() > maxim:

                maxim = bic.getPret()
        
        return maxim
    
    def sterge_biciclete_pret_maxim(self):
        """
            Rolul acestei metode este de a sterge toate bicicletele ce au pretul egal cu pretul maxim
        """

        pret_max = self.pret_maxim()

        for i in range(len(self.__lista_biciclete)-1,-1,-1):

            if self.__lista_biciclete[i].getPret() == pret_max:

                self.__lista_biciclete.pop(i)

        self.write_to_file()
    
    def sterge_tip(self,tip):
        """
            Cu ajutorul acestei metode stergem toate bicicletele care sunt de un anumit tip introdus de catre utilizator
        """

        ok = 0

        for bic in reversed(self.__lista_biciclete):

            if bic.getTip() == tip:

                ok = 1
                self.delete(bic.getId())

        if ok == 0:

            raise RepositoryException("Nu au fost gasite biciclete de acest tip!")
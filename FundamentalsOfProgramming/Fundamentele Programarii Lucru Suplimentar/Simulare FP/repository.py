"""
    Rolul acestui modul este de a retine, citi din fisier si a returna lista de obiecte
"""

from Domain.domain import Destinatie

class Repository:
    """
        Aceasta este clasa ce se ocupa cu gestiunea listei de obiecte de tipul Destinatie
    """

    def __init__(self,file_name):
        """
            Cu ajutorul acestei metode initializam lista de obiecte
        """

        self.__file_name = file_name
        self.__lista = []
        self.read_from_file()
    
    def read_from_file(self):
        """
            Rolul acestei metode este de a citi din fisier obiectele de tipul destinatie si de a le adauga la lista
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            pass

        line = f.readline().strip()
        while line != "":

            line = line.split(",")
            d = Destinatie(int(line[0]),line[1],line[2],int(line[3]))
            self.__lista.append(d)
            line = f.readline().strip()
        
        f.close()
    
    def getAll(self):
        """
            Cu ajutorul acestei metode returnam lista de obiecte
        """

        return self.__lista
    
def teste_repository():

    try:
        f = open("simulareFPteste.txt","w")
    except IOError:
        pass
    f.write("31,Hawaii,soare scump clasic,1200\n2,Sinaia,frig ieftin clasic,300\n")
    f.close()
    repo = Repository("simulareFPteste.txt")
    l = repo.getAll()
    assert len(l) == 2
    assert l[0].getId() == 31
    try:
        f = open("simulareFPteste.txt","w")
    except IOError:
        pass
    f.write("31,Bucuresti,soare scump clasic,1200\n2,Sinaia,frig ieftin clasic,300\n3,Haidee,merge bine totul,123123")
    f.close()
    repo = Repository("simulareFPteste.txt")
    l = repo.getAll()
    assert len(l) == 3
    assert l[0].getId() == 31

teste_repository()
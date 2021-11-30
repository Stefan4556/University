from domain import Vacanta

class Repo_vacante:
    """
        Aceasta clasa are scopul de a retine toate vacantele si metodele aferente listei acestora
    """

    def __init__(self,file_name):
        """
            Initializam cu ajutorul acestei metode, lista ca fiind vida initial, dupa care incarcam obiectele de tip vacanta din fisier
        """

        self.__lista = []
        self.__file_name = file_name
        self.__load_from_file()
    
    def __load_from_file(self):
        """
            Cu ajutorul acestei metode incarcam din fisier string-uri ce le convertim ulterior in obiecte de tip vacanta si le adaugam intr-o lista mare
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            return
        
        line = f.readline().strip()

        while line != "":

            line = line.split(",")
            v = Vacanta(int(line[0]),line[1],line[2],int(line[3]))
            self.__lista.append(v)
            line = f.readline().strip()
        
        f.close()
    
    def getAll(self):
        """
            Rolul acestei metode este de a returna lista de obiecte de tip vacanta
        """

        return self.__lista
    
def teste_repo():

    f = open("vacante_test.txt","w")
    f.write("")
    f.close()

    f = open("vacante_test.txt","w")
    f.write("31,Hawaii,soare scump clasic,1200\n2,Sinaia,frig ieftin clasic,300\n1,Straja,frig scump,800\n")
    f.close()

    repo = Repo_vacante("vacante_test.txt")

    l = repo.getAll()
    assert len(l) == 3

    assert str(l[0]) == "31,Hawaii,soare scump clasic,1200"

teste_repo()
    

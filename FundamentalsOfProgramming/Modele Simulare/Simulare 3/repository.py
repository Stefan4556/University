from domain import Arta

class Repo_arta():
    """
        Clasa ce se ocupa cu incarcarea din fisier si stocarea intr-o lista a artelor
    """

    def __init__(self,file_name):
        """
            Metoda ce se ocupa cu initializarea repository-ului de arte
        """

        self.__lista = []
        self.__file_name = file_name
        self.__load_from_file()
    
    def getAll(self):
        """
            Metoda se ocupa cu returnarea listei de arte
        """

        return self.__lista
    
    def __load_from_file(self):
        """
            Aceasta metoda are rolul de a incarca din fisier artele
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            return

        line = f.readline().strip()

        while line != "":

            line = line.split(",")
            a = Arta(int(line[0]),line[1],line[2],int(line[3]))
            self.__lista.append(a)
            line = f.readline().strip()
        
        f.close()
    
    def cauta_camera(self,camera):
        """
            Cu ajutorul acestei metode verificam daca exista sau nu o camera cu numarul introdus de catre utilizator
        """

        for i in self.__lista:

            if i.getNrCamera() == camera:

                return True
        
        return False

def teste_repo():

    repo = Repo_arta("test3.txt")
    f = open("test3.txt","w")
    f.write("")
    f.close()
    
    f = open("test3.txt","w")
    f.write("1,Peisaj cu case de tara,Stefan Luchian,13 \n2,Giverny; casa artistului,Claude Monet,13 \n3,Impersie. Rasarit de soare,Claude Monet,13 \n")
    f.close()
    repo = Repo_arta("test3.txt")
    assert len(repo.getAll()) == 3
    l = repo.getAll()
    assert str(l[0]) == "1,Peisaj cu case de tara,Stefan Luchian,13"

    assert repo.cauta_camera(13) == True
    assert repo.cauta_camera(20) == False

teste_repo()
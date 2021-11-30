from domain import Spa

class Repo_spa:
    """
        Clasa ce se ocupa cu retinerea lsitei de servicii ale unui spa si metodele aferente acesteia
    """

    def __init__(self,file_name):
        """
            Aceasta metoda se ocupa cu initializarea listei de servicii si cu incarcarea acestora din fisier intr-o lista
        """

        self.__file_name = file_name
        self.__lista = []
        self.__load_from_file()
    
    def __load_from_file(self):
        """
            Metoda ce incarca din fisier in lista obiectele de tip Spa
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            return
        
        line = f.readline().strip()
        while line != "":

            line = line.split(",")
            s = Spa(int(line[0]),line[1],line[2],int(line[3]))
            self.__lista.append(s)
            line = f.readline().strip()

        f.close()
    
    def getAll(self):
        """
            Metoda ce returneaza intreaga lista de obiecte de tip spa
        """

        return self.__lista
    
    def cauta_abonament(self,abonament):
        """
            Aceasta metoda are rolul de a cauta un abonament, iar in cazul in care exista este returnat True, altfel False
        """

        l = self.getAll()
        
        for i in l:

            tipuri = i.getSirTipuriAbonamente().split(" ")

            if abonament in tipuri:

                return True
        
        return False

def teste_repo():

    f = open("test4.txt","w")
    f.write("")
    repo = Repo_spa("test4.txt")
    assert len(repo.getAll()) == 0

    f = open("test4.txt","w")
    f.write("1,Jacuzzi,basic silver gold,30\n2,Masaj,classic gold,100\n3,Sauna,premium gold,150")
    f.close()
    repo = Repo_spa("test4.txt")

    assert len(repo.getAll()) == 3
    l = repo.getAll()
    assert str(l[0]) == "1,Jacuzzi,basic silver gold,30"

    assert repo.cauta_abonament("ic") == False
    assert repo.cauta_abonament("gold") == True
    assert repo.cauta_abonament("classic") == True

teste_repo()
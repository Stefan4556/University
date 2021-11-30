from domain import Melodie

class Repo_muzica:
    """
        Clasa ce se ocupa cu retinerea listei melodiilor, incarcarea acestora din fisier si a altor metode aferente
    """

    def __init__(self,file_name):
        """
            Aceasta metoda initializeaza lista de melodii
        """

        self.__file_name = file_name
        self.__lista = []
        self.__load_from_file()
    
    def __load_from_file(self):
        """
            Rolul acestei metode este de a incarca din fisier toate melodiile
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            return
        
        line = f.readline().strip()

        while line != "":
            line = line.split(",")
            m = Melodie(int(line[0]),line[1],line[2],line[3])
            self.__lista.append(m)
            line = f.readline().strip()
        
        f.close()
    
    def getAll(self):
        """
            Metoda returneaza lista de melodii
        """

        return self.__lista
    
    def cauta_id(self,id):
        """
            Aceasta metoda returneaza True daca exista id-ul primit in lista sau false daca nu exista
        """

        for i in self.__lista:

            if i.getId() == id:

                return True
        
        return False
    
    def returneaza_gen_corespunzator_id(self,id):
        """
            Aceasta metoda returneaza genul corespunzator unui id primit 
        """

        for i in self.__lista:

            if i.getId() == id:

                return i.getGen()

def teste_repo():

    f = open("test5.txt","w")
    f.write("")
    f.close()

    f = open("test5.txt","w")
    f.write("1,Enter Sandman,Metallica,Rock\n2,Tango to Evora,Loreena McKennit,Tango\n3,Aerials,System of a Down,Rock\n")
    f.close()

    repo = Repo_muzica("test5.txt")
    l = repo.getAll()
    assert len(l) == 3

    assert repo.cauta_id(1) == True
    assert repo.cauta_id(20) == False

    assert repo.returneaza_gen_corespunzator_id(1) == "Rock"
    assert repo.returneaza_gen_corespunzator_id(2) == "Tango"
    assert repo.returneaza_gen_corespunzator_id(20) == None

teste_repo()
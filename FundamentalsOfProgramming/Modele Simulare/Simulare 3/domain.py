class Arta():
    """
        Clasa ce se ocupa cu initializarea obiectelor de tip arta
    """

    def __init__(self,id,denumire,autor,nr_camera):
        """
            Cu ajutorul acestei metode initializam cele 4 campuri ale unui obiect de tip Arta
        """

        self.__id = id
        self.__denumire = denumire
        self.__autor = autor
        self.__nr_camera = nr_camera
    
    def getId(self):
        """
            Metoda ce returneaza id-ul unei arte
        """

        return self.__id
    
    def getDenumire(self):
        """
            Metoda ce returneaza denumirea unei arte
        """

        return self.__denumire

    def getAutor(self):
        """
            Metoda ce returneaza autorul unei arte
        """

        return self.__autor
    
    def getNrCamera(self):
        """
            Metoda ce returneaza nr camerei unei arte
        """

        return self.__nr_camera
    
    def __str__(self):
        """
            Metoda ce returneaza obiectul de tip arta sub forma de string
        """

        return str(str(self.getId())+","+self.getDenumire()+","+self.getAutor()+","+str(self.getNrCamera()))

class Validator_arta_exception(Exception):
    """
        Clasa ce se ocupa cu retinerea exceptiilor
    """

    pass

class Validator_arta():
    """
        Clasa ce se ocupa cu validarea obiectelor de tip arta
    """

    def valideaza_arta(self,a):

        if a.getNrCamera() < 0:

            raise Validator_arta_exception("Numarul camerei nu poate sa fie negativ!")

def teste_domain():

    a = Arta(1,"Test","Python P",13)
    assert a.getId() == 1
    assert a.getDenumire() == "Test"
    assert a.getAutor() == "Python P"
    assert a. getNrCamera() == 13
    assert str(a) == "1,Test,Python P,13"

    val = Validator_arta()

    a = Arta(1,"Test","Python P",13)

    try:
        val.valideaza_arta(a)
        assert True
    except Validator_arta_exception:
        assert False

    a = Arta(1,"Test","Python P",-13)

    try:
        val.valideaza_arta(a)
        assert False
    except Validator_arta_exception:
        assert True

teste_domain()
"""
    Acest modul se ocupa cu retinerea a 3 clase:
        - clasa Carte - ce creeaza obiectele de acest tip
        - ValidatorCarteException - ce stocheaza erorile ce pot aparea la nivelul validarii
        - ValidatorCarte - valideaza obiectele de tip carte
"""

class Carte:
    """
        Aceasta clasa se ocupa cu initializarea obiectelor de tip Carte
    """

    def __init__(self,id,titlu,autor,an_aparitie):
        """
            Metoda ce se ocupa cu initializarea campurilor unui obiect
        """

        self.__id = id
        self.__titlu = titlu
        self.__autor = autor
        self.__an_aparitie = an_aparitie
    
    def getId(self):
        """
            Aceasta metoda returneaza id ul unei carti
        """

        return self.__id
    
    def getTitlu(self):
        """
            Aceasta metoda returneaza titlul unei carti
        """

        return self.__titlu
    
    def getAutor(self):
        """
            Aceasta metoda returneaza autorul unei carti
        """

        return self.__autor
    
    def getAn_aparitie(self):
        """
            Aceasta metoda returneaza anul de aparitie al unei carti
        """

        return self.__an_aparitie
    
    def setAutor(self,autor_nou):
        """
            Aceasta metoda schimba autorul unei carti
        """

        self.__autor = autor_nou
    
    def __str__(self):
        """
            Aceasta metoda returneaza un obiect sub forma de string
        """

        return str("Id: " + str(self.__id) + " Titlu: " + self.__titlu + " Autor: " + self.__autor + " An aparitie: " + str(self.__an_aparitie))

class ValidatorCarteException(Exception):
    """
        Clasa ce se ocupa cu retinerea erorilor ce pot aparea la nivelul validatorului
    """

    pass

class ValdiatorCarte:
    """
        Clasa ce se ocupa cu retinerea metodei ce valideaza un obiect de tip carte
    """

    def validate(self,c):
        """
            Metoda ce valideaza efectiv un obiect
        """

        erori = ""

        if c.getId() <= 0:

            erori += "Id-ul nu poate sa fie un numar mai mic sau egal decat 0!"
        
        if c.getTitlu() == "":

            erori += "Titlul nu poate sa fie vid!"
        
        if c.getAutor() == "":

            erori += "Autorul nu poate sa fie vid!"
        
        if c.getAn_aparitie() <= 0:

            erori += "Anul nu poate sa fie mai mic sau egal decat 0!"
        
        if erori != "":

            raise ValidatorCarteException(erori)

def teste_domain():

    c = Carte(1,"a","a",1)
    assert c.getId() == 1
    assert c.getTitlu() == "a"
    assert c.getAutor() == "a"
    assert c.getAn_aparitie() == 1
    c.setAutor("b")
    assert c.getAutor() == "b"

    val = ValdiatorCarte()
    c = Carte(-1,"a","a",1)
    try:
        val.validate(c)
        assert False
    except ValidatorCarteException:
        assert True
    
    c = Carte(1,"","a",1)
    try:
        val.validate(c)
        assert False
    except ValidatorCarteException:
        assert True

    c = Carte(1,"a","",1)
    try:
        val.validate(c)
        assert False
    except ValidatorCarteException:
        assert True

    c = Carte(1,"a","a",-1)
    try:
        val.validate(c)
        assert False
    except ValidatorCarteException:
        assert True
    
    c = Carte(1,"a","a",1)
    try:
        val.validate(c)
        assert True
    except ValidatorCarteException:
        assert False
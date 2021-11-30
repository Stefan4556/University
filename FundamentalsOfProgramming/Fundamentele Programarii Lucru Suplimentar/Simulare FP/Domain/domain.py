# inceputa la 23:09
"""
    Acest modul se ocupa cu retinerea clasei ce initializeaza obiectele
"""

class Destinatie:
    """
        Clasa destinatie se ocupa cu initializarea si retinerea metodelor aferente obiectelor de tipul destinatie
    """

    def __init__(self,id,locatie,sir_cuv,pret):
        """
            Cu aceasta metoda initializam cele 4 campuri ale unui obiect de tipul destinatie
        """

        self.__id = id
        self.__locatie = locatie
        self.__sir_cuv = sir_cuv
        self.__pret = pret
    
    def getId(self):
        """
            Metoda cu ajutorul careia returnam id-ul unei destinatii
        """

        return self.__id
    
    def getLocatie(self):
        """
            Metoda cu ajutorul careia returnam locatia unei destinatii
        """

        return self.__locatie
    
    def getSirCuv(self):
        """
            Metoda cu ajutorul careia returnam sirul de cuvinte
        """

        return self.__sir_cuv
    
    def getPret(self):
        """
            Metoda cu ajutorul careia returnam pretul unei destinatii
        """

        return self.__pret
    
    def __str__(self):
        """
            Metoda cu ajutorul careia transformam un obiect intr un string
        """

        return str(str(self.__id) + ", " + self.__locatie + ", " +self.__sir_cuv + ", " + str(self.__pret))

def teste_domain():

    d = Destinatie(1,"Valcea","mare mic",100)
    assert d.getId() == 1
    assert d.getLocatie() == "Valcea"
    assert d.getSirCuv() == "mare mic"
    assert d.getPret() == 100

teste_domain()
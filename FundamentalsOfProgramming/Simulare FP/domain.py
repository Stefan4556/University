class Vacanta:
    """
        Aceasta clasa defineste obiectul de tip vacanta si metodele aferente acestuia
    """

    def __init__(self,id,locatie,sir_cuvinte,pret):
        """
            Cu ajutorul acestei metode initializam cele 4 campuri ale unei Vacante:
            - id
            - locatie
            - sir cuvinte cheie
            - pret
        """

        self.__id = id
        self.__locatie = locatie
        self.__sir_cuvinte = sir_cuvinte
        self.__pret = pret
    
    def getId(self):
        """
            Rolul acestei metode este de a returna id-ul unei vacante
        """

        return self.__id
    
    def getLocatie(self):
        """
            Aceasta metoda are scopul de a returna locatia pe care o vacanta o are
        """

        return self.__locatie
    
    def getSirCuvinte(self):
        """
            Cu ajutoru acestei metode este returnat sirul de cuvinte cheie ale vacantei respective
        """

        return self.__sir_cuvinte
    
    def getPret(self):
        """
            Aceasta metoda returneaza pretul unei vacante
        """

        return self.__pret

    def __str__(self):
        """
            Rolul acestei metode este de a returna un obiect de tip vacanta sub forma de string
        """

        return str(str(self.getId()) + "," + self.getLocatie() + "," + self.getSirCuvinte() + "," + str(self.getPret()))

def teste_domain():

    v = Vacanta(1,"Ramnicu Valcea","fain cald",200)
    assert v.getId() == 1
    assert v.getLocatie() == "Ramnicu Valcea"
    assert v.getSirCuvinte() == "fain cald"
    assert v.getPret() == 200
    assert str(v) == "1,Ramnicu Valcea,fain cald,200"

teste_domain()

class Melodie:
    """
        Clasa ce se ocupa cu creearea si retinerea metodelor aferente obiectelor de tip Melodie
    """

    def __init__(self,id,nume,nume_autor,gen):
        """
            Cu aceasta metoda initializam cele 4 campuri ale unui obiect de tip Melodie
        """

        self.__id = id
        self.__nume = nume
        self.__nume_autor = nume_autor
        self.__gen = gen
    
    def getId(self):
        """
            Rolul acestei metode este de a returna id-ul unei Melodii
        """

        return self.__id
    
    def getNume(self):
        """
            Rolul acestei metode este de a returna numele unei Melodii
        """

        return self.__nume

    def getNumeAutor(self):
        """
            Rolul acestei metode este de a returna numele autorului unei Melodii
        """

        return self.__nume_autor
    
    def getGen(self):
        """
            Rolul acestei metode este de a returna genul unei Melodii
        """

        return self.__gen
    
    def __str__(self):
        """
            Rolul acestei metode este de a returna un obiect de tip Melodie sub forma unui string
        """

        return str(str(self.getId()) + "," + self.getNume() + "," + self.getNumeAutor() + "," + self.getGen())

class Validator_melodie_exception(Exception):
    """
        Cu ajutorul acestei clase retinem erorile ce pot aparea la nivelul validatorului
    """

    pass

class Validator:
    """
        Cu ajutorul acestei clase stocam validatorii unui obiect de tip Melodie
    """

    def valideaza_melodie(self,m):
        """
            Cu ajutorul acestei metode validam obiectul
        """

        if m.getId() < 0:

            raise Validator_melodie_exception("Id-ul nu poate sa fie un numar negativ!")

def teste_domain():

    m = Melodie(1,"Otelul Galati","Marius","Imn")
    
    assert m.getId() == 1
    assert m.getNume() == "Otelul Galati"
    assert m.getNumeAutor() == "Marius"
    assert m.getGen() == "Imn"
    assert str(m) == "1,Otelul Galati,Marius,Imn"

    val = Validator()

    m = Melodie(-1,"Otelul Galati","Marius","Imn")
    try:
        val.valideaza_melodie(m)
        assert False
    except Validator_melodie_exception:
        assert True
    
    m = Melodie(1,"Otelul Galati","Marius","Imn")
    try:
        val.valideaza_melodie(m)
        assert True
    except Validator_melodie_exception:
        assert False

teste_domain()
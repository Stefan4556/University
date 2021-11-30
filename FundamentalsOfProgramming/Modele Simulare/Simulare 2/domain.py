class Bicicleta():
    """
        clasa ce se ocupa cu retinerea detaliilor despre o bicicleta si cu metodele aferente acesteia
    """

    def __init__(self,id,tip,pret):
        """
            metoda prin care initializam un obiect de tip bicicleta
        """

        self.__id = id
        self.__tip = tip
        self.__pret = pret
    
    def getId(self):
        """
            metoda ce returneaza id bicicleta
        """

        return self.__id
    
    def getTip(self):
        """
            metoda ce returneaza tip bicicleta
        """

        return self.__tip
    
    def getPret(self):
        """
            metoda ce returneaza pret bicicleta
        """

        return self.__pret
    
    def __str__(self):
        """
            metoda ce returneaza un obiect bicicleta sub forma de string
        """

        return str(str(self.getId()) + ", " + self.getTip() + ", " + str(self.getPret()))

class Validator_bicicleta_exception(Exception):
    """
        Clasa ce prinde erorile ce pot aparea la niveul validatorilor
    """

    pass

class ValidatorBicicleta():
    """
        Clasa ce se ocupa cu validarea bicicletelor
    """

    def valideaza_bicicleta(self,c):
        """
            Metoda ce se ocupa cu validarea propriu-zisa a obiectului
        """

        if c.getId() < 0:
            raise Validator_bicicleta_exception("Id-ul nu poate sa fie un numar negativ!")

def teste_domain():

    b = Bicicleta(1,"bmx",500)

    assert b.getId() == 1
    assert b.getTip() == "bmx"
    assert b.getPret() == 500

    val = ValidatorBicicleta()

    b = Bicicleta(-1,"bmx",501)

    try:
        val.valideaza_bicicleta(b)
        assert False
    except Validator_bicicleta_exception:
        assert True
    
    b = Bicicleta(1,"bmx",501)
    try:
        val.valideaza_bicicleta(b)
        assert True
    except Validator_bicicleta_exception:
        assert False

teste_domain()
"""
    Domain-ul ce retine id_inchirierii, statusul unei carti, id_clientului si id_cartii
"""

class Inchiriere():
    """
        Clasa inchiriere
    """

    def __init__(self,id_inchiriere,id_client,id_carte):
        """
            Initializam obiectul de tip Inchiriere
        """

        self.__id_inchiriere = id_inchiriere
        self.__id_client = id_client
        self.__id_carte = id_carte
    
    def getId_inchiriere(self):
        """
            Metoda ce returneaza id-ul inchirierii
        """

        return self.__id_inchiriere
    
    def getId_client(self):
        """
            Metoda ce returneaza id-ul clientului ce a realizat inchirierea
        """

        return self.__id_client
    
    def getId_carte(self):
        """
            Metoda ce returneaza id-ul cartii pe care clientul a inchiriat-o
        """

        return self.__id_carte

    def __str__(self):
        """
            Cu ajutorul acestei metode convertim dintr-un obiect intr-un sir de stringuri pentru a afisa mai frumos
        """

        return "ID: " + str(self.getId_inchiriere()) + ", Client: " + str(self.getId_client()) + ", Carte: " + str(self.getId_carte())

class Validator_inchirieri_exception(Exception):
    """
        Clasa ce retine exceptiile ce pot aparea la nivelul validarii datelor inchirierii
    """

    pass

class Validator_inchiriere:
    """
        Clasa ce se ocupa cu validarea datelor inchirierii
    """

    def valideaza_inchiriere(self,inchiriere):

        if inchiriere.getId_inchiriere() < 0 or inchiriere.getId_inchiriere() > 999:
            raise Validator_inchirieri_exception("Id invalid")

def TesteCreareInchiriere():

    i = Inchiriere(1,2,3)
    assert i.getId_inchiriere() == 1
    assert i.getId_client() == 2
    assert i.getId_carte() == 3

def Teste_valideaza_inchiriere():

    val = Validator_inchiriere()

    i = Inchiriere(1,2,3)
    try:
        val.valideaza_inchiriere(i)
        assert True
    except Validator_inchirieri_exception:
        assert False
    
    i = Inchiriere(-1,2,3)
    try:
        val.valideaza_inchiriere(i)
        assert False
    except Validator_inchirieri_exception:
        assert True
    
    i = Inchiriere(1000,2,3)
    try:
        val.valideaza_inchiriere(i)
        assert False
    except Validator_inchirieri_exception:
        assert True
     
    try:
        i = Inchiriere(int("a"),2,3)
        val.valideaza_inchiriere(i)
        assert False
    except ValueError:
        assert True
    
    try:
        i = Inchiriere(int(""),2,3)
        val.valideaza_inchiriere(i)
        assert False
    except ValueError:
        assert True

def Ruleaza_teste_domain_inchirieri():

    TesteCreareInchiriere()
    Teste_valideaza_inchiriere()

Ruleaza_teste_domain_inchirieri()
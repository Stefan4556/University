"""
    Domeniu clienti, getteri, setteri, validari si teste
"""

class Client():
    """
        Clasa client
    """
    
    def __init__(self,id,nume,cnp):
        """
            Initializam obiectul de tip Client
        """

        self.__id = id
        self.__nume = nume
        self.__cnp = cnp
    
    def getId_client(self):
        """
            Aceasta functie returneaza id-ul clientului
        """

        return self.__id
    
    def getNume(self):
        """
            Functia se ocupa cu returnarea numelui clientului
        """

        return self.__nume
    
    def getCnp(self):
        """
            Cu ajutorul acestei functii este aflat cnp-ul clientului
        """

        return self.__cnp
    
    def setNume(self,nume_nou):
        """
            Aceasta functie este singura metoda de a accesa numele clientului si de a-l modifica
        """

        self.__nume = nume_nou
    
    def setCnp(self,cnp_nou):
        """
            Este singura metoda de a accesa cnp-ul clientului si de a il modifica
        """

        self.__cnp = cnp_nou
    
    def __str__(self):
        """
            Am definit functia ce converteste datele unui client intr-un sir de tipul string
        """

        return "Id: " + str(self.__id) + ", Nume: " + str(self.__nume) + ", CNP: " + str(self.__cnp)

class Validator_client_exception(Exception):
    """
        Clasa ce retine exceptiile ce pot aparea la nivelul validarii datelor clientului
    """

    pass

def remove_spaces(string):
    """
        Functie ce scoate spatiile dintr-un string
    """

    return string.replace(' ','')

class Validator_client:
    """
        Clasa ce se ocupa cu validarea datelor clientului
    """

    def valideaza_client(self,client):

        erori = ""

        if client.getId_client() < 0 or client.getId_client() > 999:
            erori += "Id invalid\n"

        nume = client.getNume()
        nume = remove_spaces(nume)
        nume = nume.isalpha()
        if len(client.getNume()) == 0 or nume == False:
            erori += "Nume invalid\n"
        
        if client.getCnp() <= 999999999999 or client.getCnp() > 10000000000000:
            erori += "Cnp invalid\n"
        
        if len(erori) > 0:
            raise Validator_client_exception(erori)

def TestCreareClient():
    
    client = Client(1, "Dumitru George", 1234567891234)
    assert client.getId_client() == 1
    assert client.getNume() == "Dumitru George"
    assert client.getCnp() == 1234567891234

def TestModificareClient():

    client = Client(1, "Dumitru George", 1234567891234)
    client.setNume("Andrei Gheorghe")
    assert client.getNume() == "Andrei Gheorghe"
    client.setCnp(2131231231131)
    assert client.getCnp() == 2131231231131

def Test_remove_spaces():

    assert(remove_spaces("Stefan F")) == "StefanF"
    assert(remove_spaces("Dumitru George")) == "DumitruGeorge"
    assert(remove_spaces("Alex Popa")) == "AlexPopa"

def Test_Valideaza_client():

    val = Validator_client()

    c = Client(-1,"Stefan Farcasanu",1234567891234)
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True
        
    c = Client(1,"Stefan Farcasanu",123)
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True

    c = Client(1,"",0) 
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True
        
    c = Client(1,"",1234567891234)
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True
        
    c = Client(-1,"Stefan Farcasanu", 1)   
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True
        
    c = Client(2,"Stefan Farcasanu", 1234567891234)
    try:
        val.valideaza_client(c)
        assert True
    except Validator_client_exception:
        assert False
        
    c = Client(-1,"123",1234567891234)
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True
        
    c = Client(-1,"1a2b",1234567891234)
    try:
        val.valideaza_client(c)
        assert False
    except  Validator_client_exception:
        assert True
        
    c = Client(-1,"Stefan Farcasanu", -1)
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True
        
    c = Client(20,"Stefan Farcasanu", -123)
    try:
        val.valideaza_client(c)
        assert False
    except Validator_client_exception:
        assert True            

def Ruleaza_teste_domain_clienti():
    
    TestCreareClient()
    TestModificareClient()
    Test_remove_spaces()
    Test_Valideaza_client()

Ruleaza_teste_domain_clienti()



"""
    Domain carti, getteri, setteri, validari si teste
"""

class Carte():
    """
        Clasa carte
    """
    
    def __init__(self,id,titlu,descriere,autor):
        """
            Initializam obiectul de tip Carte
        """

        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
    
    def getId_carte(self):
        """
            Aceasta functie returneaza id-ul cartii
        """

        return self.__id
    
    def getTitlu(self):
        """
            Functia se ocupa cu returnarea titlului cartii
        """

        return self.__titlu

    def getDescriere(self):
        """
            Cu ajutorul acestei functii este aflata descrierea cartii
        """

        return self.__descriere

    def getAutor(self):
        """
            Functia returneaza numele autorului
        """

        return self.__autor
    
    def setTitlu(self,titlu_nou):
        """
            Aceasta functie reprezinta singura metoda de a accesa titlul cartii
        """
        
        self.__titlu = titlu_nou
    
    def setDescriere(self,descriere_noua):
        """
            Este singura metoda de a accesa si modifica descrierea cartii
        """

        self.__descriere = descriere_noua
    
    def setAutor(self,autor_nou):
        """
            La fel ca cele 2 metode definite anterior, are rolul de a modifica numele autorului
        """

        self.__autor = autor_nou
    
    def __str__(self):
        """
            Am definit functia ce converteste un obiect de tipul carte intr-un sir de tipul string
        """

        return "Id: " + str(self.__id) + ", Titlu: " + str(self.__titlu) + ", Descriere: " + str(self.__descriere) + ", Autor: " + str(self.__autor)

class Validator_carti_exception(Exception):
    """
        Clasa ce retine exceptiile ce pot aparea la nivelul validarii datelor cartii
    """

    pass

def remove_spaces(string):
    """
        Functie ce scoate spatiile dintr-un string
    """

    return string.replace(' ','')

class Validator_carte:
    """
        Clasa ce se ocupa cu validarea datelor clientului
    """

    def valideaza_carte(self,carte):

        erori = ""

        if carte.getId_carte() < 0 or carte.getId_carte() > 999:
            erori += "Id invalid\n"

        titlu = carte.getTitlu()
        titlu = remove_spaces(titlu)
        titlu = titlu.isalpha()
        if len(carte.getTitlu()) == 0 or titlu == False:
            erori += "Titlu invalid\n"

        descriere = carte.getDescriere()
        descriere = remove_spaces(descriere)
        descriere = descriere.isalpha()
        if len(carte.getDescriere()) == 0 or descriere == False:
            erori += "Descriere invalida\n"
        
        autor = carte.getAutor()
        autor = remove_spaces(autor)
        autor = autor.isalpha()
        if len(carte.getAutor()) == 0 or autor == False:
            erori += "Autor invalid\n"
        
        if len(erori) > 0:
            raise Validator_carti_exception(erori)

def TestCreareCarte():

    carte = Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")
    assert carte.getId_carte() == 1
    assert carte.getTitlu() == "Tata Bogat Tata Sarac"
    assert carte.getAutor() == "Robert Kiyosaki"
    assert carte.getDescriere() == "Educatie financiara"

def TestModificareCarte():

    carte = Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")
    carte.setTitlu("Carte mov")
    assert carte.getTitlu() == "Carte mov"
    carte.setDescriere("Antreprenoriat")
    assert carte.getDescriere() == "Antreprenoriat"
    carte.setAutor("Robert")
    assert carte.getAutor() == "Robert"

def Test_remove_spaces():

    assert(remove_spaces("Tata Bogat")) == "TataBogat"
    assert(remove_spaces("Tata Sarac")) == "TataSarac"
    assert(remove_spaces("De la idee")) == "Delaidee"

def Test_Valideaza_carte():

    val = Validator_carte()

    c = Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert True
    except Validator_carti_exception:
        assert False
    
    c = Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki1")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True

    c = Carte(1,"Tata Bogat Tata Sarac","Educatie98financiara","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except  Validator_carti_exception:
        assert True
    
    c = Carte(1,"Tata Bogat Tata Sarac","Educat9ie financiara","Rob8ert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(1,"Tata Bogat2 Tata Sarac","Educatie financiara","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(1,"Tata Bogat2 Tata Sarac","Educatie financiara","Rober2t Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(1,"Tata Bogat2 Tata Sarac2","Educatie21 financiara","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(1,"Tata Bogat1 Tata1 Sarac","Educatie2 financiara1","Robert1 Kiyosaki2")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(-1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(10001,"Tata Bogat Tata Sarac","Educatie financiara","Rober2t Kiyosaki21")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True

    c = Carte(-1,"Tata Bogat Tata Sarac","Ed21ucatie financiara","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(-1,"Tata Bogat Tata Sarac","Educati21 financiara","Robert Kiyosa123ki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(-11,"Tata Bo12gat Tata Sar3ac","Educatie financiara","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(-112,"Tata Bog1at Ta2ta Sarac","Educatie financiara","Ro2bert Kiyos3aki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(10001,"Tata1 Bog2at Tata Sarac","Edu2catie financiar2a","Robert Kiyosaki")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(-25,"Ta3ta Bog5at Ta1ta Sar2ac","Educ3atie finan3ciara","Rob2ert Kiyosak2i")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(1,"","","")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(-1,"A","2","-1")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(1,"A","B","-")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True
    
    c = Carte(1,"1","2","3")
    try:
        val.valideaza_carte(c)
        assert False
    except Validator_carti_exception:
        assert True

def Ruleaza_teste_domain_carte():

    TestCreareCarte()
    TestModificareCarte()
    Test_remove_spaces()
    Test_Valideaza_carte()

Ruleaza_teste_domain_carte()
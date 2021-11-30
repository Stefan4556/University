class Spa:
    """
        Clasa ce se ocupa cu initializarea obiectelor de acest tip si cu retinerea metodelor aferente acestora
    """

    def __init__(self,id,denumire_serviciu,sir_tipuri_abonamente,pret):
        """
            Metoda ce initializeaza propriu-zis un obiect de tip Spa
        """

        self.__id = id
        self.__denumire_serviciu = denumire_serviciu
        self.__sir_tipuri_abonamente = sir_tipuri_abonamente
        self.__pret = pret
    
    def getId(self):
        """
            Metoda ce returneaza id-ul unui obiect de tip spa
        """

        return self.__id
    
    def getDenumireServiciu(self):
        """
            Metoda ce returneaza denumirea serviciului unui obiect de tip spa
        """

        return self.__denumire_serviciu
    
    def getSirTipuriAbonamente(self):
        """
            Metoda ce returneaza tipurile de abonamente sub forma de string ale unui obiect de tip spa
        """

        return self.__sir_tipuri_abonamente
    
    def getPret(self):
        """
            Metoda ce returneaza pretul unui obiect de tip spa
        """

        return self.__pret
    
    def __str__(self):
        """
            Metoda ce returneaza obiectul de tip spa sub forma de string
        """

        return str(str(self.getId()) + "," + self.getDenumireServiciu() + "," + self.getSirTipuriAbonamente() + "," + str(self.getPret()))

def teste_domain():

    s = Spa(1,"Piscina","premium gold",150)
    assert s.getId() == 1
    assert s.getDenumireServiciu() == "Piscina"
    assert s.getSirTipuriAbonamente() == "premium gold"
    assert s.getPret() == 150
    assert str(s) == "1,Piscina,premium gold,150"

teste_domain()
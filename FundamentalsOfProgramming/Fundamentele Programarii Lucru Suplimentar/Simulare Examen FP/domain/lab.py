"""
    Modulul lab.py se ocupa cu retinerea clasei ce prinde erorile la nivelul validatorului si cu clasa ce creeaza obiectele de tipul lab
"""

class ValidatorLabException(Exception):
    """
        Aceasta clasa se ocupa cu erorile ce pot aparea la nivelul validatrii unui laborator
    """

    pass

class Lab:
    """
        Clasa Lab se ocupa cu initializaarea obiectelor de tip lab si cu retinerea metodelor aferente acesteia
    """

    def __init__(self,id,labnr,problemnr):
        """
            Aceasta metoda are rolul de a initializa un obiect de tipul Lab
        """

        self.__id_Student = id
        self.__lab_nr = labnr
        self.__probem_nr = problemnr
    
    def getIdStudent(self):
        """
            Metoda ce returneaza id-ul studentului caruia i a fost asignat un laborator
        """

        return self.__id_Student
    
    def getLabNr(self):
        """
            Metoda ce returneaza numarul laboratorului
        """

        return self.__lab_nr
    
    def getProblemNr(self):
        """
            Metoda ce returneaza numarul problemei
        """

        return self.__probem_nr
    
    def __str__(self):
        """
            Metoda ce returneaza un obiect de tipul lab in string
        """

        return str("Id student: " + str(self.__id_Student) + " Nr lab: " + str(self.__lab_nr) + " Nr problema: " + str(self.__probem_nr))

class ValidatorLab:
    """
        Aceasta clasa se ocupa cu validarea unui obiect de tipul Lab
    """

    def validate(self,l):
        """
            Aceasta este metoda ce ridica erorile ce pot aparea in procesul de validare al unui obiect de tip lab
        """

        erori = ""

        if l.getIdStudent() <= 0:

            erori += "Id-ul nu poate sa fie negativ!"
        
        if l.getLabNr() <= 0:

            erori += "Numarul laboratorului nu poate sa fie negativ!"
        
        if l.getProblemNr() <= "0":

            erori += "Numarul problemei nu poate sa fie negativ!"
        
        if erori != "":
            
            raise ValidatorLabException(erori)
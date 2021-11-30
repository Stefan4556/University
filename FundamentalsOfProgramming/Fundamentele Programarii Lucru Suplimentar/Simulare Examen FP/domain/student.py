"""
    Modulul student.py se ocupa cu retinerea clasei ce prinde erorile la nivelul validatorului si cu clasa ce creeaza obiectele de tipul student
"""

class ValidatorStudentException(Exception):
    """
        Aceasta clasa se ocupa cu erorile ce pot aparea la nivelul validatrii unui student
    """

    pass

class Student:
    """
        Clasa Student5 se ocupa cu initializaarea obiectelor de tip Student si cu retinerea metodelor aferente acesteia
    """

    def __init__(self,id,nume):
        """
            Aceasta metoda are rolul de a initializa un obiect de tipul Student
        """

        self.__id = id
        self.__nume = nume
    
    def getId(self):
        """
            Metoda ce returneaza id-ul studentului 
        """

        return self.__id
    
    def getNume(self):
        """
            Metoda ce returneaza numele studentului 
        """

        return self.__nume
    
    def __str__(self):
        """
            Metoda ce returneaza un obiect de tipul student in string
        """

        return str("Id: " + str(self.__id) + " Nume: " + self.__nume)
    
class ValidatorStudent:
    """
        Aceasta clasa se ocupa cu validarea unui obiect de tipul Student
    """

    def validate(self,c):
        """
            Aceasta este metoda ce ridica erorile ce pot aparea in procesul de validare al unui obiect de tip Student
        """

        erori = ""

        if c.getId() <= 0:
            
            erori += "Id-ul nu poate sa fie negativ!"
        
        if c.getNume() == "":

            erori += "Numele nu poate sa fie vid!"
        
        if erori != "":

            raise ValidatorStudentException(erori)
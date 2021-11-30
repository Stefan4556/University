"""
    Acest modul se ocupa cu retinerea a 3 clase:
        - clasa Word - ce initializeaza obiectele de acest tip
        - clasa WordValidatorException - ce retine erorile ce pot aparea la nivelul validatorului
        - clasa WordValidator - ce se ocupa cu validarea unui obiect de acest tip
"""

class Word:
    """
        Aceasta clasa se ocupa cu initializarea obiectelor de tipul Word si cu retinerea metodelor aferente acestora
    """

    def __init__(self,id,lang,word):
        """
            Metoda init initializeaza obiectul
        """

        self.__id = id
        self.__lang = lang
        self.__word = word
    
    def getId(self):
        """
            Aceasta metoda returneaza id ul unui cuvant
        """

        return self.__id
    
    def getLang(self):
        """
            Aceasta metoda returneaza limba unui cuvant
        """

        return self.__lang
    
    def getWord(self):
        """
            Aceasta metoda cuvantul propriu-zis
        """

        return self.__word
    
    def __str__(self):
        """
            Aceasta metoda returneaza boeictul sub forma de string
        """

        return str("Id: " + str(self.__id) + " Limba: " + self.__lang + " Cuvant: " + self.__word)

class WordValidatorException(Exception):
    """
        Rolul acestei metode este de a retine erorile ce pot aparea la nivelul validatorului
    """

    pass

class WordValidator:
    """
        Clasa ce retine o metoda ce valideaza obiectele de tip word
    """

    def validate(self,w):
        """
            Acesta metoda se ocupa cu validarea efectiva a unui cuvant
        """

        erori = ""

        if w.getWord() == "":

            erori += "Cuvantul nu poate sa fie vid!\n"
        
        if w.getLang() != "En" and w.getLang() != "Ro" and w.getLang() != "Fr":

            erori += "Limba in care a fost introdus cuvantul este gresita!\n"
        
        if erori != "":

            raise WordValidatorException(erori)
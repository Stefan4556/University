"""
    Rolul acestei metode este de a retien clasa Bicicleta, clasa ce intializeaza obiectele de acest tip si retine metodele aferente acesteia
"""

class Bicicleta:
    """
        Aceasta clasa se ocupa cu creearea obiectelor de tip Bicicleta si cu metodele aferente acestora
    """

    def __init__(self,id,tip,pret):
        """
            Aceasta metoda se ocupa cu initializarea campurilro unui obiect 
        """

        self.__id = id
        self.__tip = tip
        self.__pret = pret
    
    def getId(self):
        """
            Cu ajutorul acestei metode returnam id ul unei biciclete
        """

        return self.__id

    def getTip(self):
        """
            Cu ajutorul acestei metode returnam tipul unei biciclete
        """

        return self.__tip
    
    def getPret(self):
        """
            Cu ajutorul acestei metode returnam pretul unei biciclete
        """

        return self.__pret
    
    def __str__(self):
        """
            Cu ajutorul acestei metode returnam un obiect sub forma de string
        """

        return str("ID: " + str(self.__id) + " Tip: " + str(self.__tip) + " Pret: " + str(self.__pret))
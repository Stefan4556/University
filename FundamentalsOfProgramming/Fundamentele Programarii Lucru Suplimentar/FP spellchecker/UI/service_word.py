"""
    In acest modul sunt retinute 2 clase:
        - SpellCheckerControllerException - clasa ce se ocupa cu retienrea erorilor ce apar la nivelul controller-ului
        - SpellCheckerController - realzieaza legatura dintr ui domain si repo
"""

from Domain.domain_word import Word

class SpellCheckerControllerException(Exception):
    """
        Metoda ce retine erorile ce pot aparea la nivelul controller-ului
    """

    pass

class SpellCheckerController:
    """
        Aceasta clasa realizeaza legatura intre ui, domain si repo
    """

    def __init__(self,repo,val):
        """
            Rolul acestei metode este de a initializa legatura dintre ui, domain si repo 
        """

        self.__repo = repo
        self.__val = val
    
    def addWord(self,id,lang,word):
        """
            Aceasta este metoda ce se ocupa cu adaugare unui cuvant in dictionar
        """

        w = Word(id,lang,word)

        self.__val.validate(w)

        self.__repo.adaugare_word(w)
    
    def afisare_cuvinte(self):
        """
            Cu autorul acestei metode aducem lista de cuvinte in ui unde o putem afisa
        """

        return self.__repo.getAll()
    
    def verifica_propozitie(self,lang,prop):
        """
            Rolul acestei metode este de a afisa cuvintele ce nu exista in dcitonar dintr-o prop citita
        """

        w = Word(1,lang,"a")
        self.__val.validate(w)

        prop = prop.strip()
        prop = prop.split(" ")

        lista_cuvinte_inexistente = []

        for cuvinte in prop:

            if self.__repo.exista_word_in_lang(lang,cuvinte) == None:

                lista_cuvinte_inexistente.append(cuvinte)
        
        if len(lista_cuvinte_inexistente) == 0:

            raise SpellCheckerControllerException("Toate cuvintele din propozitie exista deja in dictionar!")
        
        return lista_cuvinte_inexistente
    
    def verifica_propozitie_fisier(self,input_file,lang,output_file):
        """
            Rolul acestei metode este de a corecta propozitia ce se afla intr un fisier intrroduse de utilziator si de a afisa o in altul
        """

        w = Word(1,lang,"a")
        self.__val.validate(w)
        self.__repo.verifica_prop_fisier(input_file,lang,output_file)
    
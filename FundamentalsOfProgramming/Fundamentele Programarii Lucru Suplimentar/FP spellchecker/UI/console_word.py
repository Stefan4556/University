"""
    Acest modul se ocupa cu interfata grafica a aplicatiei si retine doar o singura clasa
"""

from Domain.domain_word import WordValidatorException
from Repository.repository_word import RepositoryException
from UI.service_word import SpellCheckerControllerException

class SpellCheckerUI:
    """
        Aceasta calsa se ocupa cu interfata grafica a aplcatiei si cu legatura dintre utilziator si cod 
    """

    def __init__(self,srv):
        """
            Initializam legatura dintre consola si controller si meniul aplicatiei
        """

        self.__srv = srv
        self.__meniu = """
                        Meniu

            1) Adauga cuvant 
            2) Verifica propozitie
            3) Afiseaza propozitie corectata
            4) Afiseaza dicitonar
            5) Exit

        """
    
    def adauga_cuvant(self):
        """
            Aceasta metoda adauga un cuvant la lista
        """

        id = int(input("Introduceti id-ul cuvantului: "))
        lang = input("Introduceti limba cuvnatului: ")
        word = input("Introduceti cuvantul: ")
        self.__srv.addWord(id,lang,word)
    
    def afiseaza_dictionar(self):
        """
            Cu ajutorul acestei metode afisam cuvintele din dictionar
        """

        l = self.__srv.afisare_cuvinte()

        for cuv in l:

            print(str(cuv))
        
    def verifica_propozitie(self):
        """
            Aceasta metoda afiseaza pe ecran cuvintele dintr o propozitie ce nu se gasesc in dictionar
        """

        lang = input("Introduceti limba in care este propozitia: ")
        prop = input("Introduceti propozitia: ")
        l = self.__srv.verifica_propozitie(lang,prop)
        for cuv in l:
            print(str(cuv))
    
    def scrie_in_fisier_prop_corectata(self):
        """
            Aceasta metoda primeste o propozitie sau mai multe intr un fisier introdus de catre utilizator si creeaza un altul in care o afiseaza corectata dupa criteriile din enunt
        """

        lang = input("Introduceti limba in care este textul: ")
        fisier_input = input("Introduceti numele fisierului din care citim: ")
        fisier_output = input("Introduceti numele fisierului in care afisam: ")
        self.__srv.verifica_propozitie_fisier(fisier_input,lang,fisier_output)

    def run(self):
        """
            Aceasta este metoda efectiva ce porneste aplciatia
        """

        while True:

            print(self.__meniu)
            cmd = input("Introduceti comanda dorita: ")

            if cmd == "5":

                print("La revedere!")
                return
            
            elif cmd == "1":

                try:
                    self.adauga_cuvant()
                except ValueError:
                    print("Date de intrare invalide!")
                except WordValidatorException as e:
                    print(e)
                except RepositoryException as e:
                    print(e)
            
            elif cmd == "2":

                try:
                    self.verifica_propozitie()
                except WordValidatorException as e:
                    print(e)
                except SpellCheckerControllerException as e:
                    print(e)

            elif cmd == "3":
                
                try:
                    self.scrie_in_fisier_prop_corectata()
                except WordValidatorException as e:
                    print(e)

            elif cmd == "4":

                self.afiseaza_dictionar()
            
            else:

                print("Comanda invalida!")
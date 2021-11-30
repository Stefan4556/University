"""
    Modulul labui.py se ocupa cu interfata grafica pe care utilizatorul o vede si cu apelarea functiilor din controller
"""

from ui.labcontroller import LabControllerException
from repository.labrepository import LabRepositoryException
from domain.lab import ValidatorLabException

class LabUI:
    """
        Clasa LabUi contine metodele aferente ce realizeaza comenzile utilziatorului
    """

    def __init__(self,srv):
        """
            In aceasta metoda este initializata legatura dintre ui si controller si meniul aplicatiei
        """

        self.__srv = srv
        self.__meniu = """
                        Meniu
            
            1) Vizualizare lista studenti
            2) Cautare student dupa id
            3) Asignare laborator student
            4) Vizualizare laboratoare student
            5) Vizulaizare studenti si probleme asignate pentru un laborator dat
            6) Exit

        """
    
    def vizualizare_studenti(self):
        """
            Aceasta este metoda ce se ocupa cu primirea listei de studenti si afisarea acesteia
        """

        l = self.__srv.vizualizare_lista_studenti()

        for st in l:

            print(str(st))

    def cauta_student_id(self):
        """
            Aceasta este metoda ce se ocupa cu cautarea unui student dupa id
        """

        id = int(input("Introduceti id-ul studentului pe care-l cautati: "))
        st = self.__srv.getStudentById(id)
        print(str(st))

    def addStudentLab(self):
        """
            Aceasta este metoda ce se ocupa cu asignarea unui laborator unui student
        """

        id_student = int(input("Introduceti id-ul studentului caruia doriti sa ii asignati un laborator: "))
        lab_nr = int(input("Introduceti numarul laboratorului: "))
        prob_nr = input("Introduceti numarul problemei: ")
        self.__srv.addLab(id_student,lab_nr,prob_nr)
    
    def showStudentLabs(self):
        """
            Aceasta metoda afiseaza toate laboratoarele pe care un student le are
        """

        id_student = int(input("Introduceti id-ul studentului: "))
        l = self.__srv.getLabsByStudentId(id_student)
        for lab in l:
            print(str(lab))
    
    def vizualizare_studenti_probleme_pt_lab(self):
        """
            Aceasta metoda afiseaza pe ecran toti studentii si problemele ce au un anumit laborator
        """

        lab_nr = int(input("Introduceti numarul laboratorului: "))
        l = self.__srv.vizualizare_st_pb_nr_lab(lab_nr)
        for i in range(0,len(l)):
            print(str(l[i][0]) + " Problema: " + l[i][1])

    def run(self):
        """
            Aceasta este metoda ce porneste aplciatia si primeste comenzi de la utilizator
        """

        while True:

            print(self.__meniu)
            cmd = input("Introduceti comanda dorita: ")

            if cmd == "6":

                print("La revedere!")
                return 
            
            if cmd == "1":

                self.vizualizare_studenti()
            
            elif cmd == "2":

                try:
                    self.cauta_student_id()
                except ValueError:
                    print("Valoarea introdusa este gresita!")
                except LabControllerException as e:
                    print(e)
            
            elif cmd == "3":
                
                try:
                    self.addStudentLab()
                except ValueError:
                    print("Date de intrare invalide!")
                except LabControllerException as e:
                    print(e)
                except LabRepositoryException as e:
                    print(e)
                except ValidatorLabException as e:
                    print(e)
            
            elif cmd == "4":

                try: 
                    self.showStudentLabs()
                except ValueError:
                    print("Date de intrare invalide!")
                except LabControllerException as e:
                    print(e)
            
            elif cmd == "5":

                try:
                    self.vizualizare_studenti_probleme_pt_lab()
                except ValueError:
                    print("Date de intrare invalide!")
                except LabControllerException as e:
                    print(e)
                
            else:

                print("Comanda invalida!")


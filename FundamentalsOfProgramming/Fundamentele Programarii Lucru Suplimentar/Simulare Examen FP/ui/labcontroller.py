"""
    Modulul lab controller se ocupa cu realizarea legaturii dintre ui si aplicatia si legatura dintre cele 2 clase student si lab
"""

from domain.lab import Lab

class LabControllerException(Exception):
    """
        Aceasta este clasa ce se ocupa cu stocarea erorilor ce pot aparea la nivelul lab controller
    """

    pass

class LabController:
    """
        Aceasta este clasa LabController ce se ocuap cu realizarea legaturilor intre celelalte module si retinerea metodelor aferente
    """

    def __init__(self,st_repo,lab_repo,st_val,lab_val):
        """
            Initializam legaturile catre celelalte module
        """

        self.__st_repo = st_repo
        self.__lab_repo = lab_repo
        self.__st_val = st_val
        self.__lab_val = lab_val
    
    def addLab(self,student_id,lab_number,problem_number):
        """
            Cu ajutorul acestei metode ii asignam unui student un laborator
        """

        self.__lab_val.validate(Lab(student_id,lab_number,problem_number))  # validam

        if self.__st_repo.findById(student_id) == None:

            raise LabControllerException("Nu exista un student cu id-ul cautat!")

        self.__lab_repo.add(Lab(student_id,lab_number,problem_number))
    
    def getStudentById(self,student_id):
        """
            Cu ajutorul acestei metode returnam un student dupa id daca acesta exista, altfel ridicam o eroare
        """

        rez = self.__st_repo.findById(student_id)

        if rez == None:

            raise LabControllerException("Nu exista un student cu id-ul cautat!")
        
        return rez
    
    def getLabsByStudentId(self,student_id):
        """
            Cu ajutorul acestei metode returnam toate laboratoarele asignate unui student dupa id ul acestuia
        """

        if self.__st_repo.findById(student_id) == None:

            raise LabControllerException("Nu exista un student cu id-ul cautat!")
        
        l = self.__lab_repo.getAll()

        lista_lab = []

        for lab in l:

            if lab.getIdStudent() == student_id:

                lista_lab.append(lab)
        
        if len(lista_lab) == 0:

            raise LabControllerException("Studentul nu are laboratoare asignate!")

        return lista_lab
    
    def vizualizare_lista_studenti(self):
        """
            Metoda ce returneaza lista de studenti
        """

        return self.__st_repo.getAll()
    
    def vizualizare_st_pb_nr_lab(self,nr_lab):
        """
            Metoda cu returnarea unei liste cu cuprinde toti studentii de au un anumit laborator
        """

        l = self.__lab_repo.getAll()

        lista_rezultat = []

        for lab in l:

            if lab.getLabNr() == nr_lab:

                l_curent = []
                l_curent.append(lab.getIdStudent())
                l_curent.append(lab.getProblemNr())
                lista_rezultat.append(l_curent)
        
        if len(lista_rezultat) == 0:

            raise LabControllerException("Nu exista acest laborator!")
            
        for i in range(0,len(lista_rezultat)):

            lista_rezultat[i][0] = self.__st_repo.id_to_obj_st(lista_rezultat[i][0])
        
        return lista_rezultat

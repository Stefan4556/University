"""
    Rolula cestui modul este de a retine 2 clase:
        - RepositoryException - clasa ce retine erorile ce pot aparea la nivelul repository
        - Repository - clasa ce retine dictioanrul
"""

from Domain.domain_word import Word

class RepositoryException(Exception):
    """
        Clasa ce se ocupa cu stocarea erorilor
    """

    pass

class Repository:
    """
        Clasa ce se ocupa cu intretinerea dictionarului
    """

    def __init__(self,file_name):
        """
            Cu ajutorul acestei metode initializam dictionarul
        """

        self.__file_name = file_name
        self.__lista = []
        self.read_from_file()
    
    def read_from_file(self):
        """
            Aceasta este metoda ce citeste date din fisier pe care le transforma in obiecte si le stocheaza intr o lista
        """

        try:
            f = open(self.__file_name,"r")
        except IOError:
            pass
        
        line = f.readline().strip()
        while line != "":

            line = line.split(", ")
            w = Word(int(line[0]),line[1],line[2])
            self.__lista.append(w)
            line = f.readline().strip()
        
        f.close()
    
    def write_to_file(self):
        """
            Rolula cestei metode este de a scrie in fisier lista dupa ce aceasta sufera modificari
        """

        try:
            f = open(self.__file_name,"w")
        except IOError:
            pass

        l = self.getAll()

        for word in l:

            f.write(str(word.getId()) + ", " + word.getLang() + ", " + word.getWord() + "\n")
        
        f.close()

    def getAll(self):
        """
            Metoda returneaza lista de cuvinte 
        """

        return self.__lista
    
    def verifica_id(self,id):
        """
            Rolula cestei metode este de a verifica daca exista sau nu un obiect cu un id anume
        """

        l = self.getAll()

        for word in l:

            if word.getId() == id:

                return True
        
        return False

    def exista_word(self,wrd):
        """
            Rolul acestei metode este de a verifica daca exista un word in dictionar
        """

        l = self.getAll()

        for word in l:

            if word.getWord() == wrd:

                return True
            
        return False
    
    def exista_word_in_lang(self,lang,word):
        """
            Rolul acestei metode este de a verifica daca exista un anumit cuant intr o anumita limba
        """

        l =self.getAll()

        for wrd in l:

            if wrd.getLang() == lang and wrd.getWord() == word:

                return wrd
        
        return None

    def adaugare_word(self,w):
        """
            Metoda se ocupa cu adaugare unui cuvant in dictionar
        """

        if self.verifica_id(w.getId()) == True:

            raise RepositoryException("Exista deja un cuvant cu acest id!")
        
        if self.exista_word(w.getWord()) == True:

            raise RepositoryException("Exista deja acest cuvant in dictionar!")

        self.__lista.append(w)

        self.write_to_file()
    
    def golire_fisier_output(self,fisier_output):
        """
            Rolul acestei metode este de a golii fisierul de output pentru cerinta 3
        """

        try:
            fisier = open(fisier_output,"w")
        except IOError:
            pass
        fisier.write("")
        fisier.close()

    def citeste_fisier_input_rezolva(self,input_file,lang,fisier_output):
        """
            Aceasta metoda rezolva cerinta 3
        """

        lista_cuv_input = []
        try:
            f = open(input_file,"r")
        except IOError:
            return
        
        self.golire_fisier_output(fisier_output)

        line = f.readline().strip()

        while line != "":

            line = line.split(" ")
            lista_cuv_input = []
            for cuv in line:
                lista_cuv_input.append(cuv)
            self.scrie_fisier_output(lista_cuv_input,lang,fisier_output)
            line = f.readline().strip()
        
        f.close()
    
    def scrie_fisier_output(self,lista_cuv_input,lang,fisier_output):
        """
            Aceasta metoda este o functie auxiliara pentru metoda precedenta
        """

        try:
            fis = open(fisier_output,"a")
        except IOError:
            pass
            
        for cuvant in lista_cuv_input:

            if self.exista_word_in_lang(lang,cuvant) == None and len(cuvant) > 2: # inseamna ca nu exista si trb afisat cu { }
                fis.write("{" + cuvant + "} ")
            else:
                fis.write(cuvant + " ")
        
        fis.write("\n")
        fis.close()

    def verifica_prop_fisier(self,input_file,lang,output_file):
        """
            Aceasta metoda este apelata in service si are rolul de a rezolva cerinta 3
        """

        self.citeste_fisier_input_rezolva(input_file,lang,output_file)




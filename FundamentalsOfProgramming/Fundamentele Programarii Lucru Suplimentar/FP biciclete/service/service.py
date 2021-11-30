"""
    Acest modul contine clasa Service, clasa ce reprezinta legatura dintre consola repo si consola domain
"""

class Service:
    """
        Clasa service realizeaza legatura dintre ui si repository
    """

    def __init__(self,repo):
        """
            Cu ajutorul acestei metode realziam legatura dintre service si repo
        """

        self.__repo = repo
    
    def stergere_tip(self,tip):
        """
            Aceasta metoda are rolul de a apela functia din repo ce sterge toate bicicletele de un anumit tip
        """

        self.__repo.sterge_tip(tip)
    
    def stergere_max(self):
        """
            Aceasta metoda are rolul de a apela functia din repo ce sterge toate bicicletel de un pret maxim
        """

        self.__repo.sterge_biciclete_pret_maxim()
    
    def afisare_bicicelte(self):
        """
            Aceasta metoda are rolul de a returna lista de biciclete pentru a putea fi afisata in consola
        """

        return self.__repo.getAll()
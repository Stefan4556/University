"""
    Aceast modul se ocupa cu retinerea a 2 clase:
        - ServiceException - clasa ce retine toate erorile ce pot aparea la nivelul service-ului
        - Service - clasa ce realizeaza legatura intre consola domain si repo 
"""

from domain import Carte,ValdiatorCarte
from repository_carti import Repository
from lista_globala import lista_undo

class ServiceException(Exception):
    """
        Clasa ce se ocupa cu retinerea erorilor ce pot aparea la nivelul service-ului
    """

    pass

class Service:
    """
        Clasa Service realizeaza legatura intre consola, repo si domain
    """

    def __init__(self,repo,val):
        """
            Aceasta metoda initializeaza legatura directa catre repo si domain
        """

        self.__repo = repo
        self.__val = val
    
    def afisare_carti(self):
        """
            Aceasta metoda apeleaza functia din repo ce returneaza lsita de carti
        """

        return self.__repo.getAll()
    
    def adaugare_carte(self,id,titlu,autor,an_aparitie):
        """
            Metoda ce adauga o carte la lista
        """

        c = Carte(id,titlu,autor,an_aparitie)

        self.__val.validate(c)

        self.__repo.adaugare_carte(c)
    
    def modifica_carti(self,cifra,autor):
        """
            Metoda ce modifica autorii cartilor al caror id contine o anumita cifra
        """

        c = Carte(1,"Da",autor,1974)

        self.__val.validate(c)

        self.__repo.modifica_carti(cifra,autor)
    
    def undo_lista(self):
        """
            Metoda ce realizeaza intoarcerea la lista precedenta de carti daca aceasta a suferit modificari
        """

        self.__repo.undo()
    
    def afisare_elemente_filtru(self, sir, an):
        """
            Rolul acestei metode este de a afisa cartile ce corespund unui anumit filtru
        """

        l = self.__repo.getAll()

        lista_filtrata = []

        for carte in l:

            if sir in carte.getTitlu() and carte.getAn_aparitie() >= an:

                lista_filtrata.append(carte)
        
        if len(lista_filtrata) == 0:

            raise ServiceException("Nu exista elemente ce sa corespunda filtrului curent!")
        
        return lista_filtrata

def teste_service():

    try:
       f = open("biblioteca_test.txt","w")
    except IOError:
        pass
    f.write("1; Harap Alb; dadaaa; 1974\n2; Carte; Autor; 2012\n3; Mov; Hautor; 2013\n10; da; dadaaa; 10\n")
    f.close()
    
    repo = Repository("biblioteca_test.txt")
    val = ValdiatorCarte()
    srv = Service(repo,val)

    l = srv.afisare_carti() 
    assert len(l) == 4

    srv.adaugare_carte(100,"b","b",100)
    l = srv.afisare_carti()
    assert len(l) == 5

    srv.undo_lista()
    l = srv.afisare_carti()
    assert len(l) == 4

    srv.modifica_carti(1,"Popa")
    l = srv.afisare_carti()
    assert l[0].getAutor() == "Popa"

    try:
        l = srv.afisare_elemente_filtru("adasdasda",1000)
        assert False
    except ServiceException:
        assert True

    l = srv.afisare_elemente_filtru("",-1)
    assert len(l) == 4 

    srv.undo_lista()
    srv.undo_lista()


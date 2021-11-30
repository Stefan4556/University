from repository import Repo_spa

class Service_spa_exception(Exception):
    """
        Aceasta clasa se ocupa cu retinerea erorilor ce pot aparea la nivelul service-ului
    """

    pass

class Service_spa:
    """
        Aceasta clasa are rolul de a realiza legatura dintre ui si repo si retine totodata 2 filtre ce pot fi aplicate asupra listei de servicii spa
    """

    def __init__(self,repo):
        """
            Realizam initializarea service-ului spa
        """

        self.__repo = repo
    
    def afisare_servicii_ce_contin_tip(self,tip):
        """
            Aceasta metoda reprezinta filtrul numarul 1: afiseaza pe ecran toate serviciile ce contin un anumit abonament si le sorteaza pe acestea descrescator dupa pret
        """

        if self.__repo.cauta_abonament(tip) == False:

            raise Service_spa_exception("Nu exista acest tip de abonament!")

        l = self.__repo.getAll()

        lista = []

        for i in l:

            tipuri = i.getSirTipuriAbonamente().split(" ")

            if tip in tipuri:

                lista.append(i)
        
        for i in range(0,len(lista)-1):

            for j in range(i+1,len(lista)):

                if lista[i].getPret() < lista[j].getPret():

                    lista[i],lista[j] = lista[j],lista[i]
        
        return lista
    
    def afisare_tipuri_abonamente(self):
        """
            Aceasta metoda reprezinta filtrul numarul 2: afiseaza pe ecran toate tipurile de abonamente si care servicii au disponibile aceste tipuri
        """

        lista_tipuri = []

        l = self.__repo.getAll()

        for i in l:

            tipuri = i.getSirTipuriAbonamente()
            tipuri = tipuri.split(" ")
            for j in range(0,len(tipuri)):

                if tipuri[j] not in lista_tipuri:

                    lista_tipuri.append(tipuri[j])
        
        rezultat = []

        for i in range(0,len(lista_tipuri)):

            lista_intermediara = []

            lista_intermediara.append(lista_tipuri[i])

            for j in l:

                if lista_tipuri[i] in j.getSirTipuriAbonamente():

                    lista_intermediara.append(j.getDenumireServiciu())
            
            rezultat.append(lista_intermediara)
        
        return rezultat

def test_service():

    repo = Repo_spa("test4.txt")
    srv = Service_spa(repo)

    l = srv.afisare_tipuri_abonamente()
    assert len(l) == 5
    assert l[0][0] == "basic"
    assert l[0][1] == "Jacuzzi"

    l = srv.afisare_servicii_ce_contin_tip("gold")
    assert len(l) == 3
    assert str(l[0]) == "3,Sauna,premium gold,150"

    try:
        l = srv.afisare_servicii_ce_contin_tip("ic")
        assert False
    except Service_spa_exception:
        assert True

    try:
        l = srv.afisare_servicii_ce_contin_tip("platinum")
        assert False
    except Service_spa_exception:
        assert True

test_service()


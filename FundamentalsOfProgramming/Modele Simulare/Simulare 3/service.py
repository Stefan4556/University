from repository import Repo_arta
from domain import Arta,Validator_arta,Validator_arta_exception

class Service_exception(Exception):
    """
        Clasa ce se ocupa cu prinderea exceptiilor ce pot aparea la nivelul service-ului
    """

    pass

class Service_arta():
    """
        Rolul acestei clase este de a realiza legatura dintre ui, repo si domain
    """

    def __init__(self,repo,val):
        """
            Initializam service-ul si legaturile acestuia
        """

        self.__repo = repo
        self.__val = val
    
    def afisare_contin_sir_carac(self,sir):
        """
            Cu ajutorul acestei metode realizam filtrarea clientilor dupa urmatorul criteriu:
            daca acesteia au in denumire un sir de caractere introdus de catre utilzator sunt afisate descrescator dupa autor
        """

        l = self.__repo.getAll()

        lista = []

        for i in l:

            if sir in i.getDenumire():

                lista.append(i)
        
        if len(lista) == 0:

            raise Service_exception("Nu au fost gasite denumiri ce sa contina sirul de caractere citit!")
        
        for i in range(0,len(lista)-1):
            for j in range(i+1,len(lista)):
                if lista[i].getAutor() < lista[j].getAutor():

                    lista[i],lista[j] = lista[j],lista[i]
        
        return lista
    
    def afisare_autori_din_camera(self,camera):
        """
            Cu ajutorul acestei metode realizam urmatoarea filtrare:
            este returnata lista ce contine doar numele autorilor ale caror opere sunt expuse intr-o camera al carei numar este
            introdus de catre utilizator
        """

        self.__val.valideaza_arta(Arta(1,"da","da",camera))

        if self.__repo.cauta_camera(camera) == False:

            raise Service_exception("Nu exista o camera ca numarul dat!")
        
        l = self.__repo.getAll()

        lista = []

        for i in l:

            if i.getNrCamera() == camera:

                lista.append(i.getAutor())
        
        return lista

def teste_service():

    repo = Repo_arta("test3.txt")
    f = open("test3.txt","w")
    f.write("")
    f.close()

    f = open("test3.txt","w")
    f.write("1,Peisaj cu case de tara,Stefan Luchian,13 \n2,Giverny; casa artistului,Claude Monet,13 \n3,Impersie. Rasarit de soare,Claude Monet,13 \n")
    f.close()

    repo = Repo_arta("test3.txt")
    val = Validator_arta()

    srv = Service_arta(repo,val)

    l = srv.afisare_autori_din_camera(13)
    assert len(l) == 3
    assert (l[0]) == "Stefan Luchian"

    try:
        l = srv.afisare_autori_din_camera(200)
        assert False
    except Service_exception:
        assert True
    
    l = srv.afisare_contin_sir_carac("case")
    assert len(l) == 1
    assert str(l[0]) == "1,Peisaj cu case de tara,Stefan Luchian,13"

    try:
        l = srv.afisare_contin_sir_carac("hello")
        assert False
    except Service_exception:
        assert True
    
    try:
        l = srv.afisare_autori_din_camera(-1)
        assert False
    except Validator_arta_exception:
        assert True
    
    l = srv.afisare_contin_sir_carac("cas")
    assert len(l) == 2
    assert str(l[0]) == "1,Peisaj cu case de tara,Stefan Luchian,13"

teste_service()

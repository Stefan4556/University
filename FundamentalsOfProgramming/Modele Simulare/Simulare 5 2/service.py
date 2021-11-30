from domain import Melodie,Validator,Validator_melodie_exception
from repository import Repo_muzica

class Service_muzica_exception(Exception):
    """
        Clasa ce se ocupa cu prinderea erorilor ce pot aparea la nivelul service-ului
    """

    pass

class Service_muzica:
    """
        Rolul acestei clase este de a realiza legatura dintre ui,repo si validator
    """

    def __init__(self,repo,val):
        """
            Initializam legaturile catre repo si validator
        """

        self.__repo = repo
        self.__val = val
    
    def afisare_melodii_sir(self,sir):
        """
            Aceasta metoda se ocupa cu cerinta numarul 1, cea in care ni se cere afisarea melodiilor sortate dupa numele autorului, ce contin un anumit sir de caractere introdus
        """

        l = self.__repo.getAll()

        lista = []

        for i in l:

            if sir in i.getNume():

                lista.append(i)
        
        if len(lista) == 0:

            raise Service_muzica_exception("Nu au fost gasite melodii ce sa contina sirul introdus in nume!")

        for i in range(0,len(lista)-1):
            for j in range(i+1,len(lista)):
                if lista[i].getNumeAutor() < lista[j].getNumeAutor():
                    lista[i],lista[j] = lista[j],lista[i]
        
        return lista
    
    def afisare_piese_gen_corespunzator_id(self,id):
        """
            Aceasta metoda se ocupa ce rezolvarea cerintei 2, si anume afisarea tuturor melodiilor ce au genul muzical egal cu genul corespunzator unui id introdus
        """

        self.__val.valideaza_melodie(Melodie(id,"a","a","a"))

        if self.__repo.cauta_id(id) == False:

            raise Service_muzica_exception("Nu exista o melodie cu id-ul cautat!")

        l = self.__repo.getAll()

        lista = []

        gen = self.__repo.returneaza_gen_corespunzator_id(id)

        for i in l:

            if i.getGen() == gen:

                lista.append(i)
        
        return lista

def teste_service():

    f = open("test5.txt","w")
    f.write("")
    f.close()

    f = open("test5.txt","w")
    f.write("1,Enter Sandman,Metallica,Rock\n2,Tango to Evora,Loreena McKennit,Tango\n3,Aerials,System of a Down,Rock\n5,High on life,Martin Garrix,Edm")
    f.close()

    repo = Repo_muzica("test5.txt")
    val = Validator()
    srv = Service_muzica(repo,val)

    l = srv.afisare_melodii_sir("a")
    assert len(l) == 3
    assert str(l[0]) == "3,Aerials,System of a Down,Rock"

    try:
        l = srv.afisare_melodii_sir("Dadsadasdas")
        assert False
    except Service_muzica_exception:
        assert True

    l = srv.afisare_piese_gen_corespunzator_id(5)
    assert len(l) == 1
    assert str(l[0]) == "5,High on life,Martin Garrix,Edm"

    try:
        l = srv.afisare_piese_gen_corespunzator_id(20)
        assert False
    except Service_muzica_exception:
        assert True
    
    try:
        l = srv.afisare_piese_gen_corespunzator_id(-1)
        assert False
    except Validator_melodie_exception:
        assert True

teste_service()
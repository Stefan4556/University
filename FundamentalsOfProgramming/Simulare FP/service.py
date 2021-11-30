from repository import Repo_vacante

class Exceptii_service_vacante(Exception):
    """
        Cu ajutorul acestei clase stocam erorile ce pot aparea la nivelul service-ului
    """

    pass

class Service_vacante:
    """
        Clasa service are rolul de a realiza legatura dintre ui si repo, aceasta continand 2 metode ce se ocupa cu generarea unor rapoarte
    """

    def __init__(self,repo):
        """
            Aceasta metoda are rolul de a realiza legatura dintre service si repo
        """

        self.__repo = repo
    
    def afisare_destinatii_sir_caractere(self,sir):
        """
            Metoda aceasta reprezinta cerinta numarul 1, anume: afisarea destinatiilor care contin un anumit sir de caractere citit de la tastatura in sirul de cuvinte cheie
            In cazul in care sirul introdus este vid sau nu exista in vreun sir de cuvinte, este semnalata o eroare catre utilizator
        """

        l = self.__repo.getAll()

        if len(sir) == 0:

            raise Exceptii_service_vacante("Sirul introdus este vid!")
        
        lista = []

        for i in l:

            if sir in i.getLocatie():

                lista.append(i)
        
        if len(lista) == 0:

            raise Exceptii_service_vacante("Sirul de caractere introdus nu a fost gasit in locatii!")

        for i in range(0,len(lista)-1):

            for j in range(i+1,len(lista)):

                if lista[i].getLocatie() < lista[j].getLocatie():

                    lista[i],lista[j] = lista[j],lista[i]

        return lista

    def grupare_cuvinte_cheie(self):
        """
            Aceasta metoda consta in cerinta numarul 2, anume: gruparea dupa cuvinte cheie: pentru fiecare cuvant cheie distinct se afiseaza pretul mediu al destinatiilor
        """

        l = self.__repo.getAll()

        lista_cuv_cheie = []

        for i in l:

            sir = i.getSirCuvinte()
            sir = sir.split(" ")
            
            for j in range(0,len(sir)):

                if sir[j] not in lista_cuv_cheie:

                    lista_cuv_cheie.append(sir[j])
        
        rezultat = []

        for i in range(0,len(lista_cuv_cheie)):

            lista_intermediara = []

            lista_intermediara.append(lista_cuv_cheie[i])

            contor_curent = 0

            suma_curenta = 0

            for j in l:

                if lista_cuv_cheie[i] in j.getSirCuvinte():

                    contor_curent += 1
                    suma_curenta += j.getPret()
            
            medie = suma_curenta / contor_curent

            lista_intermediara.append(medie)

            rezultat.append(lista_intermediara)

        return rezultat

def teste_service():

    f = open("vacante_test.txt","w")
    f.write("")
    f.close()

    f = open("vacante_test.txt","w")
    f.write("31,Hawaii,soare scump clasic,1200\n2,Sinaia,frig ieftin clasic,300\n")
    f.close()

    repo = Repo_vacante("vacante_test.txt")
    srv = Service_vacante(repo)
    l = srv.afisare_destinatii_sir_caractere("ai")
    assert len(l) == 2
    assert str(l[0]) == "2,Sinaia,frig ieftin clasic,300"
    assert str(l[1]) == "31,Hawaii,soare scump clasic,1200"

    try:
        l = srv.afisare_destinatii_sir_caractere("")
        assert False
    except Exceptii_service_vacante:
        assert True
    
    try:
        l = srv.afisare_destinatii_sir_caractere("dasdasdas")
        assert False
    except Exceptii_service_vacante:
        assert True
    
    l = srv.grupare_cuvinte_cheie()
    assert len(l) == 5
    assert l[0][0] == "soare"
    assert l[0][1] == 1200
    assert l[1][0] == "scump"
    assert l[1][1] == 1200

teste_service()


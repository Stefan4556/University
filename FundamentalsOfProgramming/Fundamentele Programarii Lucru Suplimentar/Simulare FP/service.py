"""
    Rolul acestui modul este de a retine clasa de erori service si clasa service ce realzieaza legatura intre consola si repository
"""

from repository import Repository

class EroriService(Exception):
    """
        Aceasta clasa se ocupa cu retinerea erorilor ce pot aparea la nivelul service-ului
    """

    pass

class Service:
    """
        Clasa Service reprezinta legatura directa dintre consola si repository 
    """

    def __init__(self,repo):
        """
            Initializam legatura dintre consola si repository
        """

        self.__repo = repo
    
    def getLista(self):
        """
            Cu ajutorul acestei metode accesam dfunctia din repository ce se ocupa cu returnarea listei de destinatii
        """
        
        return self.__repo.getAll()
    
    def destinatii_ce_contin_sir_caractere(self,sir):
        """
            Aceasta metoda rezolva prima cerinta si anume afisare destinatiilor ce contin un anumit sir de caractere in nume si sortarea descrescatoare a acestora dupa nume
        """

        lista = self.__repo.getAll()

        lista_noua = []

        ok = 0

        for el in lista:

            if sir in el.getLocatie():

                lista_noua.append(el)
                ok = 1
        
        if ok == 0:

            raise EroriService("Nu au fost gasite destinatii ce sa contina in nume sirul de caractere introdus!")

        # ne ocupam de sortarea descrescatoare dupa nume

        lista_noua = sorted(lista_noua,key=lambda x:x.getLocatie(),reverse=True)

        return lista_noua
    
    def grupare_cuvinte_cheie(self):
        """
            Aceasta metoda are rolul de a realiza cerinta a 2 a, cerinta in care se cere realizarea unei medii aritmetice pentru fiecare cuvant cheie ce apare in sirul de cuvinte al
            unei destinatii
        """

        lista = self.__repo.getAll()

        lista_cuvinte = []

        for dest in lista:

            cuvinte_dest = dest.getSirCuv()
            cuvinte_dest = cuvinte_dest.split(" ")
            for i in range(0,len(cuvinte_dest)):
                if cuvinte_dest[i] not in lista_cuvinte:
                    lista_cuvinte.append(cuvinte_dest[i])
        
        lista_finala = []
        for cuvant in lista_cuvinte:

            lista_curenta = []
            suma_curenta = 0
            contor_curent = 0

            for dest in lista:

                cuvinte_dest = dest.getSirCuv()
                cuvinte_dest = cuvinte_dest.split(" ")
                if cuvant in cuvinte_dest:
                    suma_curenta += dest.getPret()
                    contor_curent += 1
            
            lista_curenta.append(cuvant)
            lista_curenta.append(suma_curenta/contor_curent)
            lista_finala.append(lista_curenta)
        
        return lista_finala

def test_service():

    try:
        f = open("simulareFPteste.txt","w")
    except IOError:
        pass

    f.write("31,Hawaii,soare scump clasic,1200\n2,Sinaia,frig ieftin clasic,300\n")
    f.close()
    repo = Repository("simulareFPteste.txt")
    srv = Service(repo)
    l = srv.getLista()
    assert len(l) == 2

    l = srv.destinatii_ce_contin_sir_caractere("ai")
    assert len(l) == 2
    assert str(l[0]) == "2, Sinaia, frig ieftin clasic, 300"
    assert str(l[1]) == "31, Hawaii, soare scump clasic, 1200"

    try:
        l = srv.destinatii_ce_contin_sir_caractere("x")
        assert False
    except EroriService:
        assert True
    
    l = srv.grupare_cuvinte_cheie()
    assert l[0][0] == "soare"
    assert l[0][1] == 1200

test_service()
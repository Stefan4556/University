"""
     Getteri si setteri pentru clienti si carti
"""
def creeaza_carte(Id,titlu,descriere,autor):

    carte = {
            'id': Id,
            'titlu': titlu,
            'descriere': descriere,
            'autor': autor
            }

    return carte
    
def getId_carte(carte):

    return carte['id']
    
def getTitlu(carte):

    return carte['titlu']

def getDescriere(carte):

    return carte['descriere']

def getAutor(carte):

    return carte['autor']
    
def setId_carte(carte,id_nou):

    carte['id'] = id_nou
    
def setTitlu(carte,titlu_nou):
        
    carte['titlu'] = titlu_nou
    
def setDescriere(carte,descriere_noua):

    carte['descriere'] = descriere_noua
    
def setAutor(carte,autor_nou):

    carte['autor'] = autor_nou

def creeaza_client(Id,nume,cnp):

    client = {
                'id': Id,
                'nume': nume,
                'cnp': cnp
            }
    return client
    
def getId_client(client):

    return client['id']
    
def getNume(client):

    return client['nume']
    
def getCnp(client):

    return client['cnp']
    
def setId_client(client,id_nou):

    client['id'] = id_nou
    
def setNume(client,nume_nou):

    client['nume'] = nume_nou
    
def setCnp(client,cnp_nou):

    client['cnp'] = cnp_nou

def valideaza_carte(carte):
    """
         De verificat
    """

    erori = ""

    if getId_carte(carte) < 0 or getId_carte(carte) > 999:
        erori += "Id invalid\n"

    if len(getTitlu(carte)) == 0:
        erori += "Titlu invalid\n"

    if len(getDescriere(carte)) == 0:
        erori += "Descriere invalida\n"
    
    if len(getAutor(carte)) == 0:
        erori += "Autor invalid\n"
    
    if len(erori) > 0:
        raise Exception(erori)

def valideaza_client(client):
    """
        De verificat
    """

    erori = ""

    if getId_client(client) < 0 or getId_client(client) > 999:
        erori += "Id invalid\n"

    if len(getNume(client)) < 0:
        erori += "Nume invalid\n"
    
    if getCnp(client) <= 999999999999 or getCnp(client) > 10000000000000:
        erori += "Cnp invalid\n"
    
    if len(erori) > 0:
        raise Exception(erori)

def run():
    try:
        test = creeaza_client("A","Stefan",51231)
        print(test)
        valideaza_client(test)
    except Exception as erori:
        print (erori)

    """
    try:
        test2 = creeaza_carte(132,"Salut","salut","salut")
        print (test2)
        valideaza_carte(test2)
    except Exception as erori:
        print(erori)
    """

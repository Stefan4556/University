"""
    Adaugari, stergeri, modificari, cautari
    Adaugari - done
    Stergeri - done
    Cautari - done
    Modificari - done
"""
import domain

def adauga_carte(lista_carti):

    Id = int(input("Introduceti id-ul cartii: "))
    Titlu = input("Introduceti titlul cartii: ")
    Descriere = input("Introduceti descrierea cartii: ")
    Autor = input("Introduceti autorul cartii: ")

    carte = domain.creeaza_carte(Id,Titlu,Descriere,Autor)

    lista_carti.append(carte)

def adauga_client(lista_clienti):

    Id = int(input("Introduceti id-ul clientului: "))
    Nume = input("Introduceti numele clientului: ")
    Cnp = int(input("Introduceti cnp-ul clientului: "))

    client = domain.creeaza_client(Id,Nume,Cnp)

    lista_clienti.append(client)

def sterge_client_id(lista_clienti,Id):

    i = 0

    while i < len(lista_clienti):
        if domain.getId_client(lista_clienti[i]) == Id:
            lista_clienti.pop(i)
            i -= 1
        i += 1
    
    return lista_clienti

def sterge_client_cnp(lista_clienti,cnp):
    
    i = 0

    while i < len(lista_clienti):
        if domain.getCnp(lista_clienti[i]) == cnp:
            lista_clienti.pop(i)
            i -= 1
        i += 1

    return lista_clienti

def sterge_client_nume(lista_clienti,nume):

    i = 0

    while i < len(lista_clienti):
        if domain.getNume(lista_clienti[i]) == nume:
            lista_clienti.pop(i)
            i -= 1
        i += 1
    
    return lista_clienti

def design_sterge_client():

    print("")
    print("               Meniu sterge client")
    print("")
    print("Sterge client dupa id.........................Sterge-id")
    print("Sterge client dupa nume.......................Sterge-nume")
    print("Sterge client dupa cnp........................Sterge-cnp")
    print("Intoarcere la meniul precedent................Back")
    print("")

def sterge_client(lista_clienti):

    design_sterge_client()

    while True:

        cmd = input("Introduceti comanda: ")

        if cmd == "Back":
            return

        if cmd == 'Sterge-id':
            id = int(input("Introduceti id-ul persoanei pe care doriti sa o stergeti: "))
            sterge_client_id(lista_clienti,id)
        
        elif cmd == 'Sterge-nume':
            nume = input("Introduceti numele persoanei pe care doriti sa o stergeti: ")
            sterge_client_nume(lista_clienti,nume)
        
        elif cmd == 'Sterge-cnp':
            cnp = int(input("Introduceti cnp-ul persoanei pe care doriti sa o stergeti: "))
            sterge_client_cnp(lista_clienti,cnp)
        
        design_sterge_client()

def design_sterge_carte():
    
    print("")
    print("               Meniu sterge carte")
    print("")
    print("Sterge carte dupa id.............................Sterge-id")
    print("Sterge carte dupa titlu..........................Sterge-titlu")
    print("Sterge carte dupa descriere......................Sterge-descriere")
    print("Sterge carte dupa autor..........................Sterge-autor")
    print("Intoarcere la meniul precedent...................Back")
    print("")

def sterge_carte(lista_carti):

    design_sterge_carte()

    while True:

        cmd = input("Introduceti comanda: ")

        if cmd == "Back":
            return
        
        if cmd == "Sterge-id":
            id = int(input("Introduceti id-ul cartii pe care doriti sa o stergeti: "))
            sterge_carte_id(lista_carti,id)
        
        elif cmd == "Sterge-titlu":
            titlu = input("Introduceti titlul cartii pe care doriti sa o stergeti: ")
            sterge_carte_titlu(lista_carti,titlu)
        
        elif cmd == "Sterge-descriere":
            descriere = input("Introduceti descrierea cartii pe care doriti sa o stergeti: ")
            sterge_carte_descriere(lista_carti,descriere)

        elif cmd == "Sterge-autor":
            autor = input("Introduceti autorul cartii pe care doriti sa o stergeti: ")
            sterge_carte_autor(lista_carti,autor)
        
        design_sterge_carte()

            

def design_actualizeaza_client():

    print("")
    print("                 Meniu actualizeaza client")
    print("")
    print("Actualizeaza id-ul clientului....................Actualizeaza id")
    print("Actualizeaza numele clientului...................Actualizeaza nume")
    print("Actualizeaza cnp-ul clientului...................Actualizeaza cnp")
    print("Intoarcere la meniul precedent...................Back")
    print("")

def design_actualizeaza_carte():

    print("")
    print("                 Meniu actualizeaza carti")
    print("")
    print("Actualizeaza id-ul cartii.........................Actualizeaza id")
    print("Actualizeaza titlul cartii........................Actualizeaza titlul")
    print("Actualizeaza descrierea cartii....................Actualizeaza descrierea")
    print("Actualizeaza autor................................Actualizeaza autor")
    print("Intoarcere la meniul precedent....................Back")
    print("")

def actualizeaza_client(lista_clienti):

    Id = int(input("Introduceti id-ul clientului: "))
    Nume = input("Introduceti numele clientului: ")
    Cnp = int(input("Introduceti cnp-ul clientului: "))
    
    design_actualizeaza_client()

    i = cauta_client(lista_clienti,Id,Nume,Cnp)

    if i != len(lista_clienti):

        while True:

            cmd = input("Introduceti comanda: ")

            if cmd == "Back":
                return
            
            if cmd == "Actualizeaza id":
                id_nou = int(input("Introduceti id-ul nou: "))
                domain.setId_client(lista_clienti[i],id_nou)
            
            elif cmd == "Actualizeaza nume":
                nume_nou = input("Introduceti numele nou: ")
                domain.setNume(lista_clienti[i],nume_nou)
            
            elif cmd == "Actualizeaza cnp":
                cnp_nou = int(input("Introduceti cnp-ul nou: "))
                domain.setCnp(lista_clienti[i],cnp_nou)
            
            design_actualizeaza_client()
    else:
        print("Clientul nu a fost gasit!")
        return

def actualizeaza_carte(lista_carti):

    Id = int(input("Introduceti id-ul cartii: "))
    Titlu = input("Introduceti titlul cartii: ")
    Descriere = input("Introduceti descrierea cartii: ")
    Autor = input("Introduceti autorul cartii: ")

    design_actualizeaza_carte()

    i = cauta_carte(lista_carti,Id,Titlu,Descriere,Autor)

    if i != len(lista_carti):

        while True:

            cmd = input("Introduceti comanda: ")

            if cmd == "Back":
                return
            
            if cmd == "Actualizeaza id":
                id_nou = int(input("Introduceti id-ul nou: "))
                domain.setId_carte(lista_carti[i],id_nou)
            
            elif cmd == "Actualizeaza titlul":
                titlu_nou = input("Introduceti titlul nou: ")
                domain.setTitlu(lista_carti[i],titlu_nou)
            
            elif cmd == "Actualizeaza descrierea":
                descriere_noua = input("Introduceti descrierea noua: ")
                domain.setDescriere(lista_carti[i],descriere_noua)

            elif cmd == "Actualizeaza autor":
                autor_nou = input("Introduceti autorul nou: ")
                domain.setAutor(lista_carti[i],autor_nou)
            
            design_actualizeaza_carte()
    else:
        print("Cartea nu a fost gasita!")
        return 



def sterge_carte_id(lista_carti,Id):

    i = 0

    while i < len(lista_carti):
        if domain.getId_carte(lista_carti[i]) == Id:
            lista_carti.pop(i)
            i -= 1
        i += 1
    
    return lista_carti

def sterge_carte_titlu(lista_carti,titlu):

    i = 0

    while i < len(lista_carti):
        if domain.getTitlu(lista_carti[i]) == titlu:
            lista_carti.pop(i)
            i -= 1
        i += 1
    
    return lista_carti

def sterge_carte_descriere(lista_carti,descriere):
    
    i = 0

    while i < len(lista_carti):
        if domain.getDescriere(lista_carti[i]) == descriere:
            lista_carti.pop(i)
            i -= 1
        i += 1
    
    return lista_carti

def sterge_carte_autor(lista_carti,autor):
    
    i = 0

    while i < len(lista_carti):
        if domain.getAutor(lista_carti[i]) == autor:
            lista_carti.pop(i)
            i -= 1
        i += 1
    
    return lista_carti

def cauta_client(lista_clienti,Id,nume,cnp):

    for i in range(0,len(lista_clienti)):
        if domain.getId_client(lista_clienti[i]) == Id and domain.getNume(lista_clienti[i]) == nume and domain.getCnp(lista_clienti[i]) == cnp:
            return i
    
    return i + 1 # la fel ca la cauta_carte

def cauta_carte(lista_carti,Id,Titlu,Descriere,Autor):

    for i in range(0,len(lista_carti)):
        if domain.getId_carte(lista_carti[i]) == Id and domain.getTitlu(lista_carti[i]) == Titlu and domain.getDescriere(lista_carti[i]) == Descriere and domain.getAutor(lista_carti[i]) == Autor:
            return i
    
    return i + 1 # i + 1 = len(lista_carti) || pentru a evita cazul in care cartea cautata e pe pozitia 0


def afisare_lista_clienti(lista_clienti):

    for i in range(0,len(lista_clienti)):
        print("Id: " + str(domain.getId_client(lista_clienti[i])) + " Nume: " + domain.getNume(lista_clienti[i]) + " Client: " + str(domain.getCnp(lista_clienti[i])))

def afisare_lista_carti(lista_carti):

    for i in range(0,len(lista_carti)):
        print("Id: " + str(domain.getId_carte(lista_carti[i])) + " Titlu: " + domain.getTitlu(lista_carti[i]) + " Descriere: " + domain.getDescriere(lista_carti[i]) + " Autor: " + domain.getAutor(lista_carti[i]))


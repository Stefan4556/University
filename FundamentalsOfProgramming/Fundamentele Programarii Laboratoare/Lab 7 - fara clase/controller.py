"""
    Sortari
    Statistica
    Filtrari
"""

import domain
import repository

def sortare_crescatoare_clienti_nume(lista_clienti):

    l = lista_clienti
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if domain.getNume(l[i]) > domain.getNume(l[j]):
                l[i],l[j] = l[j],l[i]
    return l

def sortare_crescatoare_clienti_id(lista_clienti):

    l = lista_clienti
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if domain.getId_client(l[i]) > domain.getId_client(l[j]):
                l[i],l[j] = l[j],l[i]
    return l

def run():

    lista_clienti = [
                     {'id': 21, 'nume': "Farcasanu Stefan", 'cnp': 2131231231},
                     {'id': 12, 'nume': "Dorel", 'cnp': 21312312},
                     {'id': 11, 'nume': "George", 'cnp': 12121212},
                     {'id': 32, 'nume': "Dumitru", 'cnp': 12123123}
                    ]
    print (lista_clienti)
    l = sortare_crescatoare_clienti_id(lista_clienti)
    print(l)
    l = sortare_crescatoare_clienti_nume(lista_clienti)
    print(l)

def design_meniu_principal():

    print("")
    print("                         Meniu principal")
    print("")
    print("Modifica lista de clienti..........................Modifica clienti")
    print("Modifica lista de carti............................Modifica carti")
    print("Cauta carte sau client.............................Cauta")
    print("Pentru a iesi din program..........................Exit")
    print("")

def design_meniu_modifica_clienti():

    print("")
    print("                     Meniu modifica lista de clienti")
    print("")
    print("Adauga client..............................................Adauga")
    print("Actualizeaza client........................................Actualizeaza")
    print("Sterge client..............................................Sterge")
    print("Afiseaza lista clienti.....................................Afiseaza")
    print("Intoarcere la meniul principal.............................Back")
    print("")

def desing_meniu_modifica_carti():

    print("")
    print("                      Meniu modifica lista de carti")
    print("")
    print("Adauga carte...............................................Adauga")
    print("Actualizeaza carte.........................................Actualizeaza")
    print("Sterge carti...............................................Sterge")
    print("Afiseaza lista carti.......................................Afiseaza")
    print("Intoarcere la meniul principal.............................Back")
    print("")

def modifica_lista_clienti(lista_clienti,lista_carti):

    design_meniu_modifica_clienti()

    comenzi = {
                'Adauga': repository.adauga_client,
                'Sterge': repository.sterge_client,
                'Actualizeaza' : repository.actualizeaza_client,
                'Afiseaza': repository.afisare_lista_clienti
              }
    
    while True:

        cmd = input("Introduceti comanda: ")

        if cmd == "Back":
            return
        if cmd in comenzi:
            try:
                comenzi[cmd](lista_clienti)
            except IndexError:
                print("Lipseste un parametru") # trebuie sa vad ce eroare e
        else:
            print("Comanda invalida")

        design_meniu_modifica_clienti() 


def modifica_lista_carti(lista_clienti,lista_carti):

    desing_meniu_modifica_carti()

    comenzi = {
                'Adauga': repository.adauga_carte,
                'Actualizeaza': repository.actualizeaza_carte,
                'Sterge': repository.sterge_carte,
                'Afiseaza': repository.afisare_lista_carti
              }
    
    while True:

        cmd = input("Introduceti comanda: ")

        if cmd == "Back":
            return
        if cmd in comenzi:
            try:
                comenzi[cmd](lista_carti)
            except IndexError:
                print("Lipseste un parametru") # trebuie sa vad ce eroare e
        else:
            print("Comanda invalida")
        
        desing_meniu_modifica_carti()
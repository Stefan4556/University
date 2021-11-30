"""
    Meniul principal
"""
import controller
def meniu():

    print("Bine ati venit!")
    a = input("Apasati enter ca sa ajungeti la meniul principal")
    comenzi = {
                'Modifica clienti': controller.modifica_lista_clienti, 
                'Modifica carti': controller.modifica_lista_carti
              }

    lista_carti = [
                    {'id': 100, 'titlu': "Aventurile lui Tom Sayer", 'descriere': "Aventura", 'autor': "Mark Twain"},
                    {'id': 10, 'titlu': "Think and grow rich", 'descriere': "Educatie financiara", 'autor': "Napoleon Hill"},
                    {'id': 20, 'titlu': "Money Master the game", 'descriere': "Independenta financiara", 'autor': "Tony Robbins"},
                    {'id': 30, 'titlu': "Rich Dad, Poor Dad", 'descriere': "Business", 'autor': "Robert T. Kiyosaki"}
                  ]

    lista_clienti = [
                     {'id': 21, 'nume': "Farcasanu Stefan", 'cnp': 2131231231},
                     {'id': 12, 'nume': "Dorel", 'cnp': 21312312},
                     {'id': 11, 'nume': "George", 'cnp': 12121212},
                     {'id': 32, 'nume': "Dumitru", 'cnp': 12123123}
                    ]

    if len(a) == 0:
        controller.design_meniu_principal()

    while True:

        cmd = input("Introduceti comanda: ")

        if cmd == "Exit":
            print("La revedere!")
            return
        if cmd in comenzi:
            try:
                comenzi[cmd](lista_clienti,lista_carti)
            except IndexError:
                print ("Lipseste un parametru") # trebuie pusa alta exceptie, cred ca cele custom aici
        else:
            print("Comanda invalida")
        
        controller.design_meniu_principal()


meniu()

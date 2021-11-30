from domain import Validator_film_exception
from repository import MovieRepositoryException

class MoviesUI():

    def __init__(self,srv):

        self.__srv = srv
        self.meniu = """      Meniul Programului
        
        1) Afisati toate filmele
        2) Updatati un film
        3) Exit 

        """
    
    def update_movie(self):

        id_m = int(input("Introduceti id-ul filmului pe care doriti sa-l modificati: "))
        nume = input("Introduceti numele filmului: ")
        pret = float(input("Introduceti pretul: "))
        nr_locuri = int(input("Introduceti numarul de locuri: "))
        self.__srv.update_movie(id_m,nume,pret,nr_locuri)

    def showUI(self):

        while True:

            print(self.meniu)
            cmd = input("Introduceti comanda: ")

            if cmd == "3":
                print("La revedere!")
                return
            
            if cmd == "1":
                
                lista = self.__srv.getAll()

                for i in lista:
                    print(str(i))

            elif cmd == "2":

                try:
                    self.update_movie()
                except ValueError:
                    print("Date invalide")
                except MovieRepositoryException as e:
                    print(e)
                except Validator_film_exception as e:
                    print(e)
            
            else:

                print("Comanda invalida!")
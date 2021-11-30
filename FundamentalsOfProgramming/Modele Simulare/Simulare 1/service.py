from domain import Movie
from repository import MovieRepository,MovieRepositoryException
from domain import Validator_movie,Validator_film_exception

class MovieControler():

    def __init__(self,repo,val):

        self.__repo = repo
        self.__val = val
    
    def getAll(self):

        return self.__repo.getAll()
    
    def update_movie(self,id_movie,name,price,booked_seats):

        m = Movie(id_movie,name,price,booked_seats)

        self.__val.valideaza_film(m)

        self.__repo.update(id_movie,name,price,booked_seats)

def teste_controler():

    repo = MovieRepository("test1.txt")
    val = Validator_movie()
    srv = MovieControler(repo,val)

    assert len(srv.getAll()) == 2
    srv.update_movie(2,"merge",19,19)

    try:
        srv.update_movie(20,"ok",11,11)
        assert False
    except MovieRepositoryException:
        assert True

teste_controler()
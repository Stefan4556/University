class Movie():

    def __init__(self,id,name,price,nr_locuri):

        self.__id = id
        self.__name = name
        self.__price = price
        self.__nr_locuri = nr_locuri
    
    def getId(self):

        return self.__id
    
    def getName(self):

        return self.__name
    
    def getPrice(self):

        return self.__price
    
    def getBookedSeats(self):

        return self.__nr_locuri
    
    def setName(self,nume):

        self.__name = nume
    
    def setPrice(self,pret):

        self.__price = pret
    
    def setBookedSeats(self,nr):

        self.__nr_locuri = nr
    
    def __str__(self):
        
        return str(self.getId()) + " " + self.getName() + " " + str(self.getPrice()) + " " + str(self.getBookedSeats())

class Validator_movie():

    def valideaza_film(self,c):

        erori = ""

        if c.getId() < 0:

            erori += "Id-ul nu poate sa fie negativ \n"

        if c.getPrice() < 10 or c.getPrice() > 20:

            erori += "Pretul dat nu este in intervalul 10,20 \n"
        
        if c.getBookedSeats() < 0 or c.getBookedSeats() > 100:

            erori += "Numarul de locuri rezervate nu este in intervalul 0,100 \n"
        
        if len(c.getName()) > 30 or c.getName() == "":

            erori += "Numele introdus nu este valid \n"
        
        if erori != "":

            raise Validator_film_exception(erori)

class Validator_film_exception(Exception):

    pass

def teste_domain():

    film = Movie(1,"Salut",21,21)
    assert film.getId() == 1
    assert film.getName() == "Salut"
    assert film.getPrice() == 21
    assert film.getBookedSeats() == 21

    film.setName("Merge")
    assert film.getName() == "Merge"

    film.setPrice(19.2)
    assert film.getPrice() == 19.2

    film.setBookedSeats(21)
    assert film.getBookedSeats() == 21

    val = Validator_movie()

    try:
        m = Movie(-1,"Merge",20,20)
        val.valideaza_film(m)
        assert False
    except Validator_film_exception:
        assert True
    
    try:
        m = Movie(1,"",20,20)
        val.valideaza_film(m)
        assert False
    except Validator_film_exception:
        assert True

    try:
        m = Movie(-1,"MergeMergeMergeMergeMergeMergeMerge",20,20)
        val.valideaza_film(m)
        assert False
    except Validator_film_exception:
        assert True

    try:
        m = Movie(1,"Merge",9,20)
        val.valideaza_film(m)
        assert False
    except Validator_film_exception:
        assert True

    try:
        m = Movie(1,"Merge",21,20)
        val.valideaza_film(m)
        assert False
    except Validator_film_exception:
        assert True

    try:
        m = Movie(1,"Merge",11,-1)
        val.valideaza_film(m)
        assert False
    except Validator_film_exception:
        assert True
    
    try:
        m = Movie(1,"Merge",11,101)
        val.valideaza_film(m)
        assert False
    except Validator_film_exception:
        assert True

teste_domain()

from domain import Movie

class MovieRepositoryException(Exception):

    pass

class MovieRepository():

    def __init__(self,file_name):

        self.__lista_movies = []
        self.__file_name = file_name
        self.load_from_file()
    
    def __len__(self):

        return len(self.__lista_movies)
    
    def load_from_file(self):

        try:
            f = open(self.__file_name,"r")
        except IOError:
            return

        line = f.readline().strip()
        while line != "":
            line = line.split(",")
            m = Movie(int(line[0]),line[1],float(line[2]),int(line[3]))
            self.__lista_movies.append(m)
            line = f.readline().strip()
        
        f.close()
    
    def write_to_file(self):

        l = self.getAll()
        f = open(self.__file_name,"w")
        for i in l:

            mov = str(str(i.getId())+","+i.getName()+","+str(i.getPrice())+","+str(i.getBookedSeats())+"\n")
            f.write(mov)

        f.close()

    def salveaza(self,m):

        self.__lista_movies.append(m)

    def update(self,id_m,nume,pret,nr_locuri):

        if self.cauta_id(id_m) == False:

            raise MovieRepositoryException("Nu exista un film cu id-ul dat!")
        
        for i in range(0,len(self.__lista_movies)):
    
            if self.__lista_movies[i].getId() == id_m:

                self.__lista_movies[i].setName(nume)
                self.__lista_movies[i].setPrice(pret)
                self.__lista_movies[i].setBookedSeats(nr_locuri)
        
        self.write_to_file()

    def cauta_id(self,id_m):

        for i in self.__lista_movies:

            if i.getId() == id_m:

                return True
        
        return False

    def getAll(self):

        return self.__lista_movies
    
    def save(self):

        self.write_to_file()

def teste_repo():

    repo = MovieRepository("test1.txt")
    l = repo.getAll()
    assert len(l)==2

    assert repo.cauta_id(1) == True
    assert repo.cauta_id(2) == True
    assert repo.cauta_id(3) == False

    try:
        repo.update(30,"da",11,11)
        assert False
    except MovieRepositoryException:
        assert True
    
    try:
        repo.update(1,"a mers",11.1,11)
        assert True
    except MovieRepositoryException:
        assert False

    f = open("test1.txt","w")
    f.write("")
    f.close()
    f = open("test1.txt","w")
    f.write("1,Da,11,11 \n")
    f.write("2,num,12,12 \n")
    f.close()
    repo = MovieRepository("test1.txt")
    l = repo.getAll()
    assert len(l) == 2

teste_repo()
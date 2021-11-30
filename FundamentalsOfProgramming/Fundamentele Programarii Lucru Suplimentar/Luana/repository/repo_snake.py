from domain.domain_snake import Snake
from utils.utils import generate_apples,out_of_grid,compare_coordonates_with_list

class RepoSnake:

    def __init__(self,file_name):

        self.__file_name = file_name
        self.__dimension = 0
        self.__nr_mere = 0
        self.__lista_mere = []
        self.__matrice = []
        self.__snake = 0
        self.read_from_file()
        self.create_table()
    
    def read_from_file(self):

        try:
            f = open(self.__file_name,"r")
        except IOError:
            return
        
        line = f.readline().strip()
        self.__dimension = int(line)
        
        line = f.readline().strip()
        self.__nr_mere = int(line)

        f.close()
    
    def create_table(self):

        for i in range(0,self.__dimension):

            linie = ["B"] * self.__dimension
            self.__matrice.append(linie)
        
        head = [self.__dimension//2-1,self.__dimension//2]
        self.__matrice[self.__dimension//2-1][self.__dimension//2] = "H"
        tail = [[self.__dimension//2,self.__dimension//2 ],[self.__dimension//2+1,self.__dimension//2]]
        self.__matrice[self.__dimension//2][self.__dimension//2] = "T"
        self.__matrice[self.__dimension//2+1][self.__dimension//2] = "T"

        s = Snake(head,tail,"UP")
        self.__snake = s

        lista_mere = generate_apples(head,tail,self.__nr_mere,self.__dimension)

        self.__lista_mere = lista_mere

        for mar in lista_mere:

            self.__matrice[mar[0]][mar[1]] = "A"
        
    def getMatrix(self):

        return self.__matrice
    
    
    def game_over(self):
        """
        method that determines if the user lost the game or not
        :param head: list of coordinates
        :param tail: list of lists of coordinates
        :param dimension:
        :return: True - if the game is over (user failed :))
                False - otherwise
        """
        if out_of_grid(self.__snake.get_head(), self.__dimension) is True:
            return True
        for coord in self.__snake.get_tail():
            if out_of_grid(coord, self.__dimension) is True:
                return True
        return False

    def moveSnake(self, counter):
        """
        method that moves the snake in the direction that faces by a number of positions
        :param counter: how many positions the snake moves
        :return: -
        """

        dict = {"UP": [-1, 0], "DOWN": [1, 0], "LEFT": [0, -1], "RIGHT": [0, 1]}
        for single_move in range(0,counter):
            modification = dict[self.__snake.get_direction()]
            head = self.__snake.get_head()
            head[0] += modification[0]
            head[1] += modification[1]
            if compare_coordonates_with_list(head,self.__lista_mere) == True:
                lista_tail = self.__snake.get_tail()
                coord = list(lista_tail[-1])
                coord[0] += 1
                lista_tail.append(coord)
                self.__snake.setTailWithApple(lista_tail)
            for tail in self.__snake.get_tail():
                tail[0] += modification[0]
                tail[1] += modification[1]
            if self.game_over() is True:
                raise Exception
        
        self.updateMatrix()

    def updateMatrix(self):

        for line in self.__matrice:

            for i in range(0,self.__dimension):

                line[i] = "B"
        
        head = self.__snake.get_head()

        self.__matrice[head[0]][head[1]] = "H"

        tail = self.__snake.get_tail()

        for part in tail:

            self.__matrice[part[0]][part[1]] = "T"
        
        for apple in self.__lista_mere:

            if self.__matrice[apple[0]][apple[1]] == "B":

                self.__matrice[apple[0]][apple[1]] = "A"

        


        
        


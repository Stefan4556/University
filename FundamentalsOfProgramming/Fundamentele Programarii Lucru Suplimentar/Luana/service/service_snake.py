class ServiceSnake:

    def __init__(self,repo):

        self.__repo =  repo
    
    def getMatrix(self):

        return self.__repo.getMatrix()
    
    def moveSnake(self,poz):

        self.__repo.moveSnake(poz)
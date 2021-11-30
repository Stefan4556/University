class Snake:
    """
        Class Snakes initializes the coordonates of the tail, head and the direction
    """

    def __init__(self,head,tail,direction):
        """
            head - list of the coordonate of the head
            tail - a list of list which consists of the coordonate of the tail
            direction - the current direction
        """
    
        self.__head = head
        self.__tail = tail
        self.__direction = direction
    
    def setHead(self,new_head):
        """
            This method returns the coordonates of the head
        """

        self.__head = new_head
    
    def setTailWithoutApple(self,new_tail):
        """
            This method updates the list of the tail coordonates but without adding a new part
        """

        self.__tail = new_tail
    
    def setTailWithApple(self,new_tail):
        """
            This method updates the list of the tail, when the snake will eat an apple
        """

        self.__tail = new_tail
    
    def setDirection(self,new_direction):
        """
            This method sets the new direction of the snake
        """

        self.__direction = new_direction
    
    def get_head(self):
        """
            Using this method will return the coordonates of the head
        """

        return self.__head
    
    def get_tail(self):
        """
            Using this method will return the coordonates of the tail
        """

        return self.__tail
    
    def get_direction(self):
        """
            Using this method will return the direction
        """

        return self.__direction

        
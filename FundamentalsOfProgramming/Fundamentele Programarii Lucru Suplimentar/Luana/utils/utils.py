from random import randrange


def adjacent(apple1, apple2):
    """
    verify if two apples are adjacent
    :return: True - if they are adjacent
             False - otherwise
    """
    if apple1[0] == apple2[0] and abs(apple1[1] - apple2[1]) <= 1:
        return True
    if apple1[1] == apple2[1] and abs(apple1[0] - apple2[0]) <= 1:
        return True
    return False


def compare_coordonates(coord1,coord2):

    return coord1[0] == coord2[0] and coord1[1] == coord2[1]

def compare_coordonates_with_list(coord,list):

    for coord1 in list:

        if coord1[0] == coord[0] and coord1[1] == coord[1]:

            return True
    
    return False

def generate_apples(head, tail, no_apples, dimension):
    """
    returns a list of coordinates of the apples randomly in a way that 2 apples aren't adjacent and any apple doesn't
    occupy any position taken by head or tail segments
    :param head: the coordinates of the head
    :param tail: a list of the coordinates of the tail
    :param no_apples: number of the apples that have to be generated
    :param dimension: integer(dimension of the matrix)
    :return: list(coordinates)
    """
    apple_counter = 0
    apple_list = []
    while(apple_counter < no_apples):
        x = randrange(0, dimension)
        y = randrange(0, dimension)
        apple = [x, y]
        if apple not in apple_list and compare_coordonates(apple,head) == False and compare_coordonates_with_list(apple,tail) == False:
            is_adjacent = False
            for elem in apple_list:
                if adjacent(apple, elem) is True:
                    is_adjacent = True
            if is_adjacent is False:
                apple_counter += 1
                apple_list.append(apple)
    return apple_list

def out_of_grid(point, dimension):
    """
    verifies if a point is still on the grid (didn't pass it's limit)
    :param point: list[x, y]
    :param dimension: integer (positive)
    :return: True - if the point is not in the grid anymore
             False - otherwise
    """
    if point[0] < 0:
        return True
    if point[0] >= dimension:
        return True
    if point[1] < 0:
        return True
    if point[1] >= dimension:
        return True
    return False
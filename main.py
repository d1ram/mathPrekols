import random

class Random_Player:
    def __init__(self) -> None:
        self.choise = None
        self.last_choise = None
        self.choises = []
        
    def generate_choise(self):
        choise = random.randint(0, 1)
        if choise == 0:
            self.choise = False
            self.last_choise = False
        else:
            self.choise = True
            self.last_choise = True

    def play_turn(self):
        self.generate_choise()
        if self.choise == False:
            self.choises.append('x')
        else:
            self.choises.append('o')


class Predator:
    def __init__(self) -> None:
        self.choise = None
        self.choises = []
        self.last_choise = None

        
    def play_turn(self, last_op_choise):
        if last_op_choise == False:
            self.choise = False
            self.last_choise = False
        else:
            self.choise = False
            self.last_choise = False

        if self.choise:
            self.choises.append('o')
        else:
            self.choises.append('x')

class Tit4Tat:
    def __init__(self) -> None:
        self.choise = None
        self.choises = []
        self.last_choise = None
        
    def play_turn(self, last_op_choise):
        if last_op_choise == False:
            self.choise = False
            self.last_choise = False
        else:
            self.choise = True
            self.last_choise = True

        if self.choise:
            self.choises.append('o')
        else:
            self.choises.append('x')

def settings(y, z):
    firstpl_point = None
    secondpl_point = None
    points_list = []
    if y == 'x' and z == 'x':
        firstpl_point = 1
        secondpl_point = 1
        points_list.append(firstpl_point)
        points_list.append(secondpl_point)
        return points_list
    elif y == 'x' and z == 'o':
        firstpl_point = 5
        secondpl_point = 0
        points_list.append(firstpl_point)
        points_list.append(secondpl_point)
        return points_list
    elif y == 'o' and z == 'o':
        firstpl_point = 3
        secondpl_point = 3
        points_list.append(firstpl_point)
        points_list.append(secondpl_point)
        return points_list
    elif y == 'o' and z == 'x':
        firstpl_point = 0
        secondpl_point = 5
        points_list.append(firstpl_point)
        points_list.append(secondpl_point)
        return points_list

def calc_points(firstPL, secondPL, x):
    sum_firstpl = 0
    sum_secondpl = 0
    overall = []
    for n in range(x):
        points_list = settings(firstPL.choises[n-1], secondPL.choises[n-1])
        firstpl_points = points_list[0]
        secondpl_points = points_list[1]
        sum_firstpl += firstpl_points
        sum_secondpl += secondpl_points
    overall.append(sum_firstpl)
    overall.append(sum_secondpl)
    return overall

def set_go(firstPL, secondPL, x):
    prev_choise_firstpl = None 
    prev_choise_secondpl = None 

    for _ in range(x):
        if firstPL.last_choise is not None:
            prev_choise_firstpl = firstPL.last_choise

        if secondPL.last_choise is not None:
            prev_choise_secondpl = secondPL.last_choise  

        firstPL.play_turn(prev_choise_secondpl)
        secondPL.play_turn(prev_choise_firstpl)
    overall = calc_points(firstPL, secondPL, x)
    print("First Player Choices:", firstPL.choises, overall[0])
    print("Second Player Choices:", secondPL.choises, overall[1])

firstPL = Tit4Tat()
secondPL = Predator()

set_go(firstPL, secondPL, 10)
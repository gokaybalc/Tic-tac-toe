import pygame as py
import sys
import numpy as np


#loads modules
py.init()
#

#initilize basic constants
WİNDOW_WİDTH=600
WİNDOW_HEİGHT=600
WHİTE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
turn=0
#

#creates surface and fills it with white color
surface=py.display.set_mode((WİNDOW_WİDTH,WİNDOW_HEİGHT))
surface.fill(WHİTE)
#

#Sets game icon and title
py.display.set_caption("Tic-Tac-Toe")
icon=py.image.load("Tic-tac-toe.png")
py.display.set_icon(icon)
#

#Creates grid class to form grids
class Grid(py.Rect):
    def __init__(self,left,top,width,height,touched=False):
        self.touched=touched
        self.shape=0
        super().__init__(left,top,width,height)

    def draw_line(self):
        py.draw.line(surface,RED,(self.left,self.top),(self.left+80,self.top+80),2)
        py.draw.line(surface,RED,(self.left+80,self.top),(self.left,self.top+80),2)
    
    def draw_circle(self):
        py.draw.circle(surface,BLUE,(self.left+40,self.top+40),40,2)
    
    def set_touched(self):
        self.touched=True
        if turn%2!=0:
            self.draw_circle()
            self.shape=7
        else:
            self.draw_line()
            self.shape=2



#Checks who is the winner
def check(ls):
    shapes=np.reshape((np.array([x.shape for x in ls])),(3,3))
    row=shapes.sum(0)
    column=shapes.sum(1)
    antidiagonal=np.trace(np.fliplr(shapes))
    diagonal=np.trace(shapes)
    if 21 == diagonal or 21 in column or 21 == antidiagonal or 21 in row:
        myfont = py.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Player 1 Wins!', False, (0, 0, 0))
        surface.blit(textsurface,(0,0))
        
        return False

    elif 6 == diagonal or 6 in column or 6 == antidiagonal or 6 in row:
        myfont = py.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Player 2 Wins!', False, (0, 0, 0))
        surface.blit(textsurface,(0,0))
        
        return False

    elif 0 not in shapes:
        myfont = py.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Drawn!', False, (0, 0, 0))
        surface.blit(textsurface,(0,0))
        
        return False
    
    else:
        return True

#
#Creates nine grid onjects and adds them to a list
def List_of_Grids():
    grids=[]
    for y in range(1,4):
        for x in range(1,4):
            grids+=[Grid(100+80*x,100+80*y,80,80)]

    return grids
#

#İnitialize grids

def setup(ls,b):
    py.draw.rect(surface,BLACK,b,0)
    myf = py.font.SysFont('Comic Sans MS', 20)
    textsrf = myf.render('Again', False, (255,255,255))
    surface.blit(textsrf,(478,150))

    for grid in ls:
        py.draw.rect(surface,BLACK,grid,2)
        grid.touched=False
        grid.shape=0

#

#event loop
def handler(ls,T,C,button):
    C=check(ls)
    for i in py.event.get():
        if i.type == py.QUIT:
            exit(0)
        if i.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            if button.collidepoint(pos)==True:
                surface.fill(WHİTE)
                setup(ls,button)
                T=0
                C=True
                return T,C

            else:
                for x in ls:
                    if x.collidepoint(pos)==True and x.touched==False and C:
                        x.set_touched()
                        T+=1
                        return T,C
    return T,C
#               

grids=List_of_Grids()
button=py.Rect(475,150,60,40)
C=True
setup(grids,button)
while True:    
    turn,C=handler(grids,turn,C,button)
    py.display.update()
    



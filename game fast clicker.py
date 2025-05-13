import pygame
pygame.init()
from random import randint
from time import time
BLUE=(50, 76, 168)
BLACK=(0 , 0 , 0)
RED=(130, 8, 8)
PURPLE=(157, 0, 168)
RED2=(168, 64, 50)
mw = pygame.display.set_mode((500, 500))

fps = pygame.time.Clock()
class Area ():
    def __init__ (self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color=color
    def color(self,new_color):
        self.fill_color=new_color
    def fill (self):
        pygame.draw.rect(mw,self.fill_color,self.rect)
    def outline(self,frame_color,thickness):
        pygame.draw.rect(mw,frame_color,self.rect,thickness)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Kartu(Area):
    def set_text(self,text,fsize,text_color):
        self.image=pygame.font.SysFont('verdana',fsize).render(text,True,text_color)
    def draw (self,shift_x,shift_y):
        self.fill()
        mw.blit(self.image,(self.rect.x + shift_x,self.rect.y + shift_y))
list_kartu=[]
kartu1=Kartu(100,150,50,100,RED)
kartu2=Kartu(200,150,50,100,RED)
kartu3=Kartu(300,150,50,100,RED)
kartu4=Kartu(400,150,50,100,RED)
kartu1.set_text('Klik',10,PURPLE)
kartu2.set_text('Klik',10,PURPLE)
kartu3.set_text('Klik',10,PURPLE)
kartu4.set_text('Klik',10,PURPLE)
list_kartu.append(kartu1)
list_kartu.append(kartu2)
list_kartu.append(kartu3)
list_kartu.append(kartu4)
jeda = 0
poin=0
label_poin=Kartu(10,10,100,50,BLUE)
label_timer=Kartu(310,10,50,50,BLUE)
waktu_awal=time()
label_win=Kartu(250,200,200,200,RED)
label_win.set_text('WIN',70,BLACK)
label_lose=Kartu(250,200,200,200,RED)
label_lose.set_text('LOSE',70,BLACK)

run = True
while run:
    fps.tick(40)
    waktu_akhir=time()
    waktu_berlalu=round (waktu_akhir-waktu_awal)
    label_poin.set_text(f'Poin: {poin}',35,BLACK)
    label_timer.set_text(f'Waktu: {waktu_berlalu}',35,BLACK)

    if jeda == 0:
        mw.fill((BLUE))
        label_poin.draw(0,0)
        label_timer.draw(0,0)
        index_random = randint (0,len(list_kartu) -1 )
        kartu_random = list_kartu[index_random]
        for kartu in list_kartu:
            kartu.outline(BLACK,15)
            kartu.color(RED)
            kartu.draw(5,50)
            if kartu == kartu_random:
                kartu.set_text('Klik',10,PURPLE)
            else:
                kartu.fill()
        jeda=20
    else:
        jeda-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y= event.pos

            for kartu in list_kartu:
                if kartu.collidepoint(x,y) and kartu == kartu_random:
                    kartu.color(BLACK)
                    kartu.fill()
                    poin += 1
                if kartu.collidepoint(x,y)and kartu != kartu_random:
                    kartu.color(RED2)
                    kartu.fill()
                    poin -= 1
    if waktu_berlalu > 5:
        pygame.display.update()
        break
    pygame.display.update()  
if poin > 10:
    print ('Win')
    label_win.draw(50,80)
    pygame.display.update()  
else:
    print('Lose')
    label_lose.draw(50,80)
    pygame.display.update()  




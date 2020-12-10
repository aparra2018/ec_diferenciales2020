import random
import pygame
import json
from math import sqrt
import time
#Sistema de ecuaciones
F=lambda c,B,u: [
            [c*(u[1]-u[0])],                        #u1
            [c*(u[0]+u[4]+u[2]-3*u[1])],            #u2
            [c*(u[1]-u[2])],                        #u3
            [c*(u[4]-u[3])],                        #u4
            [c*(u[3]+u[1]+u[5]-3*u[4])],            #u5
            [c*(u[4]-u[5])]                         #u6
        ]

#Tiempo Inicial
t=0

#Valores de U en forma de arreglo
#U = random.sample(range(10,100), 6)
global U
U=[]
#Diferencia de Tiempo
#h=random.random()
h=0.4

#Tiempo Final
#L=random.randint(4, 7)
L=100

#Valores de las constantes
#c=random.randint(0,10)
c=1

#Valor del Borde
B=random.randint(0,100)



def MetodoHeun(t,u,h,Limite,F,c,B):
    #Ver la presentacion para una descripcion del metodo
    #de Heun
    LenU = len(u)
    T = [t]
    P = []
    C = []
    for i in range(0,LenU):
        P.append([u[i]])
        C.append([u[i]])
    for i in range(0,Limite):
        T.append(T[i]+h)
        for j in range(0,LenU):
            CU=[]
            for data in P:
                CU.append(data[i])
            SF=F(c,B,CU)
            DT=T[i+1]-T[i]
            P[j].append(P[j][i]+((SF[j][0])*DT))
            CUP=[]
            for data in P:
                CUP.append(data[i])
            SFP=F(c,B,CUP)
            C[j].append(C[j][i]+((SFP[j][0]+SF[j][0])/2)*DT)
    return P,C,T

def ResolverEcuacion(t,u,h,Limite,F,c,B):
    LenU = len(u)
    T = [t]
    U = []
    for i in range(0,LenU):
        U.append([u[i]])
    for i in range(0,Limite):
        T.append(T[i]+h)
        for j in range(0,LenU):
            CU=[]
            for data in U:
                CU.append(data[0])
            SF=F(c,B,CU)
            U[j].append(U[j][i]+h*SF[j][0])
    return U,T

def MainEq():
    Prediccion,Correcion,TiempoH=MetodoHeun(t,U,h,L,F,c,B)
    #Resultados,Tiempo=ResolverEcuacion(t,U,h,L,F,c,B)
    return (Prediccion,Correcion,TiempoH)


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
WINDOW_HEIGHT = 620
WINDOW_WIDTH = 500

def redondeo(numero):
    return round(numero, -3)

def MainWindow():
    global SCREEN, CLOCK, CC, Posiciones, Tabla
    Posiciones=[
        ((10,10),(210,10),(10,370),(10,10)),
        ((10,370),(210,10),(410,490),(10,370)),
        ((10,370),(10,490),(410,490),(10,370)),
        ((210,10),(610,10),(610,250),(210,10)),
        ((210,10),(610,250),(410,490),(210,10)),
        ((610,250),(410,490),(610,490),(610,250))
    ]
    Tabla = json.loads(json.dumps({
        1000: (255,56,0),
        2000: (255,109,0),
        3000: (255,137,18),
        4000: (255,161,72),
        5000: (255,180,107),
        6000: (255,196,137),
        7000: (255,209,163),
        8000: (255,219,186),
        9000: (255,228,206),
        10000: (255,236,224),
        11000: (255,243,239),
        12000: (255,249,253),
        13000: (245,243,255),
        14000: (235,238,255),
        15000: (227,233,255),
        16000: (220,229,255),
        17000: (214,225,255),
        18000: (208,222,255),
        19000: (204,219,255)
    }))
    CC=[]
    ValorInicial=19000
    CantidadU=6
    for i in range(0,CantidadU):
        U.append(ValorInicial)
        CC.append([[204,219,255],ValorInicial])
    pygame.init()
    SCREEN=pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK=pygame.time.Clock()
    SCREEN.fill(BLACK)
    Run=True
    font=pygame.font.Font('freesansbold.ttf', 60) 
    while Run==True:
        Event=False
        Objects=DrawObj(font)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition=pygame.mouse.get_pos()
                if(Event==False):
                    for Type,Root,Obj,pos in Objects:
                        if ((Type=="text") & (Obj.collidepoint(mousePosition))):
                            SumColor(pos)
                            Event=True
                            break
                if(Event==False):
                    for Type,Root,Obj,pos in Objects:
                        if ((Type=="function") & (Obj.collidepoint(mousePosition))):
                            Prediccion,Correccion,Tiempo=MainEq()
                            Update(Objects,Correccion)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

def DrawObj(font):
    Obj=[]
    j=0
    for P in Posiciones:
        Obj.append(["polygon",pygame.draw.polygon(SCREEN,CC[j][0],P),pygame.draw.polygon(SCREEN,BLACK,P,3),j])
        j=j+1
    PMedio=PM(Posiciones)
    i=len(Obj)
    j=0
    for P in PMedio:
        text = font.render(str(j), True, BLACK)
        textRect = text.get_rect()
        textRect.center = (P[0],P[1]) 
        Obj.append(["text",text,textRect,j])
        SCREEN.blit(Obj[i][1],Obj[i][2])
        j=j+1
        i=i+1
    fnc=font.render("Init",True,BLACK)
    fnc.get_rect().center=(10,10)
    Obj.append(["function",fnc,fnc.get_rect(),0])
    SCREEN.blit(fnc,fnc.get_rect())
    return Obj

def Update(Obj,Correccion):
    j=0
    for x in range(0,len(Correccion[0])): 
        for O in Obj:
            if(O[0]=="polygon"):
                for N in Tabla:
                    if(int(N)==redondeo(Correccion[j][x])):
                        r,g,b=Tabla[str(N)]
                        CC[j][0]=(r,g,b)
                        break
                j=j+1
        j=0
def PM(Posiciones):
    PMedio=[]
    for P in Posiciones:
        PMedio.append(((P[0][0]+P[1][0]+P[2][0])/3,(P[0][1]+P[1][1]+P[2][1])/3))
    return PMedio

def SumColor(pos):
    Inicial=19000
    Escala=1000
    if(CC[pos][1]==Escala):
        CC[pos][1]=Inicial
        r,g,b=Tabla[str(CC[pos][1])]
        CC[pos][0]=(r,g,b)
        U[pos]=CC[pos][1]
    elif(CC[pos][1]>=2*Escala):
        CC[pos][1]=CC[pos][1]-Escala
        r,g,b=Tabla[str(CC[pos][1])]
        CC[pos][0]=(r,g,b)
        U[pos]=CC[pos][1]

MainWindow()

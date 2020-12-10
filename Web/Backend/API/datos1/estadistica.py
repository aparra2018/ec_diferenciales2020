#!/usr/bin/env python
# -- coding: utf-8 --
import json
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import statistics as stats
import math
import bisect

def Edad(dato):
    fecha = dato.split("-")
    fechaStr = fecha[2]+"-"+fecha[1]+"-"+fecha[0]
    fecha_nacimiento = datetime.strptime(fechaStr, "%d-%m-%Y")
    edad = relativedelta(datetime.now(), fecha_nacimiento)
    return edad.years

def Mostrar(dato,petUno,petDos):
    guar = [] #arreglo que contendra los datos pedidos
    for i in range(len(dato)):
        if (isinstance(dato[i][petUno], list)): #si la primera peticion es un arreglo
            for j in range(len(dato[i][petUno])): 
                guar.append(dato[i][petUno][j][petDos]) #guarda los datos de la segunda peticion 
        else: #sí el anterior no es un arreglo 
            guar.append(dato[i][petUno]) #se almacenan los datos 
    return(guar)        

def Suma(val):
    nombres = [] #arreglo que contiene los nombres
    cont = [] #arreglo que contiene la cantidas de veces repetido el nombre
    nombres.append(val[0])#se necesita que se inicie con un valor
    cont.append(0)#se necesita que se inicie con un valor
    for i in range(len(val)):
        resNom = nombres #comparador de nombres
        resCont = cont #comparador de cantidad
        for j in range(len(nombres)):
            if nombres[j] == val[i]: #si detecta que almacenado en nombre existe una variable igual a la de los datos
                cont[j] = cont[j]+1 #le suma 1 a su contador correspondiente
                resCont = None #se reinicia el comparador
                resNom = None #se reinicia el comparador
        if resNom == nombres and resCont == cont: #si las variables y sus comparadores coinciden
            nombres.append(val[i]) #se agrega el nombre
            cont.append(1) #se agrega un 1 al contador 
    return nombres, cont

def DatosParaMapa(datos):
    return datos

def Comparador(res,Funcion,parametro1,parametro2):
    estadigrafos=None
    if(type(res[0])==str):
        if(parametro1=="fecha_nacimiento" or parametro2=="fecha_nacimiento"):
            edades=[]
            for fecha in res:
                edades.append(Edad(fecha))
            estadigrafos=Funcion(edades)
        else:
            nom,val = Suma(res)
            estadigrafos=Funcion(val)
    if(type(res[0])==int or type(res[0])==float):
        estadigrafos=Funcion(res)
    return estadigrafos


    

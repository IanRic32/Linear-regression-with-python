# -*- coding: utf-8 -*-
"""
@author: riosv
"""

from matplotlib.pyplot import* #we import all modules of a library 
import numpy as np #we import a library numpy as name np
from math import* #we import the library math to use for some mathematic calculus
def regre(x,y): #we create a function called regre with 2 parameters
    y1=[]  #it's a first empty list to append the information
    x1=[]  #it's a second empty list to append the information
    y11=[] #it's a third empty list to append the information
    x11=[] #it's a fourth empty list to append the information
    cov=[] #it's a fifth empty list to append the information
    ww=0 # we initialize a variable with 0
    yp=sum(y)/len(y) #we have a mean of y
    xp=sum(x)/len(x) #we have a mean of x
    for i in y: #we move in the data list of y or our dependent variable
        y1.append(i-yp) 
        y11.append((i-yp)**2)
    for i in x:
        x1.append(i-xp)
        x11.append((i-xp)**2)
    i=0
    while i<= len(y1)-1:
        cov.append(y1[i]*x1[i])
        i+=1
    betha1=sum(cov)/sum(x11)
    betha0=yp-betha1*xp
    raj=[]
    for i in x:
        raj.append(betha0+betha1*i)#recta de ajuste
    residuos=[]
    for i in raj:
        residuos.append((i-yp)**2)#Suma de cuadrado Estimados SCE
    residuales=[]
    r=0
    while r<= len(y)-1:
        residuales.append(y[r]-raj[r])#y me y estimada
        r+=1
    sce=sum(residuos)
    scr1=[]
    for i in residuales:
        scr1.append(i**2)#Suma de los cuadrados residuales
    scty=sum(y11)
    scr=sum(scr1)#scr
    R2=sce/scty
    regresion=[]
    for i in x:
        regresion.append(betha0+betha1*i)
    scatter(x, y, c ="blue",marker='*')
    plot(x,regresion)
    title("R^2={:.2E}".format(R2))
    legend(["{:.3e}+{:.3e}x".format(betha0,betha1),("D_0")])
    xlabel("Serie 1")
    ylabel("Serie 2")
   
    show() #we show the all plots
    
    print("**********"*10)
    print("Varianza(x)= {}\nVarianza(y)={}".format(sum(x11)/len(x11),sum(y11)/len(y11)),"\nEcuacion del modelo:\t y={:.3e}+{:.3e}x".format(betha0,betha1),"\nMedia de:\n x={}\n y={}".format(sum(x)/len(x),sum(y)/len(y) ),"\nR^2={:3e}".format(R2))
    print("Coeficiente de correlacion de pearson={}".format( (sum(cov)/len(cov) )/(pow(sum(x11)/len(x11),1/2)*pow(sum(y11)/len(y11),1/2) )) )
    print("**********"*10,"\n\n")

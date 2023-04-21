from tkinter import  *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import sympy as sp
from math import*

Set=0
raiz= Tk()
raiz.title("Graficadora")
raiz.geometry("1345x480")


frame=Frame(raiz,bg="#707070",width=705,height=600)
frame.pack(side=LEFT)

# Crear el gráfico
figura = plt.Figure()
ax = figura.add_subplot()
canvas = FigureCanvasTkAgg(figura, master=raiz)
canvas.get_tk_widget().pack()


#Variables
Lx1 = IntVar()
Lx0= IntVar()

Cx2= IntVar()
Cx1= IntVar()
Cx0= IntVar()

Qx3= IntVar()
Qx2= IntVar()
Qx1= IntVar()
Qx0= IntVar()

ex= IntVar()

xIni= IntVar()
xFin=IntVar()

z0=IntVar()

Set=0

x = np.linspace(-10, 10, 100)
x = np.arange(xIni.get(), xFin.get(), 0.1)

'''def C():
    NAEntrada.set(0)
    NBEntrada.set(0)
    Reslabel.config(text="")
    '''
def click(valor):
    global op
    if valor==1:
        op=1
    elif valor==2:
        op=2
    elif valor==3:
        op=3
    elif valor==4:
        op=4
        
        
    
def borrar():
    # Borrar la grafica y las raíces calculadas
    ax.clear()
    canvas.draw()
    #LabelNewton.config(text="")
    ''' etiqueta_raiz.config(text="")'''
    
    
def GrafL():
    global Set
    Set=1
    x = np.arange(xIni.get(), xFin.get(), 0.1)

    a=Lx1.get()
    b=Lx0.get()
    
    y=a*x+b
    print(a)
    ax.clear()
    ax.plot(x, y)
    canvas.draw()
    
    
       
def GrafC():
    global Set
    Set=2
    x = np.arange(xIni.get(), xFin.get(), 0.1)

    a=Cx2.get()
    b=Cx1.get()
    c=Cx0.get()
    
    y=a*(x**2)+b*x+c
   
    ax.clear()
    ax.plot(x, y)
    canvas.draw()
    
def GrafQ():
    global Set
    Set=3
    x = np.arange(xIni.get(), xFin.get(), 0.1)

    a=Qx3.get()
    b=Qx2.get()
    c=Qx1.get()
    d=Qx0.get()
    
    y=a*(x**3)+b*(x**2)+c*x+d
   
    ax.clear()
    ax.plot(x, y)
    canvas.draw()


def Grafe():
    global Set
    x = np.arange(xIni.get(), xFin.get(), 0.1)
    a=ex.get()
    
    y = np.exp(a*x) 
    ax.clear()
    ax.plot(x, y)
    canvas.draw()
    Set = 4


def NewtonRaphson():
    

    x0=z0.get()
    tol=0.0000001
    n=10
    global Set
    global a
    global b
    global c
    global d
  
    x=sp.symbols('x')
    if (Set==1):
        a=Lx1.get()
        b=Lx0.get()
        f=a*x+b
    elif (Set==2):
        
        a=Cx2.get()
        b=Cx1.get()
        c=Cx0.get()
        f=a*(x**2)+b*x+c
        
    elif (Set==3):
        
        a=Qx3.get()
        b=Qx2.get()
        c=Qx1.get()
        d=Qx0.get()
        f=a*(x**3)+b*(x**2)+c*x+d
    else:
        f=np.exp(a*x) 
        
    
    df=sp.diff(f)
    f=sp.lambdify(x,f)
    df=sp.lambdify(x,df)
    for k in range (n):
        x1=x0-f(x0)/df(x0)
        if(abs(x1-x0)<tol):
            print('x',k+1,'=',x1,end=' ')
            print('es una buena aproximacion de la raiz')
            return
        x0=x1
        print('x',k+1,'=',x1)
    LabelNewton=Label(frame,text=x1,
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7")
    LabelNewton.place(relx=.75 ,rely=.85)

        
        
    



    
        
    
    
#----------------------------------------------------------------------------------------------------------------
#Etiqueta Lineal
Lineal=Label(frame,text="Lineal",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.01 ,rely=.15)
#Etiqueta x1
x1=Label(frame,text="x^1",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.2 ,rely=.1)
#Entry  x1
Ex1=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Lx1)
Ex1.place(relx=0.2,rely=0.15)

#Etiqueta +
Mas=Label(frame,text="+",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.268 ,rely=.15)


#Etiqueta x0
x0=Label(frame,text="x^0",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.3 ,rely=.1)
#Entry  x0
LEx0=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Lx0)
LEx0.place(relx=0.3,rely=0.15)

#Boton Graficar Lineal
GraficarL=Button(frame,text="GraficarL",
             font=("Roboto",15,"bold"),
             width=10,
             height=1,
             command=GrafL).place(relx=.6,rely=.15)

#----------------------------------------------------------------------------------------------------------------

#Etiqueta Cuadrática
Cuadratica=Label(frame,text="Cuadratica",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.01 ,rely=.3)
#Etiqueta x2
x2=Label(frame,text="x^2",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.25 ,rely=.25)
#Entry  x2
CEx2=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Cx2)
CEx2.place(relx=0.25,rely=0.3)

#Etiqueta +
Mas=Label(frame,text="+",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.318 ,rely=.3)


#Etiqueta x1
x1=Label(frame,text="x^1",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.35 ,rely=.25)
#Entry  x1
CEx1=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Cx1)
CEx1.place(relx=0.35,rely=0.3)

#Etiqueta +
Mas=Label(frame,text="+",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.418 ,rely=.3)


#Etiqueta x0
x0=Label(frame,text="x^0",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.45 ,rely=.25)
#Entry  x0
CEx0=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Cx0)
CEx0.place(relx=0.45,rely=0.3)

#Botón Graficar Cuadratica
GraficarC=Button(frame,text="GraficarC",
             font=("Roboto",15,"bold"),
             width=10,
             height=1,command=GrafC).place(relx=.6,rely=.3)
#-------------------------------------------------------------------------------------------------------



#Etiqueta Cubica
Cubica=Label(frame,text="Cubica",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.01 ,rely=.45)
#Etiqueta x3
x3=Label(frame,text="x^3",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.2 ,rely=.4)
#Entry  x3
QEx3=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Qx3)
QEx3.place(relx=0.2,rely=0.45)

#Etiqueta +
Mas=Label(frame,text="+",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.268 ,rely=.45)


#Etiqueta x2
x2=Label(frame,text="x^2",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.3 ,rely=.4)
#Entry  x2
QEx2=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Qx2)
QEx2.place(relx=0.3,rely=0.45)

#Etiqueta +
Mas=Label(frame,text="+",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.368 ,rely=.45)


#Etiqueta x1
x1=Label(frame,text="x^1",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.4 ,rely=.4)
#Entry  x1
QEx1=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Qx1)
QEx1.place(relx=0.4,rely=0.45)

#Etiqueta +
Mas=Label(frame,text="+",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.468 ,rely=.45)


#Etiqueta x0
x0=Label(frame,text="x^0",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.5 ,rely=.4)
#Entry  x0
QEx0=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=Qx0)
QEx0.place(relx=0.5,rely=0.45)

#Botón Graficar Cúbica
GraficarQ=Button(frame,text="GraficarQ",
             font=("Roboto",15,"bold"),
             width=10,
             height=1,command=GrafQ).place(relx=.6,rely=.45)

#-------------------------------------------------------------------------------------------------------
#Etiqueta Exponencial
Exponencial=Label(frame,text="Exponencial",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.01 ,rely=.6)
#Etiqueta x3
e=Label(frame,text="e^",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.315 ,rely=.55)
#Entry  x3
Ee=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=ex)
Ee.place(relx=0.3,rely=0.6)

#Botón Graficar Exponencial
Graficare=Button(frame,text="Graficar e",
             font=("Roboto",15,"bold"),
             width=10,
             height=1,command=Grafe).place(relx=.6,rely=.6)

#---------------------------------------------------------------


#Botón Clear all
Clear=Button(frame,text="Clear All",
             font=("Roboto",15,"bold"),
             width=10,
             height=1,command=borrar).place(relx=.01,rely=.85)

#Etiqueta Xinicial
Xinicial=Label(frame,text="De X = ",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.01 ,rely=.75)
#Entry  Xinicial
Xinicial=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=xIni)
Xinicial.place(relx=0.11,rely=0.75)

#Etiqueta Xfinal
Xfinal=Label(frame,text="a X = ",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.18 ,rely=.75)
#Entry  Xfinal
Xfinal=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=xFin)
Xfinal.place(relx=0.26,rely=0.75)


#Etiqueta raices
Labell=Label(frame,text="Calcular raices(Método Newton Raphsody)",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.35 ,rely=.7)
#Etiqueta raices
LabelxIni=Label(frame,text="Valor Inicial de X",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.35 ,rely=.75)
#Entry  Xinicial
Xfinal=Entry(frame,
                  font=("Roboto",18,"bold"), width=3,textvariable=z0)
Xfinal.place(relx=0.6,rely=0.75)


#Botón Calcular
Calcular=Button(frame,text="Calcular",
             font=("Roboto",15,"bold"),
             width=7,
             height=1,command=NewtonRaphson).place(relx=.35,rely=.85)

#Etiqueta Raizz
LabelRaizi=Label(frame,text="Raiz=",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.55 ,rely=.85)

#Etiqueta Raizz


'''#Botón show
show=Button(frame,text="Mostrar",
             font=("Roboto",15,"bold"),
             width=7,
             height=1,command=Chou).place(relx=.5,rely=.85)

'''
raiz.mainloop()

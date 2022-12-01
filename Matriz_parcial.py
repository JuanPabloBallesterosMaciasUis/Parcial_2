#Se importa libreria tkinter con todas sus funciones
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import lineal
import numpy as npp
#-------------------
#funciones de la app
#-------------------


ventana_principal = Tk()
ventana_principal.title("Menu de funciones")
ventana_principal.geometry("550x300")
ventana_principal.minsize(300, 150)

# Color de la ventana
ventana_principal.config(bg="black")

frame_opciones = Frame(ventana_principal)
frame_opciones.config(bg = "green", width = 528 , height = 270)
frame_opciones.place(x = 10, y = 15)




# Label
menu = Label(frame_opciones, text = "Bienvenido a la graficadora de funciones")
menu.config(bg = "green", fg = "white", font = ("Bahnschrift Condensed",20))
menu.place(x = 95, y = 10)

texto = Label(frame_opciones, text = "Elija una opcion: ")
texto.config(bg = "green", fg = "white", font = ("Bahnschrift Condensed",20))
texto.place(x = 36, y = 60)



#Bonotones de la ventana principal
boton = Button(bg = "white",text="    Funcion lineal    ",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=115, y=150, anchor="center")

boton = Button(bg = "white",text="Funcion cuadratica",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=115, y=200, anchor="center")

boton = Button(bg = "white",text="   Funcion cubica   ",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=115, y=250, anchor="center")

boton = Button(bg = "white",text="  Funcion exponencial   ",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=280, y=149, anchor="center")

boton = Button(bg = "white",text="   Funcion logaritmica  ",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=280, y=200, anchor="center")

boton = Button(bg = "white",text="Funcion trigonometrica",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=280, y=250, anchor="center")

boton = Button(bg = "white",text="Funcion racionales",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=450, y=173, anchor="center")

boton = Button(bg = "white",text="  Funcion radical   ",fg = "black",command=lineal.funcion_lineal, font = ("Bahnschrift Condensed",14))
boton.place(x=450, y=225, anchor="center")


ventana_principal.mainloop()
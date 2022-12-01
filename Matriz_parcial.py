
from tkinter import *
import random


root = Tk()
root.title("Buscador de numeros en una matriz")
root.geometry("800x600")
root.configure(background = "light blue")


etiqueta =Label(root, text = "Ingrese el numero de filas y columnas de la matriz:")

#se posiciona la etiqueta en la ventana
etiqueta.pack()

#se crea una caja de texto para ingresar el numero de filas y columnas
caja_texto = Entry(root)


#se posiciona la caja de texto en la ventana
caja_texto.pack()


#se define una funcion para generar la matriz
def generar_matriz():
    
    #se obtiene el numero de filas y columnas de la matriz
    filas_columnas = int(caja_texto.get())
    
    #se genera la matriz con numeros aleatorios en un rango determinado
    matriz = [[random.randint(0,9) for i in range(filas_columnas)] for j in range(filas_columnas)]
    
    return matriz


#se define una funcion para buscar un numero en la matriz
def buscar_numero(matriz, numero):
    
    #se recorre la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            #si el numero se encuentra en la matriz, se retorna la posicion en la que se encuentra
            if(matriz[i][j] == numero):
                return i, j
    
    #si el numero no se encuentra en la matriz, se retorna None
    return None
        

#se define una funcion para dibujar la matriz
def dibujar_matriz(matriz):
    
    #se obtiene el canvas en el que se va a dibujar la matriz
    canvas = Canvas(root, width = 600, height = 600)
    
    #se obtiene el ancho y el alto de cada elemento de la matriz
    ancho = 600/len(matriz)
    alto = 600/len(matriz)
    
    #se recorre la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            #para cada elemento de la matriz, se dibuja un rectangulo en el canvas, de un color determinado
            canvas.create_rectangle(j*ancho, i*alto, (j+1)*ancho, (i+1)*alto, fill = "red")
            
            #dentro de cada rectangulo, se muestra el elemento de la matriz correspondiente
            canvas.create_text(j*ancho + ancho/2, i*alto + alto/2, text = str(matriz[i][j]), font = ("Arial", 16))
    
    #se posiciona el canvas en la ventana
    canvas.pack()
    
    
    #se obtiene el numero a buscar en la matriz
    numero = int(input("Ingrese el numero a buscar en la matriz: "))
    
    #se llama a la funcion para buscar el numero en la matriz
    posicion = buscar_numero(matriz, numero)
    
    #si el numero se encuentra en la matriz, se dibuja un rectangulo en el canvas, de un color verde, que indica la posicion del numero en la matriz
    if(posicion != None):
        canvas.create_rectangle(posicion[1]*ancho, posicion[0]*alto, (posicion[1]+1)*ancho, (posicion[0]+1)*alto, fill = "green")
    
    #se muestra un mensaje en la consola, indicando si el numero se encuentra o no en la matriz
    if(posicion == None):
        print("El numero no se encuentra en la matriz")
    else:
        print("El numero se encuentra en la posicion: ", posicion[0], posicion[1])


#se crea un boton para llamar a la funcion que genera la matriz
boton = Button(root, text = "Generar matriz", command = generar_matriz)

#se posiciona el boton en la ventana
boton.pack()


root.mainloop()
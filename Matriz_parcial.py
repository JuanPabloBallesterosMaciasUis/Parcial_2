import tkinter as tk
import random

root = tk.Tk()

#funcion para buscar el numero en la matriz
def buscar():
    buscar_num = int(buscar_entry.get())
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == buscar_num:
                #pintar el rectangulo correspondiente al numero en verde
                canvas.itemconfig(rectangulos[i][j], fill="green")

#funcion para crear la matriz
def crear_matriz():
    global matriz, rectangulos #matriz global y la lista de rectangulos
    matriz = []
    rectangulos = []
    #obtener el numero de filas y columnas de la matriz
    filas = int(filas_entry.get())
    columnas = int(columnas_entry.get())
    for i in range(filas):
        fila = []
        for j in range(columnas):
            #generar un numero aleatorio para cada elemento de la matriz
            num = random.randint(0, 9)
            fila.append(num)
            #dibujar los rectangulos en el canvas, almacenando los id's en la lista rectangulos
            rectangulo = canvas.create_rectangle(i*50, j*50, i*50+50, j*50+50, fill="white")
            rectangulos.append(rectangulo)
            #agregar el numero dentro del rectangulo
            canvas.create_text(i*50+25, j*50+25, text=str(num))
        matriz.append(fila)

#crear los botones y el canvas
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

tk.Label(root, text="Ingrese el numero de filas de la matriz: ").pack()
filas_entry = tk.Entry(root)
filas_entry.pack()

tk.Label(root, text="Ingrese el numero de columnas de la matriz: ").pack()
columnas_entry = tk.Entry(root)
columnas_entry.pack()

tk.Button(root, text="Crear Matriz", command=crear_matriz).pack()

tk.Label(root, text="Buscar numero en la matriz: ").pack()
buscar_entry = tk.Entry(root)
buscar_entry.pack()

tk.Button(root, text="Buscar", command=buscar).pack()

root.mainloop()
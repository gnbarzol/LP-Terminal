import tkinter
from tkinter import Tk

def saludo():
    print("accion al presionar el botton")

def saludo2(nombre):
    print("accion al presionar el botton",nombre)


root = Tk()
root.geometry("700x300") #width height root

etiqueta = tkinter.Label(root, text ="Analizador Ruby")
etiqueta.grid(row=0,column=0)

codigo_text_area = tkinter.Text(root, height=7, width=30)
codigo_text_area.grid(row=2,column=0)

boton_lexico = tkinter.Button(root, text="Analizar Lexico", padx=40, pady=30,
                        command = saludo) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis
boton_lexico.grid(row=2,column=1)

boton_sintactico = tkinter.Button(root, text="Analizar Sintactico", padx=40, pady=30,
                        command = lambda: saludo2("Diego")) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis
boton_sintactico.grid(row=2,column=2)

result_text_area = tkinter.Text(root, height=5, width=40)
result_text_area.grid(row=3,column=0)

'''''
boton3 = tkinter.Button(root, text="presiona para obtener ", padx=40, pady=30,
                        command = lambda: saludo2(T.get("1.0", "end-1c"))) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis
boton3.grid(row=3,column=3)
'''

'''mantiene abiertala root'''
root.mainloop()

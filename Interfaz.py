import tkinter
from tkinter import Tk
import FuncionesVentana as fn
from lexico import lexer
from sintactico import parser

root = Tk()
root.geometry("550x300") #width height root

def analyze(data,resul_text_area):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        linea = str(tok)+"\n"
        result_text_area.insert(tkinter.INSERT,linea)
        print(tok)

def analyzeLexico(resul_text_area):
    result_text_area.delete("1.0", 'end-1c')
    archivo = open("prueba.txt", "r")
    for line in archivo:
        if len(line) == 0:
            break
        print(">>>" + line)
        analyze(line,result_text_area)



def analyzeSintactico(result_text_area):
    result_text_area.delete("1.0", 'end-1c')
    archivo = open("prueba.txt", "r")
    for line in archivo:
        result = parser.parse(line)
        print(result)
        linea = str(result) + "\n"
        result_text_area.insert(tkinter.INSERT, linea)


def analizador_lexico(codigo_text_area):
    if(fn.existeCodigo(codigo_text_area)):
        analyzeLexico(result_text_area)

def analizador_sintactico(codigo_text_area):
    if (fn.existeCodigo(codigo_text_area)):
        analyzeSintactico(result_text_area)
        print("asdf")




etiqueta = tkinter.Label(root, text ="Analizador Ruby")
etiqueta.place(x=10,y=10, widt=100,height=30)

codigo_text_area = tkinter.Text(root, height=7, width=30,)
codigo_text_area.place(x=10,y=50,widt=250,height=100)



boton_lexico = tkinter.Button(root, text=" Analizador Lexico ", padx=40, pady=30,
                        command = lambda: analizador_lexico(codigo_text_area)) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis

boton_lexico.place(x=270,y=60,widt=100,height=75)

boton_sintactico = tkinter.Button(root, text="Analizador Sintactico", padx=40, pady=30,
                        command = lambda: analizador_sintactico(codigo_text_area)) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis
boton_sintactico.place(x=385,y=60,widt=120,height=75)

result_text_area = tkinter.Text(root, height=5, width=40)
result_text_area.place(x=150,y=160,widt=300,height=100)





root.mainloop()



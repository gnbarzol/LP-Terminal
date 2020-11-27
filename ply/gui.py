import tkinter
#from tkinter

def saludo():
    print("accion al presionar el botton")

def saludo2(nombre):
    print("accion al presionar el botton",nombre)


ventana = tkinter.Tk()
ventana.geometry("400x300") #width height ventana

etiqueta = tkinter.Label(ventana,text = "hola mundo",bg = "blue")
etiqueta.pack() #ubica en el centro
#etiqueta.pack(side = tkinter.BOTTOM) se pone bien abajo

boton1 = tkinter.Button(ventana,text="presiona",padx=40,pady=30,
                        command = saludo) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis
boton1.pack()

'''Esto es para que la funcion pueda recibir parametros'''
boton2 = tkinter.Button(ventana,text="presiona2",padx=40,pady=30,
                        command = lambda: saludo2("Diego")) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis
boton2.pack()

cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

'''obtener el texto de la caja de texto'''
boton3 = tkinter.Button(ventana,text="presiona para obtener ",padx=40,pady=30,
                        command = lambda: saludo2(cajaTexto.get())) #padx lo hara crecer
                                          #la funcion va solo el nombre sin parentesis
boton3.pack()

ventana.mainloop()

def existeCodigo(codigo_text_area):
    txt = codigo_text_area.get("1.0",'end-1c')

    if txt == "":
        return False
    else:
        guardarArchivo(txt)

        return True
def guardarArchivo(txt):
    file = open("prueba.txt", "w")
    linea = ""
    for letra in txt:
        linea += letra
    file.write(linea)
    file.close





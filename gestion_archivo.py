datos = [
"Datos de informacion en la linea 1", 
"Datos de informacion en la linea 2", 
"Datos de informacion en la linea 3", 
"Datos de informacion en la linea 4",
"Datos de informacion en la linea 5",
]


def registrar_datos(archivo, lista):
    ruta = f"./{archivo}"
    try:
        with open(ruta, "w") as nuevo_archivo:
            nuevo_archivo.write("\n".join(lista))

    except Exception as error: 
       print('Se ha generado un error no previsto', type(error).__name__)        




def main():
    nombre_archivo ="archivo.txt"
    registrar_datos(nombre_archivo, datos)


main()
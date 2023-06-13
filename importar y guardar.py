from main import automovil_particular, automovil_carga, bicicleta, motocicleta
import csv


def guardar_datos_csv(nombre_archivo, automovil_particular, automovil_carga, bicicleta, motocicleta):
    with open(nombre_archivo, "w", newline="") as archivo:
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerow(
            [automovil_particular.__class__.__name__, automovil_particular.__dict__])
        archivo_csv.writerow(
            [automovil_carga.__class__.__name__, automovil_carga.__dict__])
        archivo_csv.writerow(
            [bicicleta.__class__.__name__, bicicleta.__dict__])
        archivo_csv.writerow(
            [motocicleta.__class__.__name__, motocicleta.__dict__])

    print(f"\nLos datos se han guardado en el archivo {nombre_archivo}.\n")


# Ejemplo de uso
guardar_datos_csv('vehiculos.csv', automovil_particular,
                  automovil_carga, bicicleta, motocicleta)


def leer_datos_csv(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        for fila in archivo_csv:
            datos_fila = ', '.join(fila)
            print(datos_fila)


# Ejemplo de uso
leer_datos_csv('vehiculos.csv')

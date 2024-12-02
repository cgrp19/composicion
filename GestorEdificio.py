from ClaseDepartamento import Departamento
from ClaseEdificio import Edificio
import csv

class GestorEdificio:
    __listaedificios = list

    def __init__(self) -> None:
        self.__listaedificios = []

    def AgregarEdificio(self, unedificio):
        self.__listaedificios.append(unedificio)

    def CargaArchivo(self):
            with open("C:\\Users\\gasto\\.vscode\\POO\\Unidad 3\\Ejercicio 1 - Bien hecho\\EdificioNorte.csv") as archivo:
                reader = csv.reader(archivo, delimiter = ';')
                next(reader)
                for fila in reader:
                    if len(fila) == 7:
                        id = int(fila[1])
                        nom = fila[2]
                        dir = fila[3]
                        empcon = fila[4]
                        pisos = int(fila[5])
                        dep = int(fila[6])
                        unedificio = Edificio(id, nom, dir, empcon, pisos, dep)
                        self.AgregarEdificio(unedificio)
                    else:
                        id = int(fila[0])
                        due = int(fila[1])
                        nom = fila[2]
                        piso = int(fila[3])
                        depto = int(fila[4])
                        hab = int(fila[5])
                        baños = int(fila[6])
                        sup = float(fila[7])
                        Edificio.AgregarDepartamento(id, due, nom, piso, depto, hab, baños, sup)

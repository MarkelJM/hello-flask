import csv
from . import FICHERO

class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    

class ListaMovimiento:
    def __init__(self) :
        self.lista_movimiento = []

    def leer_archivo (self):
        with open(FICHERO, "r", encoding="UTF-8") as fichero:
            reader = csv.DictReader(fichero)
            for linea  in reader:
                self.lista_movimiento.append(linea)

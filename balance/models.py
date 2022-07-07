import csv
from datetime import date, datetime
from . import FICHERO

CLAVES_IGNORADAS: "errores"


class Movimiento:
    def __init__(self, datos):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(datos["fecha"])

            hoy = date.today()
            if self.fecha > hoy:
                self.errores.append("la fecha no puede ser futura")
        except ValueError:
            self.fecha = None
            self.errores.append("El formato de la fecha no es válido")

        self.concepto = datos["concepto"]
        self.tipo = datos["tipo"]
        self.cantidad = datos["cantidad"]

    def __str__(self):
        return "fecha: {} concepto: {} tipo: {} cantidad: {}".format(
            self.fecha,
            self.concepto,
            self.tipo,
            self.cantidad
        )


class ListaMovimiento:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r", encoding="UTF-8") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                mov = Movimiento(linea["fecha"], linea["concepto"],
                                 linea["tipo"], linea["cantidad"])
                self.movimientos.append(mov)

    def agregar(self, movimiento):
        self.movimientos.append(movimiento)
        self.guardar_archivo()

    def guardar_archivo(self):
        nombres = list(self.movimientos[0].__dict__.keys())
        for nombre in nombres:
            if nombre in CLAVES_IGNORADAS:
                nombres.remove(nombre)
        with open(FICHERO, "w") as fichero:
            writer = csv.DictWriter(fichero, nombres)
            writer.writeheader()
            for mov in self.movimientos:
                dic_mov = mov.__dict__
                for nombre in CLAVES_IGNORADAS:
                    dic_mov.pop(nombre, "")
                writer.writerow(dic_mov)

    def __str__(self):
        return f"Lista de {len(self.movimientos)} movimientos"

    def __repr__(self):
        return self.__str__()

from flask import render_template

from . import app
from.models import ListaMovimiento


@app.route('/')
def home():
    movimientos = ListaMovimiento()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)


@app.route('/nuevo')
def nuevo():
    return render_template("nuevo.html")


@app.route('/modificar')
def actualizar():
    return "actualizar movimiento"


@app.route('/borrar')
def borrar():
    return "borrar"

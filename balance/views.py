
from flask import render_template, request, redirect, url_for

from . import app
from.models import ListaMovimiento, Movimiento


@app.route('/')
def home():
    movimientos = ListaMovimiento()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'GET':
        return render_template("nuevo.html")
    else:
        datos = request.form
        nuevo_movimiento = Movimiento(datos)
        if len(nuevo_movimiento.errores ) > 0:
            return  f"Error en el nuevo movimiento.{nuevo_movimiento.errores}"

        # guardar archivo
        lista = ListaMovimiento()
        lista.leer_archivo()
        lista.agregar(nuevo_movimiento)
        return redirect(url_for("home"))

        


@app.route('/modificar')
def actualizar():
    return "actualizar movimiento"


@app.route('/borrar')
def borrar():
    return "borrar"

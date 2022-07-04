from flask import Flask

app = Flask(__name__)

#@ --> se les llama decorador
@app.route("/")
def hola():
    return "Hola, soy Flask. Y tú ¿cómo te llamas?"

@app.route("/adios")
def adios():
    return "hasta luego"
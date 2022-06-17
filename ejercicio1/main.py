from flask import Flask
import random
from datetime import datetime
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola'

@app.route("/dado")
def dado():
    return str(random.randint(1, 6))

@app.route('/fecha')
def fecha():
  inicio = datetime(1970, 1, 1)
  final = datetime(2100, 12, 31)
  return str(inicio + (final-inicio)*random.random())

@app.route('/color')
def color():
  colores = ["Rojo", "Verde", "Azul", "Marron", "Celeste", "Rosa", "Amarillo", "Violeta", "Negro", "Blanco", "Naranja"]

  return random.choice(colores)

@app.route('/dado/<n>')
def dadoN(n):
  n = int(n)
  if n > 0 and n < 11:
    final = ""
    for i in range (n):
      final = final + str(dado())
    return final
  else:
    return "n debe ser mayor que cero y menor que 11"

@app.route("/fecha/<y>")
def fechaY(y):
    y = int(y)
    inicio = datetime(y, 1, 1)
    final = datetime(y, 12, 31)

    random_date = inicio + (final - inicio) * random.random()

    return str(random_date)

@app.route("/fecha/<y>/<m>")
def fechaYM(y, m):
    y = int(y)
    m = int(m)
    if (m == 1 or m == 3 or  m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
      inicio = datetime(y, m, 1)
      final = datetime(y, m, 31)
    elif(m == 4 or m == 6 or m == 9 or m == 11):
      inicio= datetime(y,m,1)
      final= datetime(y,m,30)
    elif(m == 2):
      inicio = datetime(y,m,1)
      final = datetime(y,m,28)

    random_date = inicio + (final - inicio) * random.random()

    return str(random_date)

app.run(host='0.0.0.0', port=81)


from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/listado')
def listado ():
  conn = sqlite3.connect('co_emissions.db')
  q="""SELECT DISTINCT Country, Value 
       FROM emissions
       WHERE Series like "pcap"
       ORDER BY Value DESC LIMIT 10;"""
  return render_template('listado.html',
                          r = str(conn.execute(q).fetchall()),
                          a = 'hapy')

@app.route('/listado/top')
def listadoTotal ():
  conn = sqlite3.connect('co_emissions.db')
  q="""SELECT DISTINCT Country, Value 
       FROM emissions
       WHERE Series like "total"
       ORDER BY Value DESC LIMIT 10;"""
  return render_template('listadoTotal.html',
                          r = str(conn.execute(q).fetchall()))

@app.route('/listado/argentina')
def listadoPorPais ():
  conn = sqlite3.connect('co_emissions.db')
  q="""SELECT DISTINCT Country, value, Series
       FROM emissions
       WHERE Year like 2018;"""
  return render_template('listadoPorPais.html',
                          r = str(conn.execute(q).fetchall()))

@app.route('/ayuda')
def acercaDe ():
  
  return render_template('ayuda.html') 
  

app.run(host='0.0.0.0', port=81)
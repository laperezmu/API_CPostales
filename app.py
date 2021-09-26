# Python standard libraries
import json
from logging import DEBUG
import os

# Third party libraries
from flask import Flask, config, redirect, request, url_for, jsonify
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests
import mysql.connector


# Internal imports
# from db import init_db_command
# from user import User

db = mysql.connector.connect(
    host = 'localhost',
    user = 'meteorok',
    password = 'devSQL1',
    database = 'db_api'
)

cursor = db.cursor(dictionary=True)
app = Flask(__name__)





@app.route('/')
def index():
    return 'hola mundo'

def pagina_not_found(error):
    return "<h1>Pagina no disponible</h1>"

@app.route('/consulta/estados/<name>', methods= ['GET'])
def consultaEstados(name):
    query = "select * from estados where d_estado = '{0}'".format(name.replace("_", " "))
    cursor.execute(query)
    estados = cursor.fetchall()
    return jsonify(estados)

@app.route('/consulta/municipios/<name>', methods= ['GET'])
def consultaMunicipios(name):
    query = "select * from municipios where d_mnpio = '{0}'".format(name.replace("_", " "))
    cursor.execute(query)
    municipios= cursor.fetchall()
    return jsonify(municipios)

@app.route('/consulta/colonias', methods= ['GET'])
def consultaColonias():
    cursor.execute('select * from colonias2')
    colonias= cursor.fetchall()
    return jsonify(colonias)

@app.route('/consulta/<cp>', methods= ['GET'])
def consultaCP(cp):
    query = "select d_asenta, municipios.D_mnpio, estados.d_estado from colonias2 right join municipios on colonias2.fk_c_CP = municipios.c_CP \
             right join estados on municipios.fk_c_estado = estados.c_estado where d_codigo = '{0}'".format(cp)
    cursor.execute(query)
    datos = cursor.fetchall()
    return jsonify(datos)



if __name__ == "__main__":
    app.register_error_handler(404, pagina_not_found)
    app.run()



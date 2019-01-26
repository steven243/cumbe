#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:06:39 2019
@author: Cumbe
"""

from firebase import firebase
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from pyknow import * 

app = Flask(__name__)
Bootstrap(app)

def get_connection():
    data = firebase.FirebaseApplication('https://diagnostico-1f675.firebaseio.com/', None)
    return data
    

def get_Gripa():
    con = get_connection()
    dataset = con.get('/Enfermedades/0', None)
    return dataset
def get_GripaSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/0/Sintomas', None)
    return dataset

def get_Neumonia():
    con = get_connection()
    dataset = con.get('/Enfermedades/1', None)
    return dataset
def get_NeumoniaSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/1/Sintomas', None)
    return dataset

def get_Tuberculosis():
    con = get_connection()
    dataset = con.get('/Enfermedades/2', None)
    return dataset
def get_TuberculosisSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/2/Sintomas', None)
    return dataset

def get_Diabetes():
    con = get_connection()
    dataset = con.get('/Enfermedades/3', None)
    return dataset
def get_DiabetesSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/3/Sintomas', None)
    return dataset

def get_Gastritis():
    con = get_connection()
    dataset = con.get('/Enfermedades/4', None)
    return dataset
def get_GastritisSint():
    con = get_connection()
    dataset = con.get('/Enfermedades/4/Sintomas', None)
    return dataset

class Sintoma(Fact):
    pass

class Enfermedad(Fact):
    pass

Gripa = get_Gripa()
GripaSint = get_GripaSint()

e100 = Gripa['100']
s101 = GripaSint['101']
s102 = GripaSint['102']
s103 = GripaSint['103']
s104 = GripaSint['104']
s105 = GripaSint['105']


Neumonia = get_Neumonia()
NeumoniaSint = get_NeumoniaSint()

e200 = Neumonia['200']
s201 = NeumoniaSint['201']
s202 = NeumoniaSint['202']
s203 = NeumoniaSint['203']
s204 = NeumoniaSint['204']
s205 = NeumoniaSint['205']

Tuberculosis = get_Tuberculosis()
TuberculosisSint = get_TuberculosisSint()

e300 = Tuberculosis['300']
s301 = TuberculosisSint['301']
s302 = TuberculosisSint['302']
s303 = TuberculosisSint['303']
s304 = TuberculosisSint['304']
s305 = TuberculosisSint['305']

Diabetes = get_Diabetes()
DiabetesSint = get_DiabetesSint()

e400 = Diabetes['400']
s401 = DiabetesSint['401']
s402 = DiabetesSint['402']
s403 = DiabetesSint['403']
s404 = DiabetesSint['404']
s405 = DiabetesSint['405']

Gastritis = get_Gastritis()
GastritisSint = get_GastritisSint()

e500 = Gastritis['500']
s501 = GastritisSint['501']
s502 = GastritisSint['502']
s503 = GastritisSint['503']
s504 = GastritisSint['504']
s505 = GastritisSint['505']

class DiagnosticoEnfermedades(KnowledgeEngine):
    
            
    @Rule(Sintoma(descripcion= s101 and s102 or s103 or s104 or s105 or s504 or s304 or s202 or s303))
    def enfermedad_1(self):
        self.declare(Enfermedad(codigo=100, tipo=e100))  
        
        
        
    @Rule(Sintoma(descripcion= s201 and s202 or s203 or s204 or s205  or s301 or s504 or s303 or s102))
    def enfermedad_2(self):
        self.declare(Enfermedad(codigo=200, tipo=e200)) 
        
        
        
    @Rule(Sintoma(descripcion= s301 and s302 or s303 or s304 or s305 or s504 or s104 or s201 or s202))
    def enfermedad_3(self):
        self.declare(Enfermedad(codigo=300, tipo=e300)) 
        
        
        
    @Rule(Sintoma(descripcion= s401 and s402 or s403 or s404 or s405))
    def enfermedad_4(self):
        self.declare(Enfermedad(codigo=400, tipo=e400))
        
        
        
    @Rule(Sintoma(descripcion= s501 and s502 or s503 or s504 or s505 or s305 or s102 or s303 or s202))
    def enfermedad_5(self):
        self.declare(Enfermedad(codigo=500, tipo=e500)) 
        



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/diagnostico', methods=['POST'])
def Diagnostico():
    
    sinto1 = request.form['sint1']


    sinto2 = request.form['sint2']

    
    sinto3 = request.form['sint3']

    
    sinto4 = request.form['sint4']
        

    sinto5 = request.form['sint5']

    
    print('===============================================================================================')
    print(sinto1)
    print(sinto2)
    print(sinto3)
    print(sinto4)
    print(sinto5)
    print('===============================================================================================')
       
    watch('RULES', 'FACTS')
    diagnostico = DiagnosticoEnfermedades()
    diagnostico.reset()
    

    diagnostico.declare(Sintoma(descripcion=sinto1))
    diagnostico.declare(Sintoma(descripcion=sinto2))
    diagnostico.declare(Sintoma(descripcion=sinto3))
    diagnostico.declare(Sintoma(descripcion=sinto4))
    diagnostico.declare(Sintoma(descripcion=sinto5))

    
    diagnostico.run()
    enfermedad = diagnostico.facts

    for d in enfermedad:
        if (type(enfermedad[d]) == Enfermedad):
            tipo = enfermedad[d]['tipo']
            resultado = {'resul':tipo}
       

    return render_template('diagnostico.html', resultado=resultado)

    print(tipo)


if __name__ == '__main__':
    app.run()
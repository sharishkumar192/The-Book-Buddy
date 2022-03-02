from app import app
from flask import Flask, render_template, url_for

@app.route('/class11cbse_biology')
def class11cbse_biology():
    return render_template('cbse/11th/biology.html')

@app.route('/class11cbse_accountancy')
def class11cbse_accountancy():
    return render_template('cbse/11th/accountancy.html')

@app.route('/class11cbse_businessstudies')
def class11cbse_businessstudies():
    return render_template('cbse/11th/businessstudies.html')

@app.route('/class11cbse_chemistry')
def class11cbse_chemistry():
    return render_template('cbse/11th/chemistry.html')

@app.route('/class11cbse_economics')
def class11cbse_economics():
    return render_template('cbse/11th/economics.html')

@app.route('/class11cbse_maths')
def class11cbse_maths():
    return render_template('cbse/11th/maths.html')

@app.route('/class11cbse_physics')
def class11cbse_physics():
    return render_template('cbse/11th/physics.html')
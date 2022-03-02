from app import app
from flask import Flask, render_template, url_for

@app.route('/class12cbse_biology')
def class12cbse_biology():
    return render_template('cbse/12th/biology.html')

@app.route('/class12cbse_accountancy')
def class12cbse_accountancy():
    return render_template('cbse/12th/accountancy.html')

@app.route('/class12cbse_businessstudies')
def class12cbse_businessstudies():
    return render_template('cbse/12th/businessstudies.html')

@app.route('/class12cbse_chemistry')
def class12cbse_chemistry():
    return render_template('cbse/12th/chemistry.html')

@app.route('/class12cbse_economics')
def class12cbse_economics():
    return render_template('cbse/12th/economics.html')

@app.route('/class12cbse_maths')
def class12cbse_maths():
    return render_template('cbse/12th/maths.html')

@app.route('/class12cbse_physics')
def class12cbse_physics():
    return render_template('cbse/12th/physics.html')

@app.route('/class12cbse_english')
def class12cbse_english():
    return render_template('cbse/12th/english.html')
from app import app
from flask import Flask, render_template, url_for

@app.route('/class12state_economics')
def class12state_economics():
    return render_template('state/12th/economics.html')

@app.route('/class12state_botany')
def class12state_botany():
    return render_template('state/12th/botany.html')

@app.route('/class12state_zoology')
def class12state_zoology():
    return render_template('state/12th/zoology.html')

@app.route('/class12state_businessmaths')
def class12state_businessmaths():
    return render_template('state/12th/businessmaths.html')

@app.route('/class12state_chemistry')
def class12state_chemistry():
    return render_template('state/12th/chemistry.html')

@app.route('/class12state_commerce')
def class12state_commerce():
    return render_template('state/12th/commerce.html')

@app.route('/class12state_computerscience')
def class12state_computerscience():
    return render_template('state/12th/computerscience.html')

@app.route('/class12state_physics')
def class12state_physics():
    return render_template('state/12th/physics.html')

@app.route('/class12state_tamil')
def class12state_tamil():
    return render_template('state/12th/tamil.html')

@app.route('/class12state_english')
def class12state_english():
    return render_template('state/12th/english.html')
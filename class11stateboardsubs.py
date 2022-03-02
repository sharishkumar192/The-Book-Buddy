from app import app
from flask import Flask, render_template, url_for

@app.route('/class11state_accountancy')
def class11state_accountancy():
    return render_template('state/11th/accountancy.html')

@app.route('/class11state_botany')
def class11state_botany():
    return render_template('state/11th/botany.html')

@app.route('/class11state_zoology')
def class11state_zoology():
    return render_template('state/11th/zoology.html')

@app.route('/class11state_businessmaths')
def class11state_businessmaths():
    return render_template('state/11th/businessmaths.html')

@app.route('/class11state_chemistry')
def class11state_chemistry():
    return render_template('state/11th/chemistry.html')

@app.route('/class11state_commerce')
def class11state_commerce():
    return render_template('state/11th/commerce.html')

@app.route('/class11state_computerscience')
def class11state_computerscience():
    return render_template('state/11th/computerscience.html')

@app.route('/class11state_physics')
def class11state_physics():
    return render_template('state/11th/physics.html')

@app.route('/class11state_tamil')
def class11state_tamil():
    return render_template('state/11th/tamil.html')

@app.route('/class11state_english')
def class11state_english():
    return render_template('state/11th/english.html')
from app import app
from flask import Flask, render_template, url_for

@app.route('/eighthcbse')
def eighthcbse():
    return render_template('cbse/8th/8thcbse.html')

@app.route('/ninthcbse')
def ninthcbse():
    return render_template('cbse/9th/9thcbse.html')

@app.route('/tenthcbse')
def tenthcbse():
    return render_template('cbse/10th/10thcbse.html')

@app.route('/eleventhcbse')
def eleventhcbse():
    return render_template('cbse/11th/11thcbse.html')

@app.route('/twelfthcbse')
def twelfthcbse():
    return render_template('cbse/12th/12thcbse.html')
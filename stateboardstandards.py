from app import app
from flask import Flask, render_template, url_for

@app.route('/eighthstate')
def eighthstate():
    return render_template('state/8th/8thstate.html')

@app.route('/ninthstate')
def ninthstate():
    return render_template('state/9th/9thstate.html')

@app.route('/tenthstate')
def tenthstate():
    return render_template('state/10th/10thstate.html')

@app.route('/eleventhstate')
def eleventhstate():
    return render_template('state/11th/11thstate.html')

@app.route('/twelfthstate')
def twelfthstate():
    return render_template('state/12th/12thstate.html')
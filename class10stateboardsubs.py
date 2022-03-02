from app import app
from flask import Flask, render_template, url_for

@app.route('/class10state_english')
def class10state_english():
    return render_template('state/10th/english.html')

@app.route('/class10state_maths')
def class10state_maths():
    return render_template('state/10th/maths.html')

@app.route('/class10state_science')
def class10state_science():
    return render_template('state/10th/science.html')

@app.route('/class10state_social')
def class10state_social():
    return render_template('state/10th/social.html')

@app.route('/class10state_tamil')
def class10state_tamil():
    return render_template('state/10th/tamil.html')
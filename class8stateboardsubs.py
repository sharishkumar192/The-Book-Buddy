from app import app
from flask import Flask, render_template, url_for

@app.route('/class8state_english')
def class8state_english():
    return render_template('state/8th/english.html')

@app.route('/class8state_maths')
def class8state_maths():
    return render_template('state/8th/maths.html')

@app.route('/class8state_science')
def class8state_science():
    return render_template('state/8th/science.html')

@app.route('/class8state_social')
def class8state_social():
    return render_template('state/8th/social.html')

@app.route('/class8state_tamil')
def class8state_tamil():
    return render_template('state/8th/tamil.html')
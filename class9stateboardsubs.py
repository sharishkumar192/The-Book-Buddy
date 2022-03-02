from app import app
from flask import Flask, render_template, url_for

@app.route('/class9state_english')
def class9state_english():
    return render_template('state/9th/english.html')

@app.route('/class9state_maths')
def class9state_maths():
    return render_template('state/9th/maths.html')

@app.route('/class9state_science')
def class9state_science():
    return render_template('state/9th/science.html')

@app.route('/class9state_social')
def class9state_social():
    return render_template('state/9th/social.html')

@app.route('/class9state_tamil')
def class9state_tamil():
    return render_template('state/9th/tamil.html')
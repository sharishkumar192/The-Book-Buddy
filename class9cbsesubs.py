from app import app
from flask import Flask, render_template, url_for

@app.route('/class9cbse_englishmoments')
def class9cbse_englishmoments():
    return render_template('cbse/9th/englishmoments.html')

@app.route('/class9cbse_englishbeehive')
def class9cbse_englishbeehive():
    return render_template('cbse/9th/englishbeehive.html')

@app.route('/class9cbse_englishworkbook')
def class9cbse_englishworkbook():
    return render_template('cbse/9th/englishworkbook.html')

@app.route('/class9cbse_history')
def class9cbse_history ():
    return render_template('cbse/9th/history.html')

@app.route('/class9cbse_politicalscience')
def class9cbse_politicalscience ():
    return render_template('cbse/9th/politicalscience.html')

@app.route('/class9cbse_geography')
def class9cbse_geography ():
    return render_template('cbse/9th/geography.html')

@app.route('/class9cbse_economics')
def class9cbse_economics():
    return render_template('cbse/9th/economics.html')

@app.route('/class9cbse_maths')
def class9cbse_maths():
    return render_template('cbse/9th/maths.html')

@app.route('/class9cbse_science')
def class9cbse_science():
    return render_template('cbse/9th/science.html')


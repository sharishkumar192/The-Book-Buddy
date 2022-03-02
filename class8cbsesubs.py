from app import app
from flask import Flask, render_template, url_for

@app.route('/class8cbse_Social_and_Political_Life')
def class8cbse_Social_and_Political_Life():
    return render_template('cbse/8th/Social_and_Political_Life.html')

@app.route('/class8cbse_science')
def class8cbse_science():
    return render_template('cbse/8th/science.html')

@app.route('/class8cbse_resource_and_development')
def class8cbse_resource_and_development():
    return render_template('cbse/8th/resourceanddevelopment.html')

@app.route('/class8cbse_maths')
def class8cbse_maths():
    return render_template('cbse/8th/maths.html')

@app.route('/class8cbse_history')
def class8cbse_history():
    return render_template('cbse/8th/history.html')

@app.route('/class8cbse_english_it_so_happened')
def class8cbse_english_it_so_happened():
    return render_template('cbse/8th/englishitsohappened.html')

@app.route('/class8cbse_english_honey_dew')
def class8cbse_english_honey_dew():
    return render_template('cbse/8th/englishhoneydew.html')

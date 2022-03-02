from app import app
from flask import Flask, render_template, url_for

@app.route('/class10cbse_englishannefrank')
def class10cbse_englishannefrank():
    return render_template('cbse/10th/englishannefrank.html')

@app.route('/class10cbse_englishfirstflight')
def class10cbse_englishfirstflight():
    return render_template('cbse/10th/englishfirstflight.html')

@app.route('/class10cbse_englishfootprints')
def class10cbse_englishfootprints():
    return render_template('cbse/10th/englishfootprints.html')

@app.route('/class10cbse_englishhelenkeller')
def class10cbse_englishhelenkeller():
    return render_template('cbse/10th/englishhelenkeller.html')

@app.route('/class10cbse_englishliterature')
def class10cbse_englishliterature():
    return render_template('cbse/10th/englishliterature.html')

@app.route('/class10cbse_englishmaincourse')
def class10cbse_englishmaincourse():
    return render_template('cbse/10th/englishmaincourse.html')

@app.route('/class10cbse_history ')
def class10cbse_history ():
    return render_template('cbse/10th/history.html')

@app.route('/class10cbse_politicalscience')
def class10cbse_politicalscience ():
    return render_template('cbse/10th/politicalscience.html')

@app.route('/class10cbse_geography ')
def class10cbse_geography ():
    return render_template('cbse/10th/geography.html')

@app.route('/class10cbse_economics')
def class10cbse_economics():
    return render_template('cbse/10th/economics.html')

@app.route('/class10cbse_maths')
def class10cbse_maths():
    return render_template('cbse/10th/maths.html')

@app.route('/class10cbse_science')
def class10cbse_science():
    return render_template('cbse/10th/science.html')

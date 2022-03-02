from app import app
from flask import Flask, render_template, url_for
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cbsetextbook')
def cbsetextbook():
    return render_template('cbsetextbook.html')

@app.route('/stateboardtextbook')
def stateboardtextbook():
    return render_template('stateboardtextbook.html')

# CBSE Standards

from cbsestandards import *

# StateBoard Standards

from stateboardstandards import *

# CBSE Subjects 

from class8cbsesubs import *
from class9cbsesubs import *
from class10cbsesubs import *
from class11cbsesubs import *
from class12cbsesubs import *

# Stateboard Subjects 

from class8stateboardsubs import *
from class9stateboardsubs import *
from class10stateboardsubs import *
from class11stateboardsubs import *
from class12stateboardsubs import *
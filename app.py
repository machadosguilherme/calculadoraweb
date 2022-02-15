from asyncio.base_futures import _format_callbacks
import re

from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['POST', 'GET'])
def calculadora():
    vl1 = int(request.form['inpt1'])
    vl2 = int(request.form['inpt2'])
    opr = request.form['inpt3']
    
    if opr == 'soma':
        total = vl1 + vl2
        return render_template('index.html', total=total)
    elif opr == 'multiplicação':
        total = vl1 * vl2
        return render_template('index.html', total=total)
    elif opr == 'subtração':
        total = vl1 - vl2
        return render_template('index.html', total=total)
    elif opr == 'divisão':
        total = vl1 // vl2
        return render_template('index.html', total=total)
        
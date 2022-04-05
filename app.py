from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['POST', 'GET'])
def calculadora():
    vl1 = int(request.form['ipt1'])
    vl2 = int(request.form['ipt2'])
    opr = request.form['ipt3']
    
    if opr == 'soma':
        total = vl1 + vl2
        return render_template('index.html', total=total)
    elif opr == 'multiplicação':
        if vl2 < 0:
            return render_template('home.html')
        total = vl1 * vl2
        return render_template('index.html', total=total)
    elif opr == 'subtração':
        total = vl1 - vl2
        return render_template('index.html', total=total)
    elif opr == 'divisão':
        if vl2 == 0:
            return render_template('home.html')
        total = vl1 // vl2
        print('teste')
        return render_template('index.html', total=total)
        
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pickcolor', methods=['POST'])
def change_bg_color():
    session['red'] = int(request.form['red'])
    session['green'] = int(request.form['green'])
    session['blue'] = int(request.form['blue'])
    return redirect('/')

app.run(debug=True)
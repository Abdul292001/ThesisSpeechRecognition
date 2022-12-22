from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/', methods=['POST'])
def getvalue():
    speech = request.form('speech')
    return render_template('pass.html', s=speech)
    
    print(speech)
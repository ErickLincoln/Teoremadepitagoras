from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

    
if __name__ == '__main__':
        app.run(debug= True)

#irei realizar algumas integrações utilizando interfaces gráficas logo adiante.

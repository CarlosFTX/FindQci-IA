from flask import Flask, render_template, request
import ModuloIA

app = Flask(__name__)
data = []
prediccion = 0

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/dataObjeto', methods=['POST'])
def dataObjeto():
    if request.method == 'POST':
        data.clear()
        data.append(request.form['a'])
        data.append(request.form['b'])
        data.append(request.form['c'])
        data.append(request.form['d'])
        data.append(request.form['e'])
        prediccion, nombre, tipo, pic = ModuloIA.predictor(data)
        print(prediccion)
        return render_template('resultados.html', text=prediccion, name=nombre, tipo=tipo, pic=pic)

if __name__== '__main__':
    app.run(debug=True)

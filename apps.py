from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = None

    if request.method == 'POST':
        tasa = float(request.form['tasa'])
        periodos = int(request.form['periodos'])

        # Aquí agregas el cálculo de los factores financieros
        resultados = {
            'Tasa de interés': tasa,
            'Número de periodos': periodos,
            # Agrega más cálculos según necesites
        }

    return render_template('index.html', resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from calcu import calcular_factores  # Asegúrate de que este import sea correcto

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tasa_interes = float(request.form["tasa_interes"])
        num_periodos = int(request.form["num_periodos"])
        resultados = calcular_factores(tasa_interes, num_periodos)
        return render_template("index.html", resultados=resultados)
    return render_template("index.html", resultados=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


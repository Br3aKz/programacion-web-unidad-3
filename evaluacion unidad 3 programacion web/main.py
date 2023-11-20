from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3)
        aprobado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

        resultado = {'promedio': promedio, 'aprobado': aprobado}

    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encuentra el nombre más largo y su longitud
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        resultado = {'nombre_mas_largo': nombre_mas_largo, 'cantidad_caracteres': cantidad_caracteres}

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
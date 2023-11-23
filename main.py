from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def compras():
    if request.method == 'POST':
        valor_tarro = 9000
        cliente = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        if 18 <= edad <= 30:
            descuento = valor_tarro - (valor_tarro * 0.15)
        elif edad > 30:
            descuento = valor_tarro - (valor_tarro * 0.25)
        else:
            descuento = 0
        neto = tarros * valor_tarro
        total = neto - descuento
        return render_template('ejercicio1.html', cliente=cliente, neto=neto, descuento=descuento, total=total)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        if nombre == "juan" and password == "admin":
            tipo_usuario = "Administrador"
            return render_template('ejercicio2.html', tipo_usuario=tipo_usuario, nombre=nombre)
        elif nombre == "pepe" and password == "user":
            tipo_usuario = "Usuario"
            return render_template('ejercicio2.html', tipo_usuario=tipo_usuario, nombre=nombre)
        else:
            error = "Usuario o contraseña incorrectos"
            return render_template('ejercicio2.html', error=error)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
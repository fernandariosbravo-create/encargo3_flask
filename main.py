from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            n1 = float(request.form.get("nota1", "").strip())
            n2 = float(request.form.get("nota2", "").strip())
            n3 = float(request.form.get("nota3", "").strip())
            asistencia = float(request.form.get("asistencia", "").strip())

            # Validaciones según enunciado
            if not (10 <= n1 <= 70 and 10 <= n2 <= 70 and 10 <= n3 <= 70):
                raise ValueError("Las notas deben estar entre 10 y 70.")
            if not (0 <= asistencia <= 100):
                raise ValueError("La asistencia debe estar entre 0 y 100.")

            promedio = round((n1 + n2 + n3) / 3, 2)
            aprobado = (promedio >= 40) and (asistencia >= 75)

            resultado = {
                "promedio": promedio,
                "asistencia": asistencia,
                "estado": "APROBADO ✅" if aprobado else "REPROBADO ❌",
                "detalle": "Cumple promedio (≥40) y asistencia (≥75%)." if aprobado
                          else "No cumple promedio (≥40) y/o asistencia (≥75%)."
            }

        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Ocurrió un error. Revisa los datos ingresados."

    return render_template("ejercicio1.html", resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            nombre1 = request.form.get("nombre1", "").strip()
            nombre2 = request.form.get("nombre2", "").strip()
            nombre3 = request.form.get("nombre3", "").strip()

            if not (nombre1 and nombre2 and nombre3):
                raise ValueError("Debes ingresar 3 nombres.")
            if len({nombre1.lower(), nombre2.lower(), nombre3.lower()}) < 3:
                raise ValueError("Los 3 nombres deben ser diferentes.")

            nombres = [nombre1, nombre2, nombre3]
            largo_max = max(len(n) for n in nombres)
            nombre_mas_largo = next(n for n in nombres if len(n) == largo_max)

            # Si hay empate, informamos (sin perder el requisito)
            empatados = [n for n in nombres if len(n) == largo_max]
            empate_msg = None
            if len(empatados) > 1:
                empate_msg = f"Hay empate entre: {', '.join(empatados)}. Se muestra el primero."

            resultado = {
                "nombre": nombre_mas_largo,
                "cantidad": largo_max,
                "empate": empate_msg
            }

        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Ocurrió un error. Revisa los datos ingresados."

    return render_template("ejercicio2.html", resultado=resultado, error=error)


if __name__ == "__main__":
    app.run(debug=True)

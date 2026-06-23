from flask import Flask, jsonify, render_template, request
import numpy as np

app = Flask(__name__)

N_PUNTOS = 400
T_MAX = 60.0              # segundos simulados
N_ANOMALIAS = 6            # cantidad de ataques inyectados
UMBRAL_SIGMA_DEFAULT = 4.0  # umbral = media + UMBRAL_SIGMA * desviacion estandar de f'(t)


def generar_trafico():
    t = np.linspace(0, T_MAX, N_PUNTOS)

    # Trafico "normal": tendencia suave + estacionalidad + ruido gaussiano
    base = 50 + 10 * np.sin(2 * np.pi * t / 20) + 5 * np.sin(2 * np.pi * t / 5)
    ruido = np.random.normal(0, 1.5, size=t.shape)
    f = base + ruido

    # Inyeccion de anomalias: picos bruscos en instantes aleatorios
    indices_ataque = np.random.choice(range(10, N_PUNTOS - 10), size=N_ANOMALIAS, replace=False)
    for idx in indices_ataque:
        signo = np.random.choice([-1, 1])
        magnitud = np.random.uniform(25, 45)
        f[idx] += signo * magnitud

    return t, f


def derivada_numerica(t, f):
    # Diferencias finitas centradas: f'(t_i) = (f(t_i+1) - f(t_i-1)) / (t_i+1 - t_i-1)
    #Las diferencias finitas centradas son una fórmula que aproxima la derivada tomando el valor de antes y el valor de después de un punto, y dividiéndolos en dos.
    df = np.zeros_like(f)
    dt = t[1] - t[0]

    df[1:-1] = (f[2:] - f[:-2]) / (2 * dt)
    df[0] = (f[1] - f[0]) / dt          # diferencia adelantada en el borde inicial
    df[-1] = (f[-1] - f[-2]) / dt       # diferencia atrasada en el borde final

    return df


def detectar_anomalias(df, umbral):
    return np.where(np.abs(df) > umbral)[0]


def clasificar_severidad(valor_abs, umbral):
    # Severidad segun cuantas veces se supera el umbral
    razon = valor_abs / umbral
    if razon > 2.0:
        return "critica"
    if razon > 1.4:
        return "media"
    return "leve"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/datos")
def datos():
    umbral_sigma = request.args.get("umbral_sigma", UMBRAL_SIGMA_DEFAULT, type=float)

    t, f = generar_trafico()
    df = derivada_numerica(t, f)

    umbral = float(np.mean(np.abs(df)) + umbral_sigma * np.std(np.abs(df)))
    indices_anomalias = detectar_anomalias(df, umbral)

    eventos = [
        {
            "indice": int(idx),
            "tiempo": float(t[idx]),
            "valor_derivada": float(df[idx]),
            "severidad": clasificar_severidad(abs(float(df[idx])), umbral),
        }
        for idx in indices_anomalias
    ]

    return jsonify({
        "t": t.tolist(),
        "f": f.tolist(),
        "df": df.tolist(),
        "umbral": umbral,
        "umbral_sigma": umbral_sigma,
        "anomalias": indices_anomalias.tolist(),
        "eventos": eventos,
    })


if __name__ == "__main__":
    app.run(debug=True)

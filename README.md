# 🔍 Detección de Anomalías en Tráfico de Red

Proyecto académico desarrollado en 2026 para la **Evaluación 4 de Cálculo Diferencial** en INACAP, carrera Ingeniería en Ciberseguridad.

Este prototipo web simula tráfico de red y detecta anomalías tipo DDoS aplicando la **primera derivada matemática** mediante diferencias finitas centradas.

---

## 👥 Autores

**Matías Gajardo, Benjamín Cheuquemilla y Benjamín Mellado**

Trabajo realizado en conjunto como parte del proceso formativo en la asignatura de Cálculo Diferencial.

---

## 🧩 Descripción del proyecto

El sistema genera tráfico de red simulado como una función matemática **f(t)**, calcula su derivada **f'(t)** usando diferencias finitas centradas, y detecta anomalías cuando la tasa de cambio supera un **umbral estadístico ajustable**.

El tráfico normal incluye tendencia suave con oscilaciones periódicas y ruido gaussiano realista. Las anomalías se simulan como **picos bruscos aleatorios** que representan ataques tipo DDoS, y se clasifican automáticamente por severidad.

---

## ✨ Características principales

* 📈 Simulación de tráfico de red con función periódica + ruido gaussiano
* 🔢 Cálculo de derivada numérica por **diferencias finitas centradas**
* 🚨 Detección de anomalías cuando **|f'(t)| > media + σ × desviación estándar**
* 🟡 Clasificación de severidad: **leve**, **media** y **crítica**
* ⚙️ Umbral σ ajustable dinámicamente desde la interfaz web
* 🌐 Visualización interactiva en el navegador vía API REST

---

## 🔬 Base matemática

La derivada se aproxima con la fórmula de **diferencias finitas centradas**:

**f'(tᵢ) = ( f(tᵢ₊₁) − f(tᵢ₋₁) ) / ( tᵢ₊₁ − tᵢ₋₁ )**

El umbral de detección se calcula como:

**umbral = media(|f'(t)|) + σ × desviación_estándar(|f'(t)|)**

Un punto se marca como anomalía cuando **|f'(t)|** supera ese umbral. Mientras mayor sea σ, más estricta es la detección.

---

## 🛠️ Stack tecnológico

* Python 3
* Flask
* NumPy
* HTML, CSS, JavaScript

---

## 🚀 Puesta en marcha local

1. Clonar el repositorio.
2. Crear y activar entorno virtual.
3. Instalar dependencias.
4. Iniciar servidor.

Comandos sugeridos en Windows PowerShell:

```
python -m venv env
.\env\Scripts\Activate.ps1
pip install flask numpy
python app.py
```

Abrir en navegador:

* `http://127.0.0.1:5000/` — interfaz web principal
* `http://127.0.0.1:5000/api/datos` — endpoint REST con los datos simulados

---

## 🗂️ Estructura del proyecto

* `app.py` — lógica principal: simulación, derivada numérica y detección de anomalías
* `templates/` — plantillas HTML para la interfaz web

---

## 🎯 Contexto académico

Este repositorio corresponde a la **Evaluación 4 de Cálculo Diferencial**, donde el objetivo fue aplicar conceptos matemáticos reales en un problema concreto de ciberseguridad.

La idea central: si el tráfico de red **cambia demasiado rápido en un instante**, es señal de un comportamiento anómalo. Eso es exactamente lo que mide **f'(t)**.

---

## 📌 Nota

Este proyecto es un **prototipo académico funcional**. El tráfico es simulado y no proviene de una red real. Su valor principal es demostrar la **aplicación de derivadas numéricas** en un problema concreto de detección de intrusiones.

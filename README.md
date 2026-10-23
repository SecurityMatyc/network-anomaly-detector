# Detector de anomalías en tráfico de red

Prototipo web que simula tráfico de red y detecta cambios anómalos mediante derivadas numéricas y diferencias finitas centradas.

Proyecto académico desarrollado en **2026** para la **Evaluación 4 de Cálculo Diferencial** en INACAP, dentro de la carrera de Ingeniería en Ciberseguridad.

## Autores

- Matías Gajardo
- Benjamín Cheuquemilla
- Benjamín Mellado

Proyecto realizado en equipo como parte del proceso formativo en la asignatura de Cálculo Diferencial.

## Descripción del proyecto

El sistema genera tráfico de red simulado como una función matemática `f(t)`, calcula su derivada `f'(t)` mediante diferencias finitas centradas y marca posibles anomalías cuando la tasa de cambio supera un umbral estadístico.

El tráfico normal combina una tendencia suave, oscilaciones periódicas y ruido gaussiano. Las anomalías se representan mediante picos bruscos aleatorios asociados conceptualmente a comportamientos de tipo DDoS.

## Características principales

- Simulación de tráfico de red mediante una función periódica con ruido gaussiano.
- Cálculo de derivada numérica mediante diferencias finitas centradas.
- Detección de anomalías mediante un umbral basado en media y desviación estándar.
- Clasificación de severidad en niveles leve, medio y crítico.
- Ajuste dinámico del parámetro `σ` desde la interfaz web.
- Visualización de resultados en el navegador mediante una API REST.

## Base matemática

La derivada se aproxima mediante la fórmula de diferencias finitas centradas:

```text
f'(tᵢ) = (f(tᵢ₊₁) − f(tᵢ₋₁)) / (tᵢ₊₁ − tᵢ₋₁)
```

El umbral de detección se calcula como:

```text
umbral = media(|f'(t)|) + σ × desviación_estándar(|f'(t)|)
```

Un punto se clasifica como anomalía cuando `|f'(t)|` supera el umbral. Mientras mayor sea el valor de `σ`, más estricta será la detección.

## Tecnologías

- Python 3
- Flask
- NumPy
- HTML
- CSS
- JavaScript

## Puesta en marcha local

### 1. Crear y activar el entorno virtual

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```powershell
pip install flask numpy
```

### 3. Iniciar el servidor

```powershell
python app.py
```

## Rutas principales

| Ruta | Descripción |
|------|-------------|
| `http://127.0.0.1:5000/` | Interfaz web principal |
| `http://127.0.0.1:5000/api/datos` | Endpoint REST con datos simulados |

## Estructura del proyecto

- `app.py`: simulación, cálculo de derivada y detección de anomalías.
- `templates/`: plantillas HTML de la interfaz web.

## Contexto y limitaciones

Este repositorio corresponde a un prototipo académico funcional. El tráfico utilizado es simulado y no proviene de una red real. El objetivo es demostrar la aplicación de derivadas numéricas a un problema conceptual de ciberseguridad, no reemplazar una plataforma de monitoreo o detección de intrusiones en producción.

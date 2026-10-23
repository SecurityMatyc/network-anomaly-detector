# Detector de anomalías en tráfico de red

Prototipo web orientado al análisis experimental de tráfico de red simulado mediante derivadas numéricas y diferencias finitas centradas.

Proyecto académico desarrollado en **2026** para la **Evaluación 4 de Cálculo Diferencial** en INACAP, dentro de la carrera de Ingeniería en Ciberseguridad.

## Estado del proyecto

Prototipo académico funcional de alcance introductorio-intermedio. La aplicación demuestra un enfoque matemático para identificar cambios bruscos en una serie temporal de tráfico simulado.

No analiza paquetes ni captura tráfico de una red real. Su propósito es educativo y experimental.

## Problema y objetivo

En un escenario de monitoreo, un cambio repentino en el volumen de tráfico puede indicar un comportamiento anómalo. Este proyecto explora cómo la tasa de cambio de una función puede utilizarse como indicador inicial para detectar variaciones significativas.

El objetivo es:

- Generar tráfico de red sintético.
- Modelar variaciones normales y picos anómalos.
- Calcular la primera derivada numérica.
- Comparar la tasa de cambio con un umbral estadístico.
- Visualizar los resultados mediante una interfaz web.

## Autores

- Matías Gajardo
- Benjamín Cheuquemilla
- Benjamín Mellado

Proyecto realizado en equipo como parte del proceso formativo en la asignatura de Cálculo Diferencial.

## Flujo de análisis

1. Se genera una serie temporal de tráfico simulado.
2. Se incorporan tendencia, oscilaciones, ruido y picos anómalos.
3. Se calcula la primera derivada mediante diferencias finitas centradas.
4. Se obtiene un umbral a partir de la media y la desviación estándar.
5. Se marcan los puntos que superan el umbral.
6. La interfaz presenta los datos y la clasificación de severidad.

## Modelo de detección

### Derivada numérica

La derivada se aproxima mediante diferencias finitas centradas:

```text
f'(tᵢ) = (f(tᵢ₊₁) − f(tᵢ₋₁)) / (tᵢ₊₁ − tᵢ₋₁)
```

### Umbral estadístico

```text
umbral = media(|f'(t)|) + σ × desviación_estándar(|f'(t)|)
```

Un punto se considera anómalo cuando `|f'(t)|` supera el umbral calculado. El parámetro `σ` puede modificarse desde la interfaz para ajustar la sensibilidad del detector:

- Un valor menor identifica más variaciones como posibles anomalías.
- Un valor mayor hace más estricto el criterio de detección.

## Funcionalidades

- Simulación de tráfico con función periódica.
- Inclusión de ruido gaussiano.
- Generación de picos bruscos asociados conceptualmente a ataques DDoS.
- Cálculo de derivada numérica.
- Detección mediante media y desviación estándar.
- Clasificación de severidad en niveles leve, medio y crítico.
- Ajuste dinámico de `σ`.
- Visualización de resultados en el navegador.
- Consulta de datos mediante endpoint REST.

## Tecnologías

- Python 3
- Flask
- NumPy
- HTML
- CSS
- JavaScript

## Estructura del proyecto

- `app.py`: generación de tráfico, cálculo de derivadas y detección de anomalías.
- `templates/`: plantillas HTML de la interfaz web.

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

### 3. Iniciar la aplicación

```powershell
python app.py
```

## Rutas y API

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `http://127.0.0.1:5000/` | Interfaz web principal |
| `GET` | `http://127.0.0.1:5000/api/datos` | Datos simulados y resultados del análisis |

## Contexto académico

Este repositorio corresponde a la Evaluación 4 de Cálculo Diferencial. El proyecto permitió aplicar conceptos de derivadas numéricas y análisis de funciones a un problema conceptual relacionado con la ciberseguridad.

La idea central es que un cambio suficientemente rápido en el tráfico puede utilizarse como señal para iniciar un análisis más detallado.

## Limitaciones y posibles mejoras

El modelo no reemplaza una solución de monitoreo, un sistema de detección de intrusiones ni una plataforma SIEM. Sus principales limitaciones son:

- El tráfico es completamente simulado.
- No se procesan paquetes ni flujos de red reales.
- El umbral depende de un criterio estadístico simple.
- No existe correlación con eventos de autenticación, procesos o activos.
- No se implementan persistencia, alertas ni respuesta automática.

Como evolución futura, podría integrarse con datasets reales, series temporales persistidas, métricas de red, modelos estadísticos más robustos y mecanismos de alertamiento.

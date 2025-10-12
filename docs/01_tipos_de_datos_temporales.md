# 🕒 01. Tipos de Datos Temporales y Manejo de Fechas en Series Temporales

---

## 🎯 Objetivo
Entender los **tipos de datos temporales**, cómo manejar **fechas y frecuencias de tiempo** en Python (usando `pandas`) y cómo preparar correctamente tus datos para el análisis de series temporales.

---

## 🧩 ¿Qué son los datos temporales?

Los **datos temporales** son aquellos que cambian con el tiempo.  
Cada observación está **asociada a una fecha o momento específico** ⏰.

Por ejemplo:

| Fecha       | Temperatura (°C) |
|--------------|------------------|
| 2024-01-01   | 10.2             |
| 2024-01-02   | 11.5             |
| 2024-01-03   | 9.8              |

💡 Cada fila representa un punto en el tiempo.  
Este tipo de datos se usa para **observar tendencias, patrones y hacer predicciones**.

---

## 📆 Tipos de datos temporales

| Tipo de dato | Ejemplo | Descripción |
|---------------|----------|-------------|
| **Fecha simple** | `2024-10-01` | Día, mes y año |
| **Fecha y hora (timestamp)** | `2024-10-01 15:30:00` | Incluye hora exacta |
| **Intervalos de tiempo** | `2024-10-01` a `2024-10-07` | Un rango de tiempo |
| **Duración o diferencia temporal** | `7 días`, `3 horas` | Cuánto tiempo ha pasado entre dos fechas |

---

## ⏱️ Frecuencia temporal

La **frecuencia** indica cada cuánto se registra una observación:

| Frecuencia | Ejemplo | Descripción |
|-------------|----------|-------------|
| `A` (Anual) | 2020, 2021, 2022 | Datos de cada año |
| `Q` (Trimestral) | T1, T2, T3, T4 | Cuatro veces al año |
| `M` (Mensual) | Enero, Febrero... | 12 veces al año |
| `W` (Semanal) | Semana 1, Semana 2... | Cada semana |
| `D` (Diaria) | 2024-10-01, 2024-10-02... | Cada día |
| `H` (Hora) | 15:00, 16:00... | Cada hora |
| `T` o `min` (Minuto) | 15:00, 15:01... | Cada minuto |

🧠 *La frecuencia ayuda a detectar patrones: diarios, semanales, mensuales, etc.*

---

## 🐍 Tratando datos temporales en Python con `pandas`

### 1️⃣ Crear una serie temporal

```python
import pandas as pd

# Crear un rango de fechas
fechas = pd.date_range(start="2024-01-01", periods=7, freq="D")
valores = [10.2, 11.5, 9.8, 12.3, 11.1, 10.7, 9.9]

# Crear un DataFrame
df = pd.DataFrame({"fecha": fechas, "temperatura": valores})
print(df)

```
 ## 📊 Resultado:

| fecha      | temperatura |
| ---------- | ----------- |
| 2024-01-01 | 10.2        |
| 2024-01-02 | 11.5        |
| 2024-01-03 | 9.8         |
| ...        | ...         |
---
## 2️⃣ Convertir una columna a tipo fecha (datetime)

A veces las fechas vienen como texto (string).
Podemos convertirlas así:

```python
df["fecha"] = pd.to_datetime(df["fecha"])
print(df.dtypes)

```
📎 Resultado:
```python
fecha          datetime64[ns]
temperatura           float64


```

## 3️⃣ Establecer la fecha como índice temporal

Esto permite trabajar fácilmente con funciones de series temporales:

```python
df = df.set_index("fecha")
print(df.head())

```
4️⃣ Cambiar la frecuencia (resamplear)

Por ejemplo, si tus datos son diarios y quieres calcular la media semanal:

```python
df_semanal = df.resample("W").mean()
print(df_semanal)


```
## 📊 Visualización simple

Podemos visualizar nuestra serie temporal con matplotlib:

```python
import matplotlib.pyplot as plt

df.plot()
plt.title("🌡️ Temperatura diaria")
plt.ylabel("°C")
plt.xlabel("Fecha")
plt.show()

```
🖼️ Resultado:
Una línea que muestra cómo cambia la temperatura día a día.

💡 Ejemplo práctico para entenderlo mejor

Imagina que eres dueño de una heladería 🍦
y guardas las ventas diarias.
| Fecha      | Ventas (€) |
| ---------- | ---------- |
| 2024-06-01 | 200        |
| 2024-06-02 | 230        |
| 2024-06-03 | 180        |

Podrías analizar:

📈 Tendencias → ¿se venden más helados en verano?

🔁 Estacionalidad → ¿bajan las ventas en invierno?

🔮 Predicción → ¿cuánto venderé la próxima semana?

Todo eso se logra entendiendo los datos temporales y sus frecuencias.

---
### 📚 Resumen

| Concepto             | Descripción                                 |
| -------------------- | ------------------------------------------- |
| **Datos temporales** | Valores medidos en el tiempo                |
| **Frecuencia**       | Cada cuánto se registran los datos          |
| **Datetime**         | Formato especial para fechas                |
| **Resample**         | Cambiar frecuencia (diario → semanal, etc.) |
| **Visualización**    | Permite detectar patrones fácilmente        |


🚀 Tarea sugerida

Crea tu propio DataFrame con fechas y valores (por ejemplo, tus horas de estudio o pasos diarios).

Convierte las fechas al formato datetime.

Grafica tus datos y comenta si ves alguna tendencia o patrón.


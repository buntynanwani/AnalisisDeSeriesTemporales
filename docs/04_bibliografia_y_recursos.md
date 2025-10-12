# 📚 Bibliografía y Recursos sobre Series Temporales

Este documento recopila **libros, recursos online y ejemplos prácticos** para seguir aprendiendo sobre el análisis y visualización de series temporales.

Además, añadimos algunos ejemplos visuales sencillos (como los de la heladería 🍦 y supermercado 🛒) para practicar con datos reales o simulados.

---

## 📖 1️⃣ Libros Recomendados

| Libro | Autor | Nivel | Descripción |
|-------|--------|--------|--------------|
| *Introduction to Time Series and Forecasting* | Brockwell & Davis | Avanzado | Una referencia clásica para entender teoría y modelos ARIMA. |
| *Practical Time Series Analysis* | Aileen Nielsen | Intermedio | Enfocado en aplicaciones reales con Python. |
| *Forecasting: Principles and Practice* | Rob J. Hyndman | Básico - Intermedio | Muy didáctico y gratuito online. |
| *Python for Data Analysis* | Wes McKinney | Intermedio | Ideal para aprender a manipular series temporales con Pandas. |

---

## 🌍 2️⃣ Recursos Online Gratuitos

- 📘 **Forecasting: Principles and Practice (Hyndman)** → [https://otexts.com/fpp3/](https://otexts.com/fpp3/)
- 🧠 **Documentación oficial de Pandas - Series Temporales** → [https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
- 📊 **Curso gratuito de Machine Learning de Andrew Ng (Coursera)** → [https://www.coursera.org/learn/machine-learning](https://www.coursera.org/learn/machine-learning)
- 🐍 **Guía de Matplotlib y Seaborn para principiantes** → [https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)
- ⚡ **Plotly Express Gallery** → [https://plotly.com/python/plotly-express/](https://plotly.com/python/plotly-express/)

---

## 🧪 3️⃣ Ejemplo práctico: “Heladería y el cambio de temperatura” 🍦🌡️

Vamos a ver cómo la temperatura afecta a las ventas de helados usando tres bibliotecas visuales.

### 📊 Con Matplotlib

```python
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Temperatura (°C)': [10, 15, 20, 25, 30, 35],
    'Ventas de helado (€)': [100, 150, 300, 500, 700, 850]
}
df = pd.DataFrame(data)

plt.figure(figsize=(7,4))
plt.plot(df['Temperatura (°C)'], df['Ventas de helado (€)'], marker='o', color='orange')
plt.title('🍦 Relación entre temperatura y ventas de helado')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Ventas (€)')
plt.grid(True)
plt.show()
```

📈 **Conclusión:** a medida que sube la temperatura, ¡la gente compra más helados! 😄

---

### 🌈 Con Seaborn

```python
import seaborn as sns
sns.set(style="whitegrid")

plt.figure(figsize=(7,4))
sns.regplot(x='Temperatura (°C)', y='Ventas de helado (€)', data=df, color='coral')
plt.title('🍦 Relación temperatura vs ventas (Seaborn)')
plt.show()
```

🔍 Seaborn añade una **línea de tendencia automática**, ayudando a ver la relación directa entre las variables.

---

### ⚡ Con Plotly (interactivo)

```python
import plotly.express as px

fig = px.scatter(df, x='Temperatura (°C)', y='Ventas de helado (€)',
                 title='🍦 Ventas de helado vs Temperatura (Plotly)',
                 size='Ventas de helado (€)', color='Temperatura (°C)')
fig.show()
```

✨ **Plotly** te permite interactuar con el gráfico y explorar los datos dinámicamente.

---

## 🛒 4️⃣ Otro ejemplo: Ventas semanales en supermercado

```python
import matplotlib.pyplot as plt

dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
ventas = [400, 450, 500, 550, 900, 1000, 650]

plt.figure(figsize=(8,4))
plt.bar(dias, ventas, color='skyblue')
plt.title('🛒 Ventas semanales en supermercado')
plt.xlabel('Día')
plt.ylabel('Ventas (€)')
plt.show()
```

📊 Observamos que los picos de venta son los **viernes y sábados**, justo antes del fin de semana.

---

## 🧠 5️⃣ Recomendaciones para seguir aprendiendo

| Nivel | Tema | Recurso sugerido |
|--------|------|------------------|
| 🟢 Principiante | Introducción a Pandas y Matplotlib | [YouTube: freeCodeCamp.org](https://www.youtube.com/watch?v=vmEHCJofslg) |
| 🟡 Intermedio | Modelos ARIMA y ETS | [Kaggle Time Series Course](https://www.kaggle.com/learn/time-series) |
| 🔵 Avanzado | Deep Learning para series temporales | [TensorFlow Time Series Guide](https://www.tensorflow.org/tutorials/structured_data/time_series) |

---

## 🎯 Conclusión final

El aprendizaje de series temporales es como mirar el **pasado para predecir el futuro**.  
Cada gráfico, cada número, te cuenta una historia de cómo cambia el mundo con el tiempo. ⏳

Sigue explorando, visualizando y experimentando — así dominarás este fascinante campo. 🚀

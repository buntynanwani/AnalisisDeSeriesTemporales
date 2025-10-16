# 🎨 Visualización de Series Temporales en Python

La **visualización** es una de las partes más poderosas del análisis de series temporales. Nos permite **entender tendencias, patrones y anomalías** sin necesidad de fórmulas complicadas.

En este módulo aprenderás a representar tus datos en gráficos usando tres bibliotecas principales de Python:

- **Matplotlib** 📊
- **Seaborn** 🌈
- **Plotly** ⚡ (interactiva)

---

## 🕒 Ejemplo de contexto: la Heladería 🍦

Imagina que eres el dueño de una heladería y llevas un registro de las **ventas diarias durante todo el año**.  
Quieres saber:

- ¿Cuándo vendes más helados?  
- ¿Hay una tendencia creciente?  
- ¿Qué pasa en invierno? ❄️  

Los gráficos te ayudarán a descubrirlo rápidamente.

---

## 1️⃣ Visualización con Matplotlib 📊

```python
import matplotlib.pyplot as plt
import pandas as pd

# Simulamos las ventas de helados
datos = {
    'mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
    'ventas': [120, 150, 200, 300, 450, 600, 700, 750, 500, 300, 200, 150]
}

df = pd.DataFrame(datos)

# Gráfico básico
plt.figure(figsize=(8,4))
plt.plot(df['mes'], df['ventas'], marker='o', color='tomato')
plt.title('🍦 Ventas mensuales de helados')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()
```

📈 **Interpretación:** vemos que las ventas aumentan en verano (junio-agosto) y bajan en invierno.

---

## 2️⃣ Visualización con Seaborn 🌈

Seaborn nos permite hacer gráficos más estéticos con poco código.

```python
import seaborn as sns

sns.set(style="whitegrid")
plt.figure(figsize=(8,4))
sns.lineplot(data=df, x='mes', y='ventas', marker='o', color='coral')
plt.title('🍦 Ventas mensuales de helados (Seaborn)')
plt.show()
```

💡 Con Seaborn puedes añadir fácilmente colores, estilos y más información sin complicarte.

---

## 3️⃣ Visualización con Plotly ⚡ (Gráficos Interactivos)

Plotly permite crear gráficos que se pueden **mover, acercar o pasar el ratón por encima**.

```python
import plotly.express as px

fig = px.line(df, x='mes', y='ventas', title='🍦 Ventas mensuales de helados (Plotly)',
              markers=True, line_shape='spline')
fig.show()
```

✨ Ahora puedes interactuar con los puntos y observar cada valor. Ideal para presentaciones o dashboards.

---

## 🛒 Otro ejemplo: Ventas en un supermercado

Veamos cómo cambian las ventas **diarias** durante una semana.

```python
import pandas as pd
import matplotlib.pyplot as plt

dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
ventas = [500, 520, 540, 600, 800, 1000, 700]

df2 = pd.DataFrame({'día': dias, 'ventas': ventas})

plt.figure(figsize=(7,4))
plt.bar(df2['día'], df2['ventas'], color='skyblue')
plt.title('🛒 Ventas diarias en supermercado')
plt.xlabel('Día')
plt.ylabel('Ventas (€)')
plt.show()
```

📊 Observamos que las ventas suben los viernes y sábados — ¡la gente hace sus compras del fin de semana! 🛍️

---

## 🔍 Recomendaciones prácticas

| Situación | Biblioteca recomendada | Motivo |
|------------|-----------------------|---------|
| Gráficos simples y rápidos | **Matplotlib** | Control total y buena base |
| Gráficos más bonitos y fáciles | **Seaborn** | Colores y estilos automáticos |
| Gráficos interactivos | **Plotly** | Ideal para presentaciones y dashboards |

---

## 🧠 Conclusión

La visualización no solo **embellece tus datos**, sino que **revela historias ocultas**.  
Antes de aplicar modelos matemáticos o predicciones, **mira tus datos**. Ellos te contarán mucho más de lo que imaginas. 👀
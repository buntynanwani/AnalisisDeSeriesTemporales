# 🔮 02. Modelos de Series Temporales

---

## 🎯 Objetivo
Aprender los **principales modelos** que se usan para analizar y predecir series temporales:  
cómo funcionan, para qué sirven y cómo aplicarlos con ejemplos del día a día 🍦🛒⏰.

---

## 🧠 ¿Qué es un modelo de serie temporal?

Un **modelo** es una forma matemática o computacional que nos ayuda a:
- **Entender patrones** del pasado (tendencia, estacionalidad…),
- **Predecir valores futuros** 🔮,
- Y **tomar decisiones informadas** (por ejemplo, cuándo comprar más stock o ajustar precios).

---

## 📊 Ejemplo de la vida real

Imagina que tienes una **heladería 🍦**  
y anotas las ventas diarias durante un año.

Con esos datos puedes responder:
- ¿Vendo más en verano? ☀️  
- ¿Las ventas suben los fines de semana? 📅  
- ¿Puedo predecir cuántos helados venderé la próxima semana? 🔮  

Para eso usamos **modelos de series temporales**.

---

## ⚙️ Tipos de patrones en una serie temporal

| Tipo de patrón | Descripción | Ejemplo |
|----------------|-------------|----------|
| 📈 **Tendencia** | Dirección general de los datos (subida o bajada) | Las ventas aumentan cada año |
| ♻️ **Estacionalidad** | Patrones que se repiten periódicamente | Más ventas en verano o fines de semana |
| 🎲 **Ruido** | Variaciones aleatorias sin patrón claro | Un día llovió y hubo menos clientes |
| ⚡ **Ciclo** | Fluctuaciones más largas y suaves | Cambios económicos, estaciones, etc. |

---

## 🧩 Tipos de modelos más comunes

A continuación te presento los modelos más usados, explicados con ejemplos cotidianos 👇

---

### 1️⃣ Modelos **AR (AutoRegresivos)**

📖 **Idea básica:**  
El valor actual depende de los **valores pasados**.

📦 Ejemplo (supermercado 🛒):  
Si ayer vendiste muchas botellas de agua, hoy probablemente vendas una cantidad similar.

📊 Fórmula general:
```
Valor_hoy = α + β1 * Valor_ayer + β2 * Valor_anteayer + error
```

📦 **En Pandas/Statsmodels:**
```python
from statsmodels.tsa.ar_model import AutoReg

model = AutoReg(ventas, lags=1).fit()
pred = model.predict(start=len(ventas), end=len(ventas)+7)
```

---

### 2️⃣ Modelos **MA (Media Móvil / Moving Average)**

📖 **Idea básica:**  
El valor actual depende de los **errores pasados** (diferencias entre predicción y realidad).

🍦 Ejemplo (heladería):  
Si la semana pasada vendiste menos de lo esperado, el modelo ajusta la predicción de esta semana.

---

### 3️⃣ Modelos **ARMA (AR + MA)**

📖 **Idea básica:**  
Combina los dos anteriores.  
Sirve cuando los datos son **estacionarios** (sin tendencia clara a subir o bajar).

💡 *Estacionario = el comportamiento del tiempo no cambia mucho.*

---

### 4️⃣ Modelos **ARIMA (AutoRegressive Integrated Moving Average)**

📖 **Idea básica:**  
Perfecto cuando los datos **tienen tendencia o estacionalidad**.  
Incluye un paso para eliminar la tendencia antes de predecir.

🛒 **Ejemplo (supermercado):**  
Las ventas aumentan en diciembre cada año.  
ARIMA ajusta ese patrón para hacer predicciones más realistas.

🧮 Fórmula: ARIMA(p, d, q)
- `p`: número de términos autorregresivos (AR)
- `d`: número de diferenciaciones (para eliminar tendencia)
- `q`: número de términos de media móvil (MA)

📦 **En Python:**
```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(ventas, order=(1,1,1))
result = model.fit()
result.plot_predict(dynamic=False)
```

---

### 5️⃣ Modelos **SARIMA (ARIMA Estacional)**

📖 **Idea básica:**  
Es una versión de ARIMA que además tiene en cuenta los **patrones estacionales**,  
por ejemplo, los fines de semana o los meses de verano.

🍦 Ejemplo (heladería):
> Sabes que las ventas suben todos los sábados y domingos,  
> y bajan los lunes. SARIMA incorpora ese patrón directamente.

---

### 6️⃣ Modelos **Prophet (Facebook Prophet)** 🧙‍♂️

📖 **Idea básica:**  
Modelo desarrollado por **Meta (Facebook)** para manejar fácilmente **tendencias + estacionalidad + festivos**.  
Es muy útil para principiantes.

🛍️ Ejemplo (tienda online):
> Prophet puede aprender que los domingos las ventas bajan,  
> y que en Navidad suben muchísimo 🎄.

📦 **Ejemplo en Python:**
```python
from prophet import Prophet
import pandas as pd

df = pd.DataFrame({
    'ds': fechas,
    'y': ventas
})

model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
model.plot(forecast)
```

---

### 7️⃣ Modelos **LSTM (Redes Neuronales)** 🧠

📖 **Idea básica:**  
Una red neuronal diseñada para **recordar secuencias de datos**.  
Ideal para datos con muchos patrones complejos.

📈 Ejemplo (energía eléctrica ⚡):
> El consumo diario depende de la hora, el día de la semana, el clima, etc.  
> Un modelo LSTM puede aprender todos esos factores a la vez.

📦 Frameworks: `TensorFlow`, `Keras`, `PyTorch`.

---

## 🧮 Comparación de los principales modelos

| Modelo | Usa datos pasados | Usa errores | Usa estacionalidad | Ideal para |
|--------|--------------------|--------------|--------------------|-------------|
| AR | ✅ | ❌ | ❌ | Series simples |
| MA | ❌ | ✅ | ❌ | Suavizar ruido |
| ARMA | ✅ | ✅ | ❌ | Datos estacionarios |
| ARIMA | ✅ | ✅ | 🔸 | Series con tendencia |
| SARIMA | ✅ | ✅ | ✅ | Series con estacionalidad |
| Prophet | ✅ | ✅ | ✅ | Casos prácticos y fáciles |
| LSTM | ✅ | ✅ | ✅ | Grandes volúmenes y patrones complejos |

---

## 📊 Visualización conceptual

Ejemplo: **Ventas diarias en la heladería 🍦**

```
| Día        | Ventas (€) |
|-------------|------------|
| Lunes       | 180        |
| Martes      | 190        |
| Miércoles   | 200        |
| Jueves      | 210        |
| Viernes     | 300        |
| Sábado      | 500        |
| Domingo     | 480        |
```

📈 **Tendencia:** sube hacia el fin de semana.  
♻️ **Estacionalidad:** patrón semanal repetido.  
🎲 **Ruido:** un día llueve, y las ventas bajan sin razón aparente.

---

## 🚀 Conclusión

> Los modelos de series temporales nos permiten **comprender el pasado, analizar el presente y predecir el futuro** 📆.

✅ Usa modelos simples (AR, MA) para empezar.  
✅ Usa ARIMA o Prophet cuando veas tendencias o estacionalidad.  
✅ Usa LSTM cuando tengas muchos datos y relaciones complejas.

---

## 🧠 Ejercicio propuesto

1. Crea un pequeño conjunto de datos con tus horas de estudio diarias 📚.  
2. Grafícalo y detecta si hay tendencia (¿estudias más los fines de semana?).  
3. Aplica un modelo ARIMA o Prophet para predecir tus próximas horas de estudio.  

---

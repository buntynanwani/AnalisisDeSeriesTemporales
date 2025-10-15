# 📘 Análisis de Series Temporales  

---

## 🧩 1. ¿Qué es una Serie Temporal?

Una **serie temporal** es una secuencia de datos que se recogen **a lo largo del tiempo** a intervalos regulares.  
Cada punto representa una observación en un momento determinado.

📅 **Ejemplo sencillo:**
| Día | Temperatura (°C) |
|-----|-------------------|
| Lunes | 20 |
| Martes | 22 |
| Miércoles | 25 |
| Jueves | 24 |
| Viernes | 23 |

🧠 En este ejemplo, la variable *temperatura* cambia **con el tiempo**, y eso es lo que hace que sea una serie temporal.

---

## ⏳ 2. ¿Por qué el orden del tiempo es tan importante?

En una serie temporal, **el orden importa**.  
No puedes mezclar los datos, porque **cada valor depende del anterior**.

> Si cambias el orden del tiempo, ¡cambias la historia que cuentan los datos!

Ejemplo:
- En economía: el precio de hoy depende del precio de ayer.  
- En salud: los casos de gripe de hoy dependen de los días anteriores.  

---

## 🎯 3. ¿Para qué sirve el análisis de series temporales?

El objetivo es **entender el pasado, controlar el presente y predecir el futuro**.  

| 🧭 Aplicación | Qué analizamos | Qué queremos saber |
|---------------|----------------|--------------------|
| 🌦️ Meteorología | Temperaturas diarias | ¿Qué tiempo hará mañana? |
| 💰 Economía | Precio de acciones | ¿Subirá o bajará el valor? |
| 🚗 Transporte | Tráfico por hora | ¿Cuándo hay más congestión? |
| 🏥 Salud | Casos diarios de enfermedad | ¿Se está propagando más rápido? |
| 🏪 Negocios | Ventas mensuales | ¿Cuánto venderemos el próximo mes? |

---

## 💡 4. ¿Por qué es tan importante?

Porque casi todo lo que medimos en el mundo **cambia con el tiempo**.  
El análisis de series temporales nos ayuda a:

- 🔍 Detectar patrones o comportamientos.
- 📈 Predecir el futuro basándonos en datos pasados.
- ⚙️ Tomar mejores decisiones (cuándo invertir, producir, contratar…).
- 🚨 Detectar anomalías o cambios inesperados.

> “No podemos predecir el futuro, pero sí aprender de cómo se repite el pasado.”

---

## 📊 5. Componentes de una Serie Temporal

Cada serie está compuesta por **partes** que nos ayudan a entender su comportamiento.

| 🧩 Componente | 🔍 Qué representa | 🌍 Ejemplo cotidiano |
|---------------|------------------|----------------------|
| **Tendencia (Trend)** | Dirección general de los datos (sube o baja). | La temperatura sube poco a poco en verano. |
| **Estacionalidad (Seasonality)** | Patrones que se repiten de forma regular. | Ventas de helados suben en verano. |
| **Ciclo (Cycle)** | Cambios largos, no regulares. | Épocas de crisis y crecimiento económico. |
| **Ruido (Noise)** | Cambios aleatorios sin patrón. | Un día hace más calor sin razón aparente. |

🧠 Analizar una serie temporal es como **separar su música**:  
- La melodía (tendencia)  
- El ritmo (estacionalidad)  
- El ruido de fondo (ruido)

---

## 📘 6. Tipos de Series Temporales

| Tipo | Descripción | Ejemplo |
|------|--------------|----------|
| **Univariada** | Solo una variable cambia con el tiempo. | Temperatura diaria. |
| **Multivariada** | Varias variables evolucionan juntas. | Temperatura + humedad + viento. |
| **Estacionaria** | Su comportamiento no cambia con el tiempo. | Sensor de temperatura estable. |
| **No estacionaria** | Tiene tendencia o estacionalidad. | Ventas que aumentan cada año. |

---

## ⚙️ 7. Etapas del Análisis de Series Temporales

| Paso | Descripción | Ejemplo |
|------|--------------|----------|
| **1️⃣ Recolección** | Conseguir datos con fechas. | Ventas diarias del último año. |
| **2️⃣ Visualización** | Observar la evolución en el tiempo. | Graficar ventas vs tiempo. |
| **3️⃣ Limpieza** | Rellenar valores faltantes, eliminar errores. | Sustituir valores nulos por promedio. |
| **4️⃣ Modelado** | Aplicar un modelo (ARIMA, Prophet…). | Entrenar modelo con datos históricos. |
| **5️⃣ Predicción y evaluación** | Predecir el futuro y medir errores. | Estimar ventas del próximo mes. |

---

## 🤖 8. Modelos más comunes

### 🔹 1. **Modelos estadísticos**

| Modelo | Qué hace | Ejemplo sencillo |
|---------|-----------|------------------|
| **AR (Autoregresivo)** | Usa valores pasados para predecir el siguiente. | “Si ayer llovió, es probable que hoy también.” |
| **MA (Media móvil)** | Predice con el promedio de los últimos días. | “El precio será como el promedio de los últimos 3 días.” |
| **ARIMA** | Combina AR + MA + diferencias. | Predice ventas o inflación. |
| **SARIMA** | ARIMA con estacionalidad (patrones repetitivos). | Ventas que suben cada verano. |

---

### 🔹 2. **Modelos modernos (Machine Learning / IA)**

| Modelo | Qué hace | Ejemplo |
|---------|-----------|---------|
| **Prophet (Facebook)** | Modelo fácil de usar para detectar tendencia y estacionalidad. | Predice tráfico web diario. |
| **LSTM (Deep Learning)** | Aprende secuencias largas y dependencias complejas. | Predice consumo eléctrico hora a hora. |
| **XGBoost / RandomForest** | Usan árboles de decisión para predicción temporal. | Predicen demanda de taxis según hora y clima. |

---

## 📈 9. Ejemplo visual: Negocio de Helados 🍦

Imagina una tienda de helados que registra sus ventas cada mes.

📅 Enero → pocas ventas  
📅 Julio → muchas ventas  
📅 Diciembre → bajan otra vez  

➡️ Si graficas esto, verás un **patrón en forma de ola**.  
Eso es **estacionalidad** 🌊  

Además, si cada año vendes más, tienes una **tendencia ascendente** 📈.

👉 Con modelos como **SARIMA** o **Prophet**, podrías predecir:
> “¿Cuántos helados venderemos el próximo verano?”

---

## 🧠 10. Librerías de Python más usadas

| Librería | Función |
|-----------|----------|
| **Pandas** | Manejar y limpiar datos con fechas. |
| **Matplotlib / Seaborn** | Graficar la evolución temporal. |
| **Statsmodels** | Modelos estadísticos (ARIMA, SARIMA). |
| **Prophet** | Predicciones fáciles con tendencia y estacionalidad. |
| **Scikit-learn** | Machine Learning clásico. |
| **TensorFlow / Keras** | Redes neuronales como LSTM. |

---

## 🧩 11. Cómo enseñar series temporales de forma visual

- 📉 Usa **gráficos claros y coloridos**.  
- 📆 Explica con **ejemplos de la vida diaria** (clima, ventas, tráfico).  
- 🧩 Muestra **cómo separar tendencia, estacionalidad y ruido**.  
- 🧠 Haz que los alumnos **modifiquen valores** y vean cómo cambia el resultado.  
- 📚 Repite la idea: *“Los datos cuentan una historia en el tiempo.”*

Ejemplo:
> “Imagina que esta gráfica son tus pasos diarios.  
> Si un día caminas más, el gráfico sube; si caminas menos, baja.”

---

## 📚 12. Conclusión

El **análisis de series temporales** es una forma de mirar el tiempo con ojos de científico.  
Nos permite anticipar lo que viene, detectar patrones y tomar mejores decisiones.

> “Predecir el futuro no es magia...  
> es aprender del pasado con inteligencia.”

---

## 🧾 Créditos
- Elaborado por: **Bunty Nanwani y equipo**
- Proyecto educativo: *Formación en Análisis de Series Temporales con Python*
- Fecha: 2025

---

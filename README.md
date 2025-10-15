# 📊 Análisis de Series Temporales

<div align="center">

**Proyecto formativo para enseñar y aplicar técnicas de análisis de series temporales con Python**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

</div>

---

## 👥 Equipo de Desarrollo

- **Lady** - Desarrolladora
- **Noé Guamán** - Desarrollador
- **Bunty Nanwani** - Desarrollador

---

## 🎯 Objetivo del Proyecto

Este proyecto tiene como finalidad proporcionar un marco educativo completo para el **análisis de series temporales**, abarcando desde conceptos básicos hasta técnicas avanzadas de modelado y predicción. A través de notebooks interactivos, documentación detallada y scripts modulares, los usuarios podrán aprender y aplicar métodos estadísticos y de machine learning para trabajar con datos temporales.

---

## 📁 Estructura del Proyecto

```
ANALISISDESERIESTEMPORALES/
│
├── 📂 data/                    # Datasets del proyecto
│   ├── 📂 external/           # Datos externos de fuentes públicas
│   ├── 📂 processed/          # Datos procesados y limpios
│   └── 📂 raw/                # Datos en bruto sin procesar
│
├── 📂 docs/                    # Documentación teórica
│   ├── 00_resumen_analisis_series_temp.md
│   ├── 01_tipos_de_datos_temporales.md
│   ├── 02_metodos_y_modelos.md
│   ├── 03_metricas_evaluacion.md
│   ├── 04_bibliografia_y_recursos.md
│   └── newplot.png
│
├── 📂 notebooks/               # Notebooks interactivos de Jupyter
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_descomposicion_series.ipynb
│   ├── 03_modelos_ARIMA.ipynb
│   ├── 04_modelos_prophet.ipynb
│   ├── 05_prediccion_con_redes_LSTM.ipynb
│   └── 06_bibliografia_y_recursos.ipynb
│
├── 📂 results/                 # Resultados del análisis
│   ├── 📂 models/             # Modelos entrenados guardados
│   ├── 📂 plots/              # Gráficos y visualizaciones
│   └── 📂 summaries/          # Resúmenes de resultados
│
├── 📂 scripts/                 # Scripts Python modulares
│   ├── preprocessing.py       # Preprocesamiento de datos
│   ├── modeling.py            # Entrenamiento de modelos
│   ├── evaluation.py          # Evaluación de modelos
│   └── visualization.py       # Generación de visualizaciones
│
├── 📂 tests/                   # Pruebas unitarias
│   ├── test_preprocessing.py
│   ├── test_modeling.py
│   └── test_visualization.py
│
├── 📂 venv/                    # Entorno virtual (no incluido en Git)
├── .gitignore                  # Archivos ignorados por Git
├── .gitignore.example          # Ejemplo de configuración Git
├── estructuraProyecto.md       # Documentación de la estructura
├── README.md                   # Este archivo
└── requirements.txt            # Dependencias del proyecto
```

---

## ⚙️ Instalación y Configuración

### 📋 Requisitos Previos

- **Python 3.10 o superior**
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)

### 🚀 Pasos de Instalación

#### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/buntynanwani/AnalisisDeSeriesTemporales.git
cd AnalisisDeSeriesTemporales
```

#### 2️⃣ Crear y activar un entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Instalar las dependencias

```bash
pip install -r requirements.txt
```

#### 4️⃣ Ejecutar Jupyter Notebook

```bash
jupyter notebook
```

Luego navega a la carpeta **`notebooks/`** y abre el notebook que desees explorar.

---

## 📚 Librerías Principales

| Librería | Versión | Descripción |
|----------|---------|-------------|
| **pandas** | - | Manipulación y análisis de datos tabulares |
| **numpy** | - | Cálculos numéricos y operaciones con arrays |
| **matplotlib** | - | Visualizaciones estáticas 2D |
| **seaborn** | - | Visualizaciones estadísticas avanzadas |
| **plotly** | - | Gráficos interactivos y dashboards |
| **statsmodels** | - | Modelado estadístico y pruebas |
| **prophet** | - | Predicción automática de series temporales |
| **tensorflow** | - | Modelos de deep learning (LSTM, RNN) |
| **scikit-learn** | - | Machine learning y métricas de evaluación |
| **jupyter** | - | Entorno de notebooks interactivos |

---

## 📖 Documentación y Recursos

### 📝 Documentos Teóricos

Todos los documentos teóricos se encuentran en la carpeta **`docs/`**:

- **00_resumen_analisis_series_temp.md** - Introducción al análisis de series temporales
- **01_tipos_de_datos_temporales.md** - Tipos de datos y manejo de fechas
- **02_metodos_y_modelos.md** - Modelos estadísticos y de ML
- **03_metricas_evaluacion.md** - Métricas para evaluar modelos
- **04_bibliografia_y_recursos.md** - Referencias y recursos adicionales

### 🎓 Presentaciones

- [📊 Análisis de Series Temporales](https://gamma.app/docs/Analisis-de-Series-Temporales-g8tbf188izvr4wm)
- [📅 Tipos de Datos Temporales y Manejo de Fechas](https://gamma.app/docs/Tipos-de-Datos-Temporales-y-Manejo-de-Fechas-en-Series-Temporales-nk74xwds3e3ja98)
- [🤖 Modelos de Series Temporales](https://gamma.app/docs/Modelos-de-Series-Temporales-yxil4umglth1ion?mode=doc)
- [📚 Bibliografía y Recursos](https://gamma.app/docs/Bibliografia-y-Recursos-sobre-Series-Temporales-nt35p80oao03nm4?mode=doc)

---

## 🔍 Notebooks Disponibles

| Notebook | Descripción |
|----------|-------------|
| `01_exploracion_datos.ipynb` | Exploración inicial y análisis descriptivo |
| `02_descomposicion_series.ipynb` | Descomposición de tendencia, estacionalidad y residuos |
| `03_modelos_ARIMA.ipynb` | Implementación de modelos ARIMA/SARIMA |
| `04_modelos_prophet.ipynb` | Predicción con Facebook Prophet |
| `05_prediccion_con_redes_LSTM.ipynb` | Modelos de deep learning con LSTM |
| `06_bibliografia_y_recursos.ipynb` | Referencias y material complementario |

---

## ⚠️ Notas Importantes

### 🐍 Versión de Python
Se recomienda usar **Python 3.10 o superior** para garantizar la compatibilidad con todas las librerías.

### 📊 Visualizaciones con Plotly
Si los gráficos interactivos de **Plotly** no se muestran correctamente en Jupyter, añade al inicio del notebook:

```python
import plotly.io as pio
pio.renderers.default = "notebook"  # o "browser" si usas VSCode
```

### 🔧 Dependencias
Asegúrate de instalar todas las dependencias del archivo `requirements.txt` antes de ejecutar los notebooks o scripts.


---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 📧 Contacto

Para preguntas, sugerencias o colaboraciones, puedes contactar al equipo a través del repositorio de GitHub.

---

<div align="center">

**⭐ Si este proyecto te resulta útil, no olvides darle una estrella en GitHub ⭐**

</div>


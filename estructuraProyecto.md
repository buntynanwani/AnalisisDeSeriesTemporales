time_series_analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── 00_resumen_analisis_series_temporales.md
│   ├── 01_tipos_de_datos_temporales.md
│   ├── 02_metodos_y_modelos.md
│   ├── 03_metricas_evaluacion.md
│   └── 04_bibliografia_y_recursos.md
│
├── notebooks/
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_descomposicion_series.ipynb
│   ├── 03_modelos_ARIMA.ipynb
│   ├── 04_modelos_prophet.ipynb
│   ├── 05_prediccion_con_redes_LSTM.ipynb
│   └── utils/
│       └── funciones_auxiliares.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── external/
│   └── README.md
│
├── results/
│   ├── plots/
│   ├── summaries/
│   └── models/
│
├── scripts/
│   ├── preprocessing.py
│   ├── visualization.py
│   ├── modeling.py
│   └── evaluation.py
│
└── tests/
    ├── test_preprocessing.py
    ├── test_modeling.py
    └── test_visualization.py

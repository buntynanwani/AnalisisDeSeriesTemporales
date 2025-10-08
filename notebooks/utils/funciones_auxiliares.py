"""
Funciones auxiliares para los notebooks de análisis de series temporales.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series(df, column, title=""):
    """Grafica una serie temporal simple."""
    plt.figure(figsize=(10, 4))
    plt.plot(df[column], label=column)
    plt.title(title or column)
    plt.xlabel("Fecha")
    plt.ylabel("Valor")
    plt.legend()
    plt.show()

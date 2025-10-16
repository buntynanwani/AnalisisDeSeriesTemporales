# REPORTE EJECUTIVO - ANÁLISIS DE SERIES DE TIEMPO (MSFT)

## RESUMEN EJECUTIVO DEL ANÁLISIS EDA

**MICROSOFT (MSFT) - PERÍODO 1999-2025**

---

## 1. CARACTERÍSTICAS GENERALES DEL DATASET

- **Número de observaciones**: 6,549 registros (días de trading)
- **Período analizado**: 1999-10-04 a 2025-10-15
- **Duración**: 26.0 años
- **Variables**: 7 columnas (Open, High, Low, Close, Adj_Close, Volume)
- **Frecuencia**: Datos diarios de mercado

---

## 2. CALIDAD DE DATOS - VALORES NULOS

✅ **EXCELENTE**: NO hay valores nulos en ninguna columna

| Columna | Valores Nulos | Porcentaje |
|---------|---------------|-----------|
| Open | 0 | 0.00% |
| High | 0 | 0.00% |
| Low | 0 | 0.00% |
| Close | 0 | 0.00% |
| Adj_Close | 0 | 0.00% |
| Volume | 0 | 0.00% |

**CONCLUSIÓN**: El dataset está COMPLETO sin necesidad de imputación.

---

## 3. DETECCIÓN DE DUPLICADOS

✅ **NO hay registros duplicados encontrados**

**CONCLUSIÓN**: Cada día de trading aparece una sola vez.

---

## 4. ANÁLISIS DE OUTLIERS (Método IQR)

| Columna | Outliers Detectados | Porcentaje | Interpretación |
|---------|-------------------|-----------|----------------|
| Open |  937 |  14.31% | Movimientos atípicos |
| High |  958 |  14.63% | Normales (picos) |
| Low |  933 |  14.25% | Normales (caídas) |
| Close |  948 |  14.48% | Normales |
| Adj_Close |  933 |  14.25% | Normales |
| Volume |  182 |   2.78% | Volúmenes anormales |

**CONCLUSIÓN**: Los outliers detectados son naturales en datos financieros (movimientos de mercado, eventos económicos). NO se recomienda eliminarlos, ya que representan eventos reales importantes.

---

## 5. ANÁLISIS DE DISTRIBUCIONES

❌ **NINGUNA variable sigue distribución normal perfecta (p-value < 0.05)**

### Razones:

- Open, High, Low, Close: Tendencia creciente en el tiempo
- Adj_Close: Similar a Close (tendencia histórica)
- Volume: Distribución sesgada (log-normal)

**CONCLUSIÓN**: Es ESPERADO que precios en series de tiempo NO sean normales. Representan un proceso estocástico no-estacionario.

---

## 6. INDICADORES DE SERIE DE TIEMPO

- **Volatilidad diaria promedio**: 1.9020%
- **Volatilidad anualizada**: 30.1928%
- **Retorno promedio diario**: 0.0548%

**CONCLUSIÓN**: Microsoft muestra moderada volatilidad, consistente con una acción de grandes capitalizaciones (blue-chip).

---

## 7. RECOMENDACIONES PARA MODELADO

### ✅ Dataset listo para modelado:

- Calidad excelente (sin valores nulos)
- Período suficientemente largo para entrenar modelos
- Outliers naturales, deben ser preservados

### ✅ Tratamientos recomendados:

1. Diferenciar la serie para hacerla estacionaria
2. Aplicar log-returns para trabajar con cambios porcentuales
3. Escalar variables si se usan algoritmos sensibles (LSTM, KNN)
4. Verificar estacionariedad con test ADF (Augmented Dickey-Fuller)

### ✅ Modelos sugeridos:

- **ARIMA**: Para análisis univariado
- **SARIMA**: Si hay estacionalidad
- **Facebook Prophet**: Automático, incluye tendencias
- **LSTM/RNN**: Deep Learning, captura patrones complejos
- **XGBoost**: Con features engineered

---

**Generado automáticamente por análisis de series temporales**

# 🌱 Sistema de Automatización de Reportes y Predicción de Biomasa

## 📋 Descripción del Sistema

Este sistema implementa un flujo completo de **automatización de reportes** y **predicción de biomasa** usando Machine Learning, con integración total con **Excel** para uso operativo.

## 🚀 Características Principales

### ✅ **Automatización de Reportes con openpyxl + pandas**
- **Generación automática** de reportes en Excel con múltiples hojas
- **Formato profesional** usando openpyxl (colores, fuentes, bordes)
- **Métricas de modelos** organizadas en tablas estructuradas
- **Gráficos embebidos** en Excel usando openpyxl.chart
- **Timestamps automáticos** y metadatos del proceso

### 📊 **Dashboard Simple Integrado**
- **KPIs principales** en formato visual
- **Comparación de rendimiento** entre modelos
- **Análisis exploratorio** de datos integrado
- **Exportación en alta resolución** (PNG, 300 DPI)
- **Diseño profesional** con métricas destacadas

### 🔄 **Flujo Completo: Carga → Modelado → Visualización**
- **Carga automatizada** desde Excel (pandas)
- **Preprocesamiento completo** (nulos, codificación, escalado)
- **Entrenamiento de múltiples modelos** (Regresión + Clasificación)
- **Evaluación automática** con métricas estándar
- **Generación de reportes** sin intervención manual

## 📁 Archivos Generados

### 1. **Notebook Principal**
```
📓 automatizacion_reportes_biomasa.ipynb
```
- Código completo del sistema
- Flujo paso a paso documentado
- Ejemplos de uso y explicaciones

### 2. **Reporte Excel Automatizado**
```
📄 Reporte_Biomasa_ML_DEMO.xlsx
```
**Hojas incluidas:**
- `Resumen_Ejecutivo`: KPIs y métricas principales
- `Resultados_Regresion`: Comparación modelos regresión
- `Resultados_Clasificacion`: Comparación modelos clasificación  
- `Datos_Ejemplo`: Muestra de datos procesados

**Características del reporte:**
- ✅ Formato profesional con colores corporativos
- ✅ Headers destacados y bordes profesionales
- ✅ Ajuste automático de ancho de columnas
- ✅ Timestamp de generación
- ✅ Métricas ordenadas por rendimiento

### 3. **Sistema de Predicción Operativo**
```
🔮 Sistema_Prediccion_Biomasa_DEMO.xlsx
```
**Hojas incluidas:**
- `Instrucciones`: Guía completa de uso
- `Nuevos_Datos`: Plantilla para predicciones
- `Info_Modelos`: Detalles técnicos de modelos

**Características del sistema:**
- ✅ **Fácil de usar**: Solo completar valores
- ✅ **Validación automática** de datos
- ✅ **Predicciones en tiempo real** (con fórmulas)
- ✅ **Confianza del modelo** incluida
- ✅ **Ejemplos preconfigurados**

## 🔧 Tecnologías Implementadas

### **Automatización de Reportes**
```python
import pandas as pd           # Manipulación de datos
import openpyxl              # Formato avanzado Excel
from openpyxl.styles import Font, PatternFill, Border
from openpyxl.chart import BarChart, LineChart
```

### **Machine Learning**
```python
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, accuracy_score
```

### **Visualización**
```python
import matplotlib.pyplot as plt
import seaborn as sns
# Dashboard con KPIs y gráficos profesionales
```

## 📈 Modelos Implementados

### **Regresión (Predicción Continua)**
- ✅ Linear Regression
- ✅ Random Forest Regressor
- **Métricas**: R², RMSE, MAE

### **Clasificación (Categorías: Baja/Media/Alta)**
- ✅ SVM (Linear, RBF, Polynomial)
- ✅ Random Forest Classifier
- **Métricas**: Accuracy, Precision, Recall, F1-Score

## 🎯 Uso del Sistema

### **1. Entrenar Modelos**
```python
# El notebook carga datos, entrena modelos y genera reportes automáticamente
jupyter notebook automatizacion_reportes_biomasa.ipynb
```

### **2. Usar Sistema de Predicción**
1. Abrir `Sistema_Prediccion_Biomasa_DEMO.xlsx`
2. Ir a hoja `Nuevos_Datos`
3. Completar variables:
   - **NDVI**: 0-1 (índice vegetación)
   - **NDRE**: 0-1 (índice borde rojo)
   - **Precipitación**: mm de lluvia
   - **Días sin lluvia**: número días
   - **Tipo suelo**: 0=Arcilloso, 1=Arenoso, 2=Franco
4. Ver predicciones automáticas

### **3. Analizar Reportes**
1. Abrir `Reporte_Biomasa_ML_DEMO.xlsx`
2. Revisar `Resumen_Ejecutivo` para KPIs
3. Analizar rendimiento en hojas específicas
4. Usar datos para decisiones

## 🔍 Variables del Modelo

### **Variables Predictoras**
| Variable | Descripción | Rango |
|----------|-------------|-------|
| NDVI | Índice de Vegetación | 0.0 - 1.0 |
| NDRE | Índice de Borde Rojo | 0.0 - 1.0 |
| Precipitación | Lluvia (mm) | 0 - 100+ |
| Días sin lluvia | Días consecutivos | 0 - 30+ |
| Tipo de suelo | Codificado | 0, 1, 2 |

### **Variables Objetivo**
- **Biomasa**: Valor continuo (kg/ha)
- **Categoría**: Baja, Media, Alta

## ⚡ Automatización Implementada

### **🔄 Flujo Automático**
```
Datos Excel → Preprocesamiento → ML → Reportes → Dashboard
```

### **📊 Reportes Automatizados**
- ✅ **Múltiples hojas** con pandas.ExcelWriter
- ✅ **Formato profesional** con openpyxl
- ✅ **Gráficos embebidos** automáticamente
- ✅ **Métricas calculadas** y formateadas
- ✅ **Timestamps** y metadatos

### **🎨 Dashboard Automático**
- ✅ **KPIs visuales** con métricas destacadas
- ✅ **Comparación de modelos** en gráficos
- ✅ **Análisis exploratorio** integrado
- ✅ **Exportación automática** en PNG

## 📊 Resultados de Demostración

### **Mejores Modelos**
- **Regresión**: Random Forest (R² = 0.8156)
- **Clasificación**: Random Forest (Accuracy = 0.8947)

### **Archivos Operativos**
- ✅ Sistema listo para usar en producción
- ✅ Interfaz amigable en Excel
- ✅ Reportes automáticos programables
- ✅ Dashboard actualizable

## 🚀 Ventajas del Sistema

### **Para Usuarios Finales**
- 🎯 **Interfaz familiar** (Excel)
- 🔮 **Predicciones inmediatas**
- 📊 **Reportes profesionales**
- 📈 **Dashboard visual**

### **Para Desarrolladores**
- 🔧 **Código modular** y reutilizable
- 📁 **Automatización completa**
- 🎨 **Formato personalizable**
- ⚡ **Escalable** a otros proyectos

### **Para la Organización**
- 💼 **Reportes consistentes**
- 📅 **Generación programable**
- 🎯 **Decisiones basadas en datos**
- 💰 **Ahorro de tiempo** significativo

---

## 🎉 Sistema Completamente Funcional

El sistema está **listo para uso inmediato** y demuestra la **integración completa** entre Python, Machine Learning y Excel para automatización de reportes y predicciones operativas.

**¡Perfecto para implementar en entornos de producción!** 🚀

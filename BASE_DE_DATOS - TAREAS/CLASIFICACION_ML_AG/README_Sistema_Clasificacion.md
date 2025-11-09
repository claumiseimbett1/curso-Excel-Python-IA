# Sistema de Clasificación de Biomasa en Excel

## 📋 Descripción

Sistema completo para clasificar biomasa en categorías (Baja, Media, Alta) usando modelos de Machine Learning. Los usuarios pueden ingresar datos en Excel y obtener clasificaciones automáticas.

**Categorías de Biomasa:**
- 🟢 **Alta**: Producción alta de biomasa
- 🟡 **Media**: Producción media de biomasa
- 🔴 **Baja**: Producción baja de biomasa

## 🎯 Características

- ✅ Clasificación automática usando el mejor modelo entrenado
- ✅ Interfaz simple: solo Excel
- ✅ Clasificaciones escritas en el mismo archivo
- ✅ Codificación visual por colores
- ✅ Métricas de confianza (cuando están disponibles)
- ✅ Validación automática de datos

## 📂 Archivos del Sistema

### Scripts Principales
```
├── 0_clasificacion_biomasa_ml.ipynb         # Notebook con entrenamiento de modelos
├── 1_guardar_modelo_clasificacion.py        # Guardar modelo entrenado
├── 2_crear_plantilla_excel_clasificacion.py # Crear plantilla Excel
├── 3_predecir_en_excel_clasificacion.py     # Clasificación automática
├── predictor_simple_clasificacion.py        # Clasificación simplificada
```

### Archivos Generados
```
├── best_model_clasificacion.pkl             # Modelo de clasificación
├── scaler_clasificacion.pkl                 # Escalador
├── label_encoder_clasificacion.pkl          # Codificador de clases
├── model_info_clasificacion.json            # Información del modelo
└── Plantilla_Clasificacion_Biomasa.xlsx     # Plantilla Excel
```

## 🚀 Inicio Rápido

### 1. Entrenar y Guardar el Modelo

Desde el notebook `0_clasificacion_biomasa_ml.ipynb`, al final agrega una celda:

```python
%run 1_guardar_modelo_clasificacion.py
```

### 2. Crear Plantilla Excel

```bash
python3 2_crear_plantilla_excel_clasificacion.py
```

### 3. Clasificar Datos

**Método Simple (Recomendado):**

1. Llena `Plantilla_Clasificacion_Biomasa.xlsx` con tus datos
2. Guarda y cierra el Excel
3. Ejecuta:
   ```bash
   python3 3_predecir_en_excel_clasificacion.py
   ```
4. Abre el Excel para ver las clasificaciones (con colores)

## ⚙️ Variables Requeridas

El modelo requiere las mismas variables que el modelo de regresión:

1. **NDVI Outlier Manual** - Índice de Vegetación (0-1)
2. **NDRE Outlier Manual** - Índice de Borde Rojo (0-1)
3. **PRECIPITACION Outlier Manual** - Precipitación en mm
4. **DIAS SIN LLUVIA Estadistica** - Días consecutivos sin lluvia
5. **Tipo_suelo** - Tipo de suelo (Arenoso, Arcilloso, Franco)

## 💻 Clasificación desde Python

```python
from predictor_simple_clasificacion import clasificar_valores_directos

categoria = clasificar_valores_directos(
    NDVI_Outlier_Manual=0.75,
    NDRE_Outlier_Manual=0.65,
    PRECIPITACION_Outlier_Manual=120.5,
    DIAS_SIN_LLUVIA_Estadistica=5,
    Tipo_suelo='Franco'
)

print(f"Categoría predicha: {categoria}")  # Ej: "Alta", "Media", "Baja"
```

## 📊 Interpretación de Resultados

El sistema clasifica cada muestra en una de las tres categorías y utiliza colores para facilitar la interpretación:

- **🟢 Verde (Alta)**: Condiciones óptimas para producción de biomasa
- **🟡 Amarillo (Media)**: Condiciones moderadas
- **🔴 Rojo (Baja)**: Condiciones que limitan la producción

Si el modelo lo permite, también se muestra la confianza de cada predicción.

## 🔄 Hacer Nuevas Clasificaciones

1. Abre el Excel
2. Agrega o modifica datos
3. Guarda el archivo
4. Ejecuta: `python3 3_predecir_en_excel_clasificacion.py`
5. Abre el Excel para ver resultados

## ❓ Diferencias con el Sistema de Regresión

| Característica | Regresión | Clasificación |
|----------------|-----------|---------------|
| Salida | Valor numérico (kg/ha) | Categoría (Baja/Media/Alta) |
| Métrica principal | R², RMSE | Accuracy, F1-Score |
| Visualización | Números con fondo verde | Colores: Verde/Amarillo/Rojo |
| Uso | Predicción exacta | Clasificación rápida |
| Mejor para | Análisis cuantitativo | Decisiones rápidas |

## 🐛 Solución de Problemas

### ❌ "No se encuentra best_model_clasificacion.pkl"
**Solución:** Ejecuta desde el notebook: `%run 1_guardar_modelo_clasificacion.py`

### ❌ "No hay datos para clasificar"
**Solución:** Llena al menos una fila completa en el Excel

### ❌ Error al leer Excel
**Solución:**
- Cierra Excel antes de ejecutar el script
- Verifica que no modificaste los encabezados

### ❌ Clasificaciones incorrectas
**Solución:**
- Verifica que los datos estén en las unidades correctas
- Tipo_suelo debe ser exactamente: "Arenoso", "Arcilloso" o "Franco"
- NDVI y NDRE deben estar entre 0 y 1

## 📊 Métricas del Modelo

El sistema guarda automáticamente en `model_info_clasificacion.json`:

- **Accuracy**: Porcentaje de clasificaciones correctas
- **Precision**: Precisión por clase
- **Recall**: Sensibilidad por clase
- **F1-Score**: Métrica combinada
- **Clases**: Lista de categorías posibles
- **Fecha de entrenamiento**
- **Hiperparámetros del mejor modelo**

## 📝 Notas Técnicas

- **Lenguaje:** Python 3.6+
- **Librerías:** pandas, numpy, scikit-learn, openpyxl
- **Compatibilidad:** Windows, macOS, Linux
- **Tipo de problema:** Clasificación multiclase (3 categorías)
- **Codificación:** LabelEncoder para clases, StandardScaler para features

## 🎯 Resumen de Flujo de Trabajo

```
1. Notebook: Entrenar modelos de clasificación
2. Script 1:  Guardar el mejor modelo
3. Script 2:  Crear plantilla Excel
4. Usuario:   Llenar datos en Excel
5. Script 3:  Clasificar y escribir resultados
6. Usuario:   Ver clasificaciones con colores
```

## 📞 Archivos Necesarios para Clasificar

Para hacer clasificaciones solo necesitas:
- `best_model_clasificacion.pkl`
- `scaler_clasificacion.pkl`
- `label_encoder_clasificacion.pkl`
- `model_info_clasificacion.json`
- `3_predecir_en_excel_clasificacion.py` o `predictor_simple_clasificacion.py`
- `Plantilla_Clasificacion_Biomasa.xlsx`

---

**¡Sistema completo de clasificación de biomasa listo para usar!** 🎉

*Última actualización: 2025-10-25*

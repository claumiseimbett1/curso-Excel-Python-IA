# Cambios Realizados - Regresión de Consumo Energético

## Resumen
Se ha actualizado todo el sistema de predicción para trabajar con el dataset de **Paneles Solares** y predecir **Consumo_kWh_Mensual** en lugar de Biomasa.

---

## Dataset Actualizado

### Archivo Excel
- **Anterior**: `Base_Prediccion_Biomasa_Outliers1.xlsx`
- **Nuevo**: `Paneles_solares_con_outliers.xlsx`
- **Hoja**: `Datos Limpios`

### Columnas del Nuevo Dataset
1. **ID_Cliente** - Identificador único
2. **Sector** - Residencial, Comercial, Industrial
3. **Consumo_kWh_Mensual** - ⭐ **VARIABLE OBJETIVO**
4. **Estrato** - Nivel socioeconómico (1-6)
5. **Ciudad** - Ciudad del cliente
6. **Area_m2** - Área en metros cuadrados
7. **Factura_Mensual_COP** - Factura mensual (excluida por correlación con objetivo)
8. **Puede_Pagar_Solar** - Sí/No
9. **Validar** - VALIDO (columna de control)

### Variables Predictoras
Después de eliminar columnas no relevantes:
- Sector
- Estrato
- Ciudad
- Area_m2
- Puede_Pagar_Solar

---

## Archivos Modificados

### 1. `2_crear_plantilla_excel.py`
**Cambios principales:**
- Nombre de archivo: `Plantilla_Prediccion_Biomasa.xlsx` → `Plantilla_Prediccion_Consumo.xlsx`
- Columna de predicción: `Biomasa_Predicha` → `Consumo_kWh_Mensual_Predicho`
- Título: "PLANTILLA DE PREDICCIÓN DE BIOMASA" → "PLANTILLA DE PREDICCIÓN DE CONSUMO ENERGÉTICO"
- Ejemplos de datos actualizados para el nuevo dataset (Sector, Estrato, Ciudad, Area_m2, Puede_Pagar_Solar)

### 2. `3_predecir_en_excel.py`
**Cambios principales:**
- Nombre de archivo: `Plantilla_Prediccion_Biomasa.xlsx` → `Plantilla_Prediccion_Consumo.xlsx`
- Columna de predicción: `Biomasa_Predicha` → `Consumo_kWh_Mensual_Predicho`
- Título del sistema: "SISTEMA DE PREDICCIÓN DE BIOMASA" → "SISTEMA DE PREDICCIÓN DE CONSUMO ENERGÉTICO"
- **Codificación de variables categóricas actualizada:**
  ```python
  sector_map = {'Residencial': 0, 'Comercial': 1, 'Industrial': 2}
  ciudad_map = {'Montería': 0, 'Sahagún': 1, 'Planeta Rica': 2, 'Cereté': 3, 'Lorica': 4}
  puede_pagar_map = {'No': 0, 'Sí': 1, 'Si': 1}
  ```

### 3. `4_crear_excel_con_boton.py`
**Cambios principales:**
- Nombre de archivo: `Plantilla_Prediccion_Con_Boton.xlsx` → `Plantilla_Prediccion_Consumo_Con_Boton.xlsx`
- Macro VBA: `PredecirBiomasa()` → `PredecirConsumo()`
- Título del botón: "🎯 PREDECIR BIOMASA" → "🎯 PREDECIR CONSUMO"
- Columna de predicción: `Biomasa_Predicha` → `Consumo_kWh_Mensual_Predicho`
- Mensajes actualizados en toda la macro

### 4. `0_regresion_consumo_ml.ipynb` (NUEVO)
**Cambios principales:**
- Creado desde `0_regresion_biomasa_ml.ipynb`
- Archivo Excel: `Base_Prediccion_Biomasa_Outliers1.xlsx` → `Paneles_solares_con_outliers.xlsx`
- Variable objetivo: `Biomasa_real Estadistica` → `Consumo_kWh_Mensual`
- Features to drop:
  - **Anterior**: `['Fecha de Medicion', 'ID_parcela', 'Categoria de Biomasa', 'Validacion']`
  - **Nuevo**: `['ID_Cliente', 'Validar', 'Factura_Mensual_COP']`
- Títulos y descripciones actualizadas en todo el notebook

### 5. `actualizar_notebook.py` (NUEVO)
Script auxiliar creado para automatizar la actualización del notebook.

---

## Instrucciones de Uso

### Paso 1: Entrenar el Modelo
1. Abre el notebook: `0_regresion_consumo_ml.ipynb`
2. Ejecuta todas las celdas (Kernel → Restart & Run All)
3. Al final del notebook, agrega una celda con el código para guardar el modelo:
   ```python
   from importlib import reload
   import sys
   sys.path.append('.')

   # Importar la función de guardar modelo
   exec(open('1_guardar_modelo.py').read())

   # Guardar el modelo
   feature_names = list(X_clean.columns)
   model_info = guardar_modelo_entrenado(
       best_model=best_model,
       best_model_name=best_model_name,
       scaler=scaler,
       results_sorted=results_sorted,
       X_train=X_train,
       feature_names=feature_names
   )
   ```

### Paso 2: Crear Plantilla de Predicción
```bash
python 2_crear_plantilla_excel.py
```
Esto creará: `Plantilla_Prediccion_Consumo.xlsx`

### Paso 3: Hacer Predicciones
1. Llena los datos en `Plantilla_Prediccion_Consumo.xlsx`
2. Ejecuta:
   ```bash
   python 3_predecir_en_excel.py
   ```

### Alternativa: Excel con Botón (Opcional)
```bash
python 4_crear_excel_con_boton.py
```
Esto creará: `Plantilla_Prediccion_Consumo_Con_Boton.xlsx`

---

## Notas Importantes

### Variables Categóricas
El sistema ahora maneja tres variables categóricas:
- **Sector**: Residencial, Comercial, Industrial
- **Ciudad**: Montería, Sahagún, Planeta Rica, Cereté, Lorica
- **Puede_Pagar_Solar**: Sí/No

Estas se codifican automáticamente durante el preprocesamiento.

### Exclusiones
- **Factura_Mensual_COP** se excluye porque está altamente correlacionada con el consumo (target)
- **ID_Cliente** y **Validar** se excluyen porque son columnas de control

### Validación Requerida
Después de entrenar el modelo, debes verificar:
1. Las métricas de rendimiento (R², RMSE, MAE)
2. La importancia de las variables predictoras
3. Los residuos y posibles outliers
4. La generalización del modelo con validación cruzada

---

## Archivos Generados al Entrenar

Después de entrenar el modelo se generarán:
- `best_model.pkl` - Modelo entrenado
- `scaler.pkl` - Escalador de datos
- `model_info.json` - Metadatos del modelo
- `Reporte_Consumo_ML_[timestamp].xlsx` - Reporte de resultados

---

## Compatibilidad

- Python 3.6+
- Librerías requeridas: pandas, openpyxl, scikit-learn, numpy
- Excel 2016+ para las plantillas con macros

---

**Fecha de actualización**: 2025-11-09
**Tipo de tarea**: Migración de dataset y actualización de variable objetivo

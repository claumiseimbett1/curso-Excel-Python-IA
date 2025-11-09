# Sistema de Predicción de Biomasa en Excel

## 📋 Descripción

Este sistema permite hacer predicciones de biomasa usando un modelo de Machine Learning entrenado. Los usuarios pueden ingresar nuevos datos en un archivo Excel y el sistema automáticamente calculará las predicciones y las escribirá en el mismo archivo.

**Ahora con DOS OPCIONES de predicción:**
- 🎯 **Opción 1:** Excel con Botón VBA (predicciones con un clic)
- ⚡ **Opción 2:** Excel Simple (ejecutando script Python)

## 🎯 Características

- ✅ Predicciones automáticas usando el mejor modelo entrenado
- ✅ Interfaz simple: solo Excel, no requiere conocimientos avanzados de Python
- ✅ Las predicciones se escriben en el mismo archivo Excel
- ✅ Validación automática de datos
- ✅ Manejo de valores faltantes
- ✅ Indicadores visuales (colores) en los resultados
- ✅ Dos métodos de predicción: con botón o con script
- ✅ Predicción directa desde Python/Jupyter (opcional)

## 📂 Archivos del Sistema

### Scripts Principales
```
├── 1_guardar_modelo.py                      # Guarda el modelo entrenado
├── 2_crear_plantilla_excel.py               # Crea la plantilla Excel básica
├── 3_predecir_en_excel.py                   # Script de predicción (versión original)
├── 4_crear_excel_con_boton.py               # Crea Excel con botón VBA (NUEVO)
├── predictor_excel_simple.py                # Predicción simplificada (NUEVO - RECOMENDADO)
```

### Documentación
```
├── README_Sistema_Prediccion.md             # Este archivo - Guía general
├── GUIA_PREDICCION_EXCEL.md                 # Guía detallada de las 2 opciones
```

### Archivos Generados Automáticamente
```
├── best_model.pkl                           # Modelo de ML entrenado
├── scaler.pkl                               # Escalador de datos
├── model_info.json                          # Información y métricas del modelo
├── Plantilla_Prediccion_Biomasa.xlsx        # Plantilla Excel básica
├── Plantilla_Prediccion_Con_Boton.xlsx      # Plantilla Excel con botón VBA
└── codigo_vba_prediccion.bas                # Código VBA para el botón
```

## 🚀 Inicio Rápido

### Configuración Inicial (Una sola vez)

**Opción A: Usar script 1 (Recomendado)**

Si ya tienes el modelo entrenado en tu notebook:

```bash
python3 1_guardar_modelo.py
```

**Opción B: Agregar código al notebook**

Si prefieres ejecutar desde el notebook, ve al **PASO 1 Detallado** más abajo.

### Elegir tu Método de Predicción

Una vez guardado el modelo, elige UNO de estos dos métodos:

#### ⚡ **MÉTODO SIMPLE** (Recomendado para empezar)

1. **Crear plantilla:**
   ```bash
   python3 2_crear_plantilla_excel.py
   ```

2. **Llenar datos:**
   - Abre `Plantilla_Prediccion_Biomasa.xlsx`
   - Llena tus datos
   - Guarda y cierra

3. **Predecir:**
   ```bash
   python3 3_predecir_en_excel.py
   ```

4. **Ver resultados:**
   - Abre el Excel
   - Las predicciones están en la columna verde

#### 🎯 **MÉTODO CON BOTÓN** (Para uso frecuente)

1. **Crear Excel con botón:**
   ```bash
   python3 4_crear_excel_con_boton.py
   ```

2. **Configurar VBA** (solo la primera vez):
   - Sigue las instrucciones en el Excel generado
   - Configuración de ~10 minutos

3. **Usar:**
   - Llena datos
   - Haz clic en el botón
   - ¡Listo!

📖 **Para instrucciones detalladas de ambos métodos, consulta:** `GUIA_PREDICCION_EXCEL.md`

---

## 📖 Guía Detallada

### PASO 1: Entrenar y Guardar el Modelo

**1.1. Ejecuta el notebook de predicción**
- Abre: `prediccion_biomasa_ml.ipynb`
- Ejecuta todas las celdas en orden (Kernel → Restart & Run All)
- Espera a que termine el entrenamiento de todos los modelos

**1.2. Agrega código al final del notebook**

Crea una nueva celda al final del notebook y pega este código:

```python
import pickle
import json
from datetime import datetime

def guardar_modelo_entrenado(best_model, best_model_name, scaler, results_sorted,
                             X_train, feature_names):
    """Guarda el modelo entrenado y toda la información necesaria"""

    print("=" * 60)
    print("GUARDANDO MODELO ENTRENADO")
    print("=" * 60)

    # Guardar modelo
    with open('best_model.pkl', 'wb') as f:
        pickle.dump(best_model, f)
    print("✓ Modelo guardado: best_model.pkl")

    # Guardar scaler
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print("✓ Scaler guardado: scaler.pkl")

    # Guardar información
    model_info = {
        'model_name': best_model_name,
        'fecha_entrenamiento': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'metricas': {
            'R2_test': float(results_sorted.loc[best_model_name, 'R2_test']),
            'RMSE_test': float(results_sorted.loc[best_model_name, 'RMSE_test']),
            'MAE_test': float(results_sorted.loc[best_model_name, 'MAE_test']),
            'CV_R2_mean': float(results_sorted.loc[best_model_name, 'CV_R2_mean']),
            'CV_R2_std': float(results_sorted.loc[best_model_name, 'CV_R2_std'])
        },
        'feature_names': feature_names,
        'n_features': len(feature_names),
        'n_train_samples': X_train.shape[0]
    }

    with open('model_info.json', 'w', encoding='utf-8') as f:
        json.dump(model_info, f, indent=2, ensure_ascii=False)
    print("✓ Información guardada: model_info.json")

    print(f"\nModelo: {best_model_name}")
    print(f"R² Score: {model_info['metricas']['R2_test']:.4f}")
    print(f"Variables: {len(feature_names)}")

    return model_info

# Ejecutar
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

**1.3. Ejecuta la celda**

Verás un mensaje de confirmación con la información del modelo guardado.

✅ **Archivos generados:** `best_model.pkl`, `scaler.pkl`, `model_info.json`

---

### PASO 2: Crear la Plantilla Excel

**2.1. Ejecuta el script de creación de plantilla**

```bash
python 2_crear_plantilla_excel.py
```

o si usas Python 3:

```bash
python3 2_crear_plantilla_excel.py
```

**2.2. Verifica el archivo generado**

Se creará el archivo: **`Plantilla_Prediccion_Biomasa.xlsx`**

Este archivo contiene:
- **Hoja 1:** "Datos para Predicción" - donde ingresas los datos
- **Hoja 2:** "Instrucciones" - guía de uso

✅ **Archivo generado:** `Plantilla_Prediccion_Biomasa.xlsx`

---

### PASO 3: Llenar Datos en el Excel

**3.1. Abre el archivo Excel**

```
Plantilla_Prediccion_Biomasa.xlsx
```

**3.2. Ve a la hoja "Datos para Predicción"**

**3.3. Llena tus datos**

| ID | NDVI Outlier Manual | NDRE Outlier Manual | PRECIPITACION Outlier Manual | DIAS SIN LLUVIA Estadistica | Tipo_suelo | Biomasa_Predicha |
|----|---------------------|---------------------|------------------------------|----------------------------|------------|------------------|
| 1  | 0.75                | 0.65                | 120                          | 5                          | Franco     | *(se llenará)*   |
| 2  | 0.68                | 0.58                | 95                           | 8                          | Arcilloso  | *(se llenará)*   |
| 3  | 0.82                | 0.72                | 140                          | 3                          | Franco     | *(se llenará)*   |

**⚠️ IMPORTANTE:**
- ❌ **NO modifiques** los encabezados (fila 5)
- ❌ **NO llenes** la columna "Biomasa_Predicha" (se llenará automáticamente)
- ✅ Puedes agregar todas las filas que necesites
- ✅ Asegúrate de llenar todas las columnas requeridas

**3.4. Guarda el archivo**

Ctrl+S o File → Save

---

### PASO 4: Ejecutar Predicción

**4.1. Ejecuta el script de predicción**

```bash
python 3_predecir_en_excel.py
```

o si usas Python 3:

```bash
python3 3_predecir_en_excel.py
```

**4.2. Verás el proceso en consola:**

```
======================================================================
SISTEMA DE PREDICCIÓN DE BIOMASA
======================================================================
✓ Modelo cargado
✓ Scaler cargado
✓ Información cargada

Modelo: Random Forest
R² Score: 0.8542
RMSE: 125.34
MAE: 98.21

======================================================================
LEYENDO DATOS DEL EXCEL
======================================================================
✓ Archivo leído: Plantilla_Prediccion_Biomasa.xlsx
  Total de filas: 13
  Filas con datos: 5

✓ Columnas verificadas: 5 variables

======================================================================
PREPROCESANDO DATOS
======================================================================
✓ Datos preprocesados: (5, 5)
✓ Datos escalados

======================================================================
HACIENDO PREDICCIONES
======================================================================
✓ Predicciones realizadas: 5 valores

  Estadísticas de predicciones:
    - Mínimo: 245.32
    - Máximo: 512.78
    - Promedio: 389.45
    - Mediana: 376.90

======================================================================
ESCRIBIENDO RESULTADOS EN EXCEL
======================================================================
✓ Resultados escritos en: Plantilla_Prediccion_Biomasa.xlsx
  Columna: Biomasa_Predicha
  Filas actualizadas: 5

======================================================================
✓ ¡PROCESO COMPLETADO EXITOSAMENTE!
======================================================================

Abre el archivo Plantilla_Prediccion_Biomasa.xlsx para ver las predicciones
Las predicciones están en la columna 'Biomasa_Predicha' (fondo verde)
```

---

### PASO 5: Ver Resultados

**5.1. Abre nuevamente el archivo Excel**

```
Plantilla_Prediccion_Biomasa.xlsx
```

**5.2. Verás las predicciones**

La columna "Biomasa_Predicha" ahora tendrá valores con **fondo verde**:

| ID | NDVI | NDRE | PRECIPITACION | DIAS SIN LLUVIA | Tipo_suelo | **Biomasa_Predicha** |
|----|------|------|---------------|-----------------|------------|----------------------|
| 1  | 0.75 | 0.65 | 120           | 5               | Franco     | **389.45** 🟢       |
| 2  | 0.68 | 0.58 | 95            | 8               | Arcilloso  | **245.32** 🟢       |
| 3  | 0.82 | 0.72 | 140           | 3               | Franco     | **512.78** 🟢       |

**5.3. Marca de tiempo**

En la fila 3 verás cuándo se hizo la última predicción.

---

## 🔄 Hacer Nuevas Predicciones

### Con Método Simple:
1. Abre el Excel
2. Agrega o modifica datos
3. Guarda el archivo
4. Ejecuta: `python3 3_predecir_en_excel.py`
5. Abre el Excel para ver resultados

### Con Método Botón:
1. Abre el Excel
2. Agrega o modifica datos
3. Haz clic en el botón "🎯 PREDECIR BIOMASA"
4. ¡Listo!

---

## 💻 Predicción Directa desde Python/Jupyter (Avanzado)

Si prefieres hacer predicciones directamente desde Python sin usar Excel:

```python
from predictor_excel_simple import predecir_valores_directos

# Hacer una predicción
biomasa = predecir_valores_directos(
    NDVI_Outlier_Manual=0.75,
    NDRE_Outlier_Manual=0.65,
    PRECIPITACION_Outlier_Manual=120.5,
    DIAS_SIN_LLUVIA_Estadistica=5,
    Tipo_suelo='Franco'
)

print(f"Biomasa predicha: {biomasa:.2f} kg/ha")
```

**Nota:** Asegúrate de que `predictor_excel_simple.py` esté creado ejecutando el script 4.

---

## ⚙️ Variables Requeridas

El modelo requiere estas variables en orden:

1. **NDVI Outlier Manual** - Índice de Vegetación (0-1)
2. **NDRE Outlier Manual** - Índice de Borde Rojo (0-1)
3. **PRECIPITACION Outlier Manual** - Precipitación en mm
4. **DIAS SIN LLUVIA Estadistica** - Días consecutivos sin lluvia
5. **Tipo_suelo** - Tipo de suelo (Arenoso, Arcilloso, Franco)

---

## ❓ Preguntas Frecuentes

### ¿Qué método de predicción debo usar?

- **Método Simple:** Ideal si estás empezando o solo harás predicciones ocasionalmente
- **Método con Botón:** Ideal si harás predicciones frecuentemente y quieres mayor comodidad

### ¿Qué pasa si tengo valores faltantes?

El sistema automáticamente:
- Rellena valores numéricos con la mediana
- Rellena valores categóricos con el valor más común

### ¿Puedo agregar más filas?

Sí, puedes agregar todas las filas que necesites. El sistema procesará todas las filas que tengan datos.

### ¿Qué significa el fondo verde?

El fondo verde en la columna "Biomasa_Predicha" indica que esas celdas contienen predicciones del modelo.

### ¿Cómo sé qué tan preciso es el modelo?

Revisa el archivo `model_info.json` o el mensaje en consola. Verás:
- **R² Score:** Qué tan bien explica el modelo la variabilidad (0-1, más alto es mejor)
- **RMSE:** Error promedio en las predicciones
- **MAE:** Error absoluto promedio

### ¿Puedo usar este sistema en otra computadora?

Sí, solo necesitas copiar estos archivos:
- `best_model.pkl`
- `scaler.pkl`
- `model_info.json`
- Scripts de predicción (3 o predictor_excel_simple.py)
- Excel correspondiente

### ¿Necesito saber programación para usar esto?

No. Con el **Método Simple**, solo necesitas:
1. Ejecutar un comando en terminal
2. Llenar datos en Excel
3. Ejecutar otro comando

Con el **Método con Botón**, después de la configuración inicial solo usas Excel.

---

## 🐛 Solución de Problemas

### ❌ Error: "No se encuentra model_info.json"

**Solución:** Ejecuta primero `python3 1_guardar_modelo.py` para guardar el modelo.

### ❌ Error: "No se encuentra Plantilla_Prediccion_Biomasa.xlsx"

**Solución:** Ejecuta `python3 2_crear_plantilla_excel.py`

### ❌ Error: "Faltan columnas en el Excel"

**Solución:** No modifiques los encabezados del Excel. Si borraste algo, regenera la plantilla.

### ❌ Error: "No hay datos para predecir"

**Solución:** Llena al menos una fila completa con todos los valores en el Excel.

### ❌ El botón VBA no funciona

**Solución:**
1. Verifica que guardaste el archivo como `.xlsm`
2. Habilita las macros al abrir el Excel
3. Verifica que Python esté instalado: `python --version`
4. Asegúrate de que `predictor_excel_simple.py` esté en la misma carpeta

### ❌ "Python no encontrado" (en el botón)

**Solución:**
1. Instala Python desde: https://www.python.org/downloads/
2. Durante la instalación, marca "Add Python to PATH"
3. Reinicia Excel y prueba nuevamente

### ❌ Las predicciones parecen incorrectas

**Solución:**
1. Verifica que los datos estén en las unidades correctas
2. Revisa que el tipo de suelo esté escrito exactamente como: "Arenoso", "Arcilloso", o "Franco"
3. Verifica que NDVI y NDRE estén entre 0 y 1

### ❌ El Excel no se actualiza

**Solución:**
- **Cierra Excel antes de ejecutar el script** (Método Simple)
- Excel no puede modificarse mientras está abierto

### 📖 Más ayuda

Para problemas específicos con cada método, consulta `GUIA_PREDICCION_EXCEL.md`

---

## 📊 Información del Modelo

El sistema guarda automáticamente:

- **Tipo de modelo:** El mejor modelo entrenado (ej. Lasso, Random Forest, Gradient Boosting)
- **Métricas de desempeño:** R², RMSE, MAE
- **Fecha de entrenamiento**
- **Variables usadas**
- **Número de muestras de entrenamiento**
- **Hiperparámetros**

Todo esto se guarda en `model_info.json` y puedes consultarlo en cualquier momento.

---

## 📊 Comparación de Métodos

| Característica | Método Simple | Método con Botón |
|----------------|---------------|------------------|
| Configuración inicial | ⭐ Muy fácil (1 min) | ⭐⭐ Media (10 min) |
| Uso diario | ⭐⭐ Fácil (3 pasos) | ⭐⭐⭐ Muy fácil (1 clic) |
| Requiere terminal | Sí | No (después de configurar) |
| Requiere VBA/Macros | No | Sí |
| Mejor para | Uso ocasional | Uso frecuente |
| Conocimientos técnicos | Básicos | Mínimos (después de configurar) |

**Recomendación:**
- Si estás empezando o solo harás predicciones de vez en cuando → **Método Simple**
- Si harás predicciones frecuentemente → **Método con Botón**

---

## 📞 Soporte

Si tienes problemas:

1. Revisa este README
2. Consulta `GUIA_PREDICCION_EXCEL.md` para instrucciones detalladas
3. Verifica los mensajes de error en consola
4. Asegúrate de seguir los pasos en orden
5. Verifica que todos los archivos necesarios existan

---

## 📝 Notas Técnicas

- **Lenguaje:** Python 3.6+
- **Librerías requeridas:**
  - pandas
  - numpy
  - scikit-learn
  - openpyxl
  - pickle (incluido en Python)

- **Compatibilidad:** Windows, macOS, Linux
- **Formatos Excel:** .xlsx (método simple), .xlsm (método con botón)

---

## 🎯 Resumen de Scripts

| Script | Propósito | Cuándo Usar |
|--------|-----------|-------------|
| `1_guardar_modelo.py` | Guardar modelo entrenado | Una sola vez después de entrenar |
| `2_crear_plantilla_excel.py` | Crear Excel básico | Para método simple |
| `3_predecir_en_excel.py` | Hacer predicciones | Cada vez que quieras predecir (método simple) |
| `4_crear_excel_con_boton.py` | Crear Excel con VBA | Para método con botón |
| `predictor_excel_simple.py` | Predicción simplificada | Llamado por script 3 o 4 |

---

**¡Listo! Ahora tienes un sistema completo de predicción de biomasa con DOS opciones de uso.** 🎉

📖 **Para más detalles, consulta:** `GUIA_PREDICCION_EXCEL.md`

---

*Última actualización: 2025-10-25*

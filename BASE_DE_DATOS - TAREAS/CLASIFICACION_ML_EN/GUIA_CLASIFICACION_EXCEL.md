# 🌱 GUÍA DE CLASIFICACIÓN DE BIOMASA EN EXCEL

## 📋 Resumen

Ahora tienes **DOS OPCIONES** para hacer clasificación de biomasa directamente desde Excel:

### ✅ OPCIÓN 1: Excel con Botón (Más Interactivo)
- Archivo: `Plantilla_Clasificacion_Con_Boton.xlsx`
- **Requiere**: Configurar macro VBA (una sola vez)
- **Ventaja**: Clasificación con un solo clic en un botón
- **Uso**: Ideal si trabajas frecuentemente con el mismo Excel

### ✅ OPCIÓN 2: Excel Simple (Más Rápido de Configurar)
- Archivo: `Plantilla_Clasificacion_Biomasa.xlsx`
- **Requiere**: Ejecutar script Python cada vez
- **Ventaja**: No necesita configuración, funciona inmediatamente
- **Uso**: Ideal si solo harás clasificaciones ocasionalmente

---

## 🚀 OPCIÓN 1: Excel con Botón

### Paso 1: Crear la Plantilla con Botón

```bash
python 4_crear_excel_con_boton_clasificacion.py
```

Esto genera:
- `Plantilla_Clasificacion_Con_Boton.xlsx` - Excel con diseño para botón
- `codigo_vba_clasificacion.bas` - Código VBA para el botón

### Paso 2: Configurar el Botón (Solo la Primera Vez)

1. **Abrir el archivo Excel**
   - Abre `Plantilla_Clasificacion_Con_Boton.xlsx`

2. **Guardar como XLSM (Excel con Macros)**
   - File → Save As
   - Tipo: `Excel Macro-Enabled Workbook (*.xlsm)`
   - Guardar

3. **Habilitar la pestaña "Desarrollador"**
   - File → Options → Customize Ribbon
   - ✓ Marca "Developer" (Desarrollador)
   - OK

4. **Abrir el Editor VBA**
   - Presiona `Alt + F11`
   - O ve a: Developer → Visual Basic

5. **Insertar un Módulo**
   - En el editor VBA: Insert → Module
   - Se creará un nuevo módulo vacío

6. **Copiar el Código VBA**
   - Ve a la hoja "📖 Instrucciones VBA" del Excel
   - Copia TODO el código VBA (está en fondo gris)
   - Pégalo en el módulo del editor VBA

7. **Crear el Botón**
   - Cierra el editor VBA (`Alt + Q`)
   - Ve a la hoja "Datos para Clasificación"
   - Developer → Insert → Button (Form Control)
   - Dibuja un botón sobre las celdas A1:C1
   - Cuando te pida asignar macro, selecciona `PredecirClaseBiomasa`
   - Haz doble clic en el botón y escribe: "🎯 PREDECIR CLASE"

8. **Guardar y Cerrar**

### Paso 3: Usar el Botón

1. Abre `Plantilla_Clasificacion_Con_Boton.xlsm`
2. Llena los datos en las columnas
3. Haz clic en el botón **"🎯 PREDECIR CLASE"**
4. Espera unos segundos...
5. ¡Listo! Las clasificaciones aparecerán automáticamente

**Nota:** Si Excel pregunta sobre macros, selecciona "Habilitar contenido" o "Enable Macros"

---

## ⚡ OPCIÓN 2: Excel Simple (Sin Botón)

### Paso 1: Crear/Usar la Plantilla

Si no tienes la plantilla:
```bash
python 2_crear_plantilla_excel_clasificacion.py
```

Esto crea: `Plantilla_Clasificacion_Biomasa.xlsx`

### Paso 2: Llenar Datos

1. Abre `Plantilla_Clasificacion_Biomasa.xlsx`
2. Llena los datos en las columnas
3. **Guarda el archivo** (Ctrl + S)
4. **Cierra Excel**

### Paso 3: Ejecutar Clasificación

Opción A - Script Original:
```bash
python 3_predecir_en_excel_clasificacion.py
```

Opción B - Script Simplificado (Recomendado):
```bash
python predictor_simple_clasificacion.py
```

### Paso 4: Ver Resultados

1. Abre nuevamente `Plantilla_Clasificacion_Biomasa.xlsx`
2. Las predicciones estarán en la columna "Clase_Predicha" (fondo morado)
3. Verás una de estas categorías: **Baja**, **Media**, o **Alta**

---

## 🔧 Archivos del Sistema

### Scripts Principales

| Archivo | Descripción | Cuándo Usar |
|---------|-------------|-------------|
| `1_guardar_modelo_clasificacion.py` | Guarda el modelo entrenado | Una sola vez después de entrenar |
| `2_crear_plantilla_excel_clasificacion.py` | Crea plantilla básica | Cuando necesites un Excel nuevo |
| `3_predecir_en_excel_clasificacion.py` | Clasificación (versión original) | Para hacer clasificaciones |
| `4_crear_excel_con_boton_clasificacion.py` | Crea Excel con botón | Para configurar Excel interactivo |
| `predictor_simple_clasificacion.py` | Clasificación simplificada | **Recomendado para clasificaciones** |

### Archivos del Modelo (Generados Automáticamente)

- `best_model_clasificacion.pkl` - Modelo de ML entrenado
- `scaler_clasificacion.pkl` - Escalador de datos (si aplica)
- `imputer_clasificacion.pkl` - Imputador de valores nulos
- `label_encoder.pkl` - Codificador de clases
- `model_info_clasificacion.json` - Información del modelo

### Plantillas Excel

- `Plantilla_Clasificacion_Biomasa.xlsx` - Plantilla básica (Opción 2)
- `Plantilla_Clasificacion_Con_Boton.xlsx` - Plantilla con botón (Opción 1)

### Código VBA

- `codigo_vba_clasificacion.bas` - Código para el botón de Excel

---

## 💻 Clasificación Directa desde Python/Jupyter

Si prefieres hacer clasificaciones directamente desde Python sin usar Excel:

```python
from predictor_simple_clasificacion import predecir_clase_directa

resultado = predecir_clase_directa(
    NDVI_Outlier_Manual=0.75,
    NDRE_Outlier_Manual=0.65,
    PRECIPITACION_Outlier_Manual=120.5,
    DIAS_SIN_LLUVIA_Estadistica=5,
    Tipo_suelo='Franco'
)

print(f"Clase de biomasa predicha: {resultado}")
# Salida: "Biomasa Alta" o "Biomasa Media" o "Biomasa Baja"
```

---

## ❓ Solución de Problemas

### ❌ Error: "No se encuentra best_model_clasificacion.pkl"

**Solución:**
```bash
python 1_guardar_modelo_clasificacion.py
```

### ❌ Error: "Python no encontrado" (en el botón VBA)

**Solución:**
1. Verifica que Python esté instalado: `python --version`
2. Si no está, instala desde: https://www.python.org/downloads/
3. Durante la instalación, marca "Add Python to PATH"

### ❌ El botón no hace nada

**Solución:**
1. Verifica que guardaste el archivo como `.xlsm`
2. Verifica que habilitaste las macros al abrir
3. Verifica que `predictor_simple_clasificacion.py` esté en la misma carpeta
4. Prueba la macro `VerificarPython` para ver si encuentra Python

### ❌ "No hay datos para clasificar"

**Solución:**
- Llena al menos una fila completa con todos los valores
- No dejes celdas vacías en las columnas de variables

### ❌ El Excel no se actualiza

**Solución:**
- **Cierra Excel antes de ejecutar el script** (si usas Opción 2)
- Excel no puede modificarse si está abierto

---

## 📊 Comparación de Opciones

| Característica | Opción 1 (Botón) | Opción 2 (Simple) |
|----------------|------------------|-------------------|
| Configuración inicial | Media (10 min) | Muy fácil (1 min) |
| Uso repetido | Muy fácil (1 clic) | Fácil (1 comando) |
| Requiere Terminal | No | Sí |
| Requiere VBA/Macros | Sí | No |
| Mejor para | Uso frecuente | Uso ocasional |
| Archivos necesarios | .xlsm + scripts | .xlsx + scripts |

---

## 🎯 Recomendaciones

### Si eres usuario de Excel principalmente:
→ Usa **Opción 1** (Excel con Botón)
- Más intuitivo
- No necesitas abrir la terminal
- Experiencia tipo "aplicación"

### Si usas Python/Jupyter frecuentemente:
→ Usa **Opción 2** (Excel Simple) o clasificación directa desde Python
- Más rápido de configurar
- Más flexible
- No necesitas lidiar con macros de Excel

### Si solo harás clasificaciones de vez en cuando:
→ Usa **Opción 2** (Excel Simple)
- Sin configuración complicada
- Funciona inmediatamente

---

## 📞 Flujo de Trabajo Completo

### Primera Vez (Configuración)

```bash
# 1. Entrenar el modelo (si no lo has hecho)
# Ejecuta tu notebook de Jupyter: 0_clasificacion_biomasa_ml.ipynb

# 2. Guardar el modelo
python 1_guardar_modelo_clasificacion.py

# 3. Elegir tu opción:

# Opción 1: Con botón
python 4_crear_excel_con_boton_clasificacion.py
# → Configura VBA siguiendo las instrucciones

# Opción 2: Simple
python 2_crear_plantilla_excel_clasificacion.py
```

### Uso Diario (Clasificaciones)

**Opción 1:**
1. Abre el .xlsm
2. Llena datos
3. Clic en botón
4. ¡Listo! (Verás: Baja, Media o Alta)

**Opción 2:**
1. Abre el .xlsx
2. Llena datos
3. Guarda y cierra
4. `python predictor_simple_clasificacion.py`
5. Abre y ve resultados

---

## 📝 Notas Importantes

1. **Seguridad de Macros**: Excel puede advertir sobre macros. Es seguro habilitarlas porque tú mismo creaste el código VBA.

2. **Ruta de Python**: El código VBA asume que Python está en el PATH del sistema. Si usaste Anaconda, puede que necesites ajustar la ruta en el VBA.

3. **Nombres de Archivos**: No cambies el nombre de `predictor_simple_clasificacion.py` si usas el botón VBA, o edita el código VBA para reflejar el nuevo nombre.

4. **Backup**: Siempre guarda una copia del Excel antes de hacer clasificaciones masivas.

5. **Variables**: Los nombres de las columnas en el Excel deben coincidir EXACTAMENTE con los del modelo entrenado.

---

## 🎨 Clases de Biomasa

El modelo clasifica la biomasa en **3 categorías**:

| Clase | Descripción | Color en Excel |
|-------|-------------|----------------|
| **Baja** | Biomasa baja | 🔵 Azul claro |
| **Media** | Biomasa media | 🟡 Amarillo |
| **Alta** | Biomasa alta | 🟢 Verde |

---

## ✅ Variables Requeridas (Tu Modelo)

Tu modelo actual requiere estas variables (verifica en `model_info_clasificacion.json`):

Las variables exactas dependen de tu dataset, pero típicamente incluyen:

- Índices de vegetación (NDVI, NDRE, etc.)
- Variables climáticas (Precipitación, Días sin lluvia, etc.)
- Variables de suelo (Tipo de suelo, pH, etc.)

Consulta el archivo `model_info_clasificacion.json` para ver la lista exacta de variables.

---

## 📈 Interpretación de Resultados

### Columnas en el Excel de Resultados:

1. **Clase_Predicha**: La categoría predicha (Baja, Media, Alta)
2. **Prob_Baja**: Probabilidad de ser clase Baja (0-1)
3. **Prob_Media**: Probabilidad de ser clase Media (0-1)
4. **Prob_Alta**: Probabilidad de ser clase Alta (0-1)

### Ejemplo de Interpretación:

```
Clase_Predicha: Alta
Prob_Baja: 0.05
Prob_Media: 0.25
Prob_Alta: 0.70
```

Esto significa:
- El modelo predice que la biomasa es **Alta**
- Tiene un 70% de confianza en esta predicción
- Hay un 25% de probabilidad de que sea Media
- Solo un 5% de probabilidad de que sea Baja

---

## 🔍 Validación de Predicciones

### Recomendaciones:

1. **Revisar probabilidades**: Si las probabilidades son similares (ej: 0.33, 0.33, 0.34), el modelo tiene baja confianza.

2. **Validar con datos conocidos**: Prueba el modelo con datos cuya clasificación ya conoces.

3. **Rangos razonables**: Verifica que los valores de entrada estén en rangos razonables.

4. **Consistencia**: Valores similares de entrada deben dar resultados similares.

---

¡Disfruta clasificando biomasa! 🌱📊🎯

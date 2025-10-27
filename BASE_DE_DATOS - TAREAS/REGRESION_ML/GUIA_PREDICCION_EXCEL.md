# 🌱 GUÍA DE PREDICCIÓN DE BIOMASA EN EXCEL

## 📋 Resumen

Ahora tienes **DOS OPCIONES** para hacer predicciones de biomasa directamente desde Excel:

### ✅ OPCIÓN 1: Excel con Botón (Más Interactivo)
- Archivo: `Plantilla_Prediccion_Con_Boton.xlsx`
- **Requiere**: Configurar macro VBA (una sola vez)
- **Ventaja**: Predicciones con un solo clic en un botón
- **Uso**: Ideal si trabajas frecuentemente con el mismo Excel

### ✅ OPCIÓN 2: Excel Simple (Más Rápido de Configurar)
- Archivo: `Plantilla_Prediccion_Biomasa.xlsx`
- **Requiere**: Ejecutar script Python cada vez
- **Ventaja**: No necesita configuración, funciona inmediatamente
- **Uso**: Ideal si solo harás predicciones ocasionalmente

---

## 🚀 OPCIÓN 1: Excel con Botón

### Paso 1: Crear la Plantilla con Botón

```bash
python 4_crear_excel_con_boton.py
```

Esto genera:
- `Plantilla_Prediccion_Con_Boton.xlsx` - Excel con diseño para botón
- `codigo_vba_prediccion.bas` - Código VBA para el botón

### Paso 2: Configurar el Botón (Solo la Primera Vez)

1. **Abrir el archivo Excel**
   - Abre `Plantilla_Prediccion_Con_Boton.xlsx`

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
   - Ve a la hoja "Datos para Predicción"
   - Developer → Insert → Button (Form Control)
   - Dibuja un botón sobre las celdas A1:C1
   - Cuando te pida asignar macro, selecciona `PredecirBiomasa`
   - Haz doble clic en el botón y escribe: "🎯 PREDECIR BIOMASA"

8. **Guardar y Cerrar**

### Paso 3: Usar el Botón

1. Abre `Plantilla_Prediccion_Con_Boton.xlsm`
2. Llena los datos en las columnas
3. Haz clic en el botón **"🎯 PREDECIR BIOMASA"**
4. Espera unos segundos...
5. ¡Listo! Las predicciones aparecerán automáticamente

**Nota:** Si Excel pregunta sobre macros, selecciona "Habilitar contenido" o "Enable Macros"

---

## ⚡ OPCIÓN 2: Excel Simple (Sin Botón)

### Paso 1: Crear/Usar la Plantilla

Si no tienes la plantilla:
```bash
python 2_crear_plantilla_excel.py
```

Esto crea: `Plantilla_Prediccion_Biomasa.xlsx`

### Paso 2: Llenar Datos

1. Abre `Plantilla_Prediccion_Biomasa.xlsx`
2. Llena los datos en las columnas
3. **Guarda el archivo** (Ctrl + S)
4. **Cierra Excel**

### Paso 3: Ejecutar Predicción

Opción A - Script Original:
```bash
python 3_predecir_en_excel.py
```

Opción B - Script Simplificado (Recomendado):
```bash
python predictor_excel_simple.py
```

### Paso 4: Ver Resultados

1. Abre nuevamente `Plantilla_Prediccion_Biomasa.xlsx`
2. Las predicciones estarán en la columna "Biomasa_Predicha" (fondo verde)

---

## 🔧 Archivos del Sistema

### Scripts Principales

| Archivo | Descripción | Cuándo Usar |
|---------|-------------|-------------|
| `1_guardar_modelo.py` | Guarda el modelo entrenado | Una sola vez después de entrenar |
| `2_crear_plantilla_excel.py` | Crea plantilla básica | Cuando necesites un Excel nuevo |
| `3_predecir_en_excel.py` | Predicción (versión original) | Para hacer predicciones |
| `4_crear_excel_con_boton.py` | Crea Excel con botón | Para configurar Excel interactivo |
| `predictor_excel_simple.py` | Predicción simplificada | **Recomendado para predicciones** |

### Archivos del Modelo (Generados Automáticamente)

- `best_model.pkl` - Modelo de ML entrenado
- `scaler.pkl` - Escalador de datos
- `model_info.json` - Información del modelo

### Plantillas Excel

- `Plantilla_Prediccion_Biomasa.xlsx` - Plantilla básica (Opción 2)
- `Plantilla_Prediccion_Con_Boton.xlsx` - Plantilla con botón (Opción 1)

### Código VBA

- `codigo_vba_prediccion.bas` - Código para el botón de Excel

---

## 💻 Predicción Directa desde Python/Jupyter

Si prefieres hacer predicciones directamente desde Python sin usar Excel:

```python
from predictor_excel_simple import predecir_valores_directos

resultado = predecir_valores_directos(
    NDVI_Outlier_Manual=0.75,
    NDRE_Outlier_Manual=0.65,
    PRECIPITACION_Outlier_Manual=120.5,
    DIAS_SIN_LLUVIA_Estadistica=5,
    Tipo_suelo='Franco'
)

print(f"Biomasa predicha: {resultado:.2f} kg/ha")
```

---

## ❓ Solución de Problemas

### ❌ Error: "No se encuentra best_model.pkl"

**Solución:**
```bash
python 1_guardar_modelo.py
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
3. Verifica que `predictor_excel_simple.py` esté en la misma carpeta
4. Prueba la macro `VerificarPython` para ver si encuentra Python

### ❌ "No hay datos para predecir"

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
→ Usa **Opción 2** (Excel Simple) o predicción directa desde Python
- Más rápido de configurar
- Más flexible
- No necesitas lidiar con macros de Excel

### Si solo harás predicciones de vez en cuando:
→ Usa **Opción 2** (Excel Simple)
- Sin configuración complicada
- Funciona inmediatamente

---

## 📞 Flujo de Trabajo Completo

### Primera Vez (Configuración)

```bash
# 1. Entrenar el modelo (si no lo has hecho)
# Ejecuta tu notebook de Jupyter

# 2. Guardar el modelo
python 1_guardar_modelo.py

# 3. Elegir tu opción:

# Opción 1: Con botón
python 4_crear_excel_con_boton.py
# → Configura VBA siguiendo las instrucciones

# Opción 2: Simple
python 2_crear_plantilla_excel.py
```

### Uso Diario (Predicciones)

**Opción 1:**
1. Abre el .xlsm
2. Llena datos
3. Clic en botón
4. ¡Listo!

**Opción 2:**
1. Abre el .xlsx
2. Llena datos
3. Guarda y cierra
4. `python predictor_excel_simple.py`
5. Abre y ve resultados

---

## 📝 Notas Importantes

1. **Seguridad de Macros**: Excel puede advertir sobre macros. Es seguro habilitarlas porque tú mismo creaste el código VBA.

2. **Ruta de Python**: El código VBA asume que Python está en el PATH del sistema. Si usaste Anaconda, puede que necesites ajustar la ruta en el VBA.

3. **Nombres de Archivos**: No cambies el nombre de `predictor_excel_simple.py` si usas el botón VBA, o edita el código VBA para reflejar el nuevo nombre.

4. **Backup**: Siempre guarda una copia del Excel antes de hacer predicciones masivas.

5. **Variables**: Los nombres de las columnas en el Excel deben coincidir EXACTAMENTE con los del modelo entrenado.

---

## ✅ Variables Requeridas (Tu Modelo)

Tu modelo actual requiere estas 5 variables:

1. `NDVI Outlier Manual`
2. `NDRE Outlier Manual`
3. `PRECIPITACION Outlier Manual`
4. `DIAS SIN LLUVIA Estadistica`
5. `Tipo_suelo` (valores: 'Arenoso', 'Arcilloso', 'Franco')

---

¡Disfruta prediciendo biomasa! 🌱📊

import json

# Leer el archivo
with open('Instructivo_Datos_ML.ipynb', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convertir a string para hacer reemplazos
content = json.dumps(data, ensure_ascii=False, indent=1)

# Hacer todos los reemplazos
replacements = [
    ('## **4. Otras librerías de visualización**', '## **5. Otras librerías de visualización**'),
    ('### **4.1 Plotly**', '### **5.1 Plotly**'),
    ('### **4.2 Seaborn**', '### **5.2 Seaborn**'),
    ('## **5. Principales comandos de scikit-learn (sklearn)**', '## **6. Principales comandos de scikit-learn (sklearn)**'),
    ('### **5.2 ¿Qué es StandardScaler?**', '### **6.2 ¿Qué es StandardScaler?**'),
    ('### **5.3 ¿Qué es LabelEncoder?**', '### **6.3 ¿Qué es LabelEncoder?**'),
    ('### **5.4 ¿Qué es scikit-learn?**', '### **6.4 ¿Qué es scikit-learn?**'),
    ('### **5.5 `np.random.seed(42)` — Explicación**', '### **6.5 `np.random.seed(42)` — Explicación**'),
    ('### **5.6 Ejemplo simple con scikit-learn (Regresión)**', '### **6.6 Ejemplo simple con scikit-learn (Regresión)**'),
    ('### **3.7 Ejemplo simple con scikit-learn - Clasificación con Random Forest**', '### **6.7 Ejemplo simple con scikit-learn - Clasificación con Random Forest**'),
    ('## **4. Principales comandos de openpyxl**', '## **7. Principales comandos de openpyxl**'),
    ('### **4.2 ¿Qué es openpyxl?**', '### **7.2 ¿Qué es openpyxl?**'),
    ('### **4.3 Ejemplo simple con openpyxl**', '### **7.3 Ejemplo simple con openpyxl**'),
    ('## **5. ¿Qué son los modelos PKL (Pickle) y por qué se guardan?**', '## **8. ¿Qué son los modelos PKL (Pickle) y por qué se guardan?**'),
    ('### **5.1 ¿Qué es Pickle?**', '### **8.1 ¿Qué es Pickle?**'),
    ('### **5.2 ¿Qué contiene un modelo PKL?**', '### **8.2 ¿Qué contiene un modelo PKL?**'),
    ('### **5.3 Alternativas a Pickle**', '### **8.3 Alternativas a Pickle**'),
    ('### **5.4 ¿Qué es un Framework?**', '### **8.4 ¿Qué es un Framework?**'),
    ('### **5.5 Ejemplo práctico: Guardar y cargar modelos PKL**', '### **8.5 Ejemplo práctico: Guardar y cargar modelos PKL**'),
    ('### **5.6 Resumen: Flujo completo de guardado y carga**', '### **8.6 Resumen: Flujo completo de guardado y carga**'),
    ('### **5.7 Ejemplo de despliegue en producción**', '### **8.7 Ejemplo de despliegue en producción**'),
    ('### **5.8 Casos de uso comunes para modelos PKL**', '### **8.8 Casos de uso comunes para modelos PKL**'),
    ('### **5.9 Mejores prácticas**', '### **8.9 Mejores prácticas**'),
    ('### **5.10 Resumen final: Pickle vs Joblib**', '### **8.10 Resumen final: Pickle vs Joblib**'),
    ('## **6. Principales comandos de PyTorch**', '## **9. Principales comandos de PyTorch**'),
    ('### **6.1 ¿Qué es PyTorch?**', '### **9.1 ¿Qué es PyTorch?**'),
    ('### **6.3 Comparación: PyTorch vs scikit-learn**', '### **9.3 Comparación: PyTorch vs scikit-learn**'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Cargar el JSON corregido
data = json.loads(content)

# Guardar el archivo
with open('Instructivo_Datos_ML.ipynb', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("Numeración corregida exitosamente!")


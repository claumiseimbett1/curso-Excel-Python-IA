"""
Script para actualizar el notebook de regresión
Cambia de predicción de Biomasa a predicción de Consumo Energético
"""

import json
import sys

def actualizar_notebook():
    # Leer el notebook
    with open('0_regresion_biomasa_ml.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    cambios_realizados = 0

    # Recorrer todas las celdas
    for cell in notebook['cells']:
        if 'source' in cell:
            source_original = ''.join(cell['source'])
            source_modificado = source_original

            # Cambios principales
            replacements = [
                # Archivo Excel
                ("'Base_Prediccion_Biomasa_Outliers1.xlsx'", "'Paneles_solares_con_outliers.xlsx'"),
                ('"Base_Prediccion_Biomasa_Outliers1.xlsx"', '"Paneles_solares_con_outliers.xlsx"'),

                # Variable objetivo
                ("'Biomasa_real Estadistica'", "'Consumo_kWh_Mensual'"),
                ('"Biomasa_real Estadistica"', '"Consumo_kWh_Mensual"'),
                ("target = 'Biomasa_real Estadistica'", "target = 'Consumo_kWh_Mensual'"),

                # Features to drop - actualizar para el nuevo dataset
                ("features_to_drop = ['Fecha de Medicion', 'ID_parcela', 'Categoria de Biomasa', 'Validacion']",
                 "features_to_drop = ['ID_Cliente', 'Validar', 'Factura_Mensual_COP']  # Factura se excluye porque está correlacionada con consumo"),

                # Títulos y descripciones
                ("Predicción de Biomasa usando Machine Learning", "Predicción de Consumo Energético usando Machine Learning"),
                ("predecir biomasa", "predecir consumo energético"),
                ("PREDICCIÓN DE BIOMASA", "PREDICCIÓN DE CONSUMO ENERGÉTICO"),
                ("Reporte_Biomasa_ML", "Reporte_Consumo_ML"),
                ("prediccion_biomasa_ml", "prediccion_consumo_ml"),
                ("BIOMASA", "CONSUMO ENERGÉTICO"),
                ("Biomasa", "Consumo"),
                ("biomasa", "consumo energético"),
            ]

            for old, new in replacements:
                if old in source_modificado:
                    source_modificado = source_modificado.replace(old, new)
                    cambios_realizados += 1

            # Actualizar la celda si hubo cambios
            if source_modificado != source_original:
                cell['source'] = source_modificado.splitlines(True)

    # Guardar el notebook modificado
    with open('0_regresion_consumo_ml.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)

    print(f"✓ Notebook actualizado exitosamente")
    print(f"✓ Se realizaron {cambios_realizados} cambios")
    print(f"✓ Nuevo archivo creado: 0_regresion_consumo_ml.ipynb")
    print("\nNOTA IMPORTANTE:")
    print("El notebook ha sido adaptado para el nuevo dataset de paneles solares.")
    print("Debes revisar y ajustar:")
    print("1. Las variables predictoras según las columnas del nuevo Excel")
    print("2. La codificación de variables categóricas (Sector, Ciudad, Puede_Pagar_Solar)")
    print("3. Los rangos y valores esperados en las visualizaciones")

if __name__ == "__main__":
    try:
        actualizar_notebook()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

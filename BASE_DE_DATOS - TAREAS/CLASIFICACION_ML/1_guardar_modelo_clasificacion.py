"""
Script 1: Guardar Modelo de Clasificación Entrenado
===================================================
Este script se ejecuta DESPUÉS de entrenar todos los modelos en el notebook.
Guarda el mejor modelo, el scaler y la información relevante.

INSTRUCCIONES:
1. Ejecuta primero el notebook: 0_clasificacion_biomasa_ml.ipynb
2. Asegúrate de haber ejecutado todas las celdas
3. Ejecuta este script: python 1_guardar_modelo_clasificacion.py

El script extraerá automáticamente:
- El mejor modelo entrenado
- El scaler
- El LabelEncoder
- Las métricas de desempeño
- Los nombres de las variables
"""

import pickle
import json
from datetime import datetime
import os
import sys

def guardar_modelo_clasificacion():
    """
    Guarda el modelo de clasificación entrenado y toda la información necesaria
    """

    print("\n" + "=" * 70)
    print("GUARDANDO MODELO DE CLASIFICACIÓN")
    print("=" * 70 + "\n")

    # Verificar que las variables existan en el entorno
    required_vars = ['best_model', 'best_model_name', 'scaler', 'le_target',
                     'results_sorted_clf', 'X_imputed', 'X_train']

    # Importar variables del notebook (si se ejecuta desde Jupyter)
    try:
        # Intentar obtener variables del entorno de ejecución actual
        import __main__

        # Verificar variables
        missing_vars = []
        for var in required_vars:
            if not hasattr(__main__, var):
                missing_vars.append(var)

        if missing_vars:
            print("❌ ERROR: Faltan variables del notebook:")
            for var in missing_vars:
                print(f"   - {var}")
            print("\n💡 SOLUCIÓN:")
            print("1. Abre el notebook: 0_clasificacion_biomasa_ml.ipynb")
            print("2. Ejecuta todas las celdas (Kernel → Restart & Run All)")
            print("3. Al final del notebook, agrega una celda nueva con:")
            print("\n" + "-" * 70)
            print("%run 1_guardar_modelo_clasificacion.py")
            print("-" * 70 + "\n")
            print("4. Ejecuta esa celda")
            return None

        # Obtener variables
        best_model = getattr(__main__, 'best_model')
        best_model_name = getattr(__main__, 'best_model_name')
        scaler = getattr(__main__, 'scaler')
        le_target = getattr(__main__, 'le_target')
        results_sorted_clf = getattr(__main__, 'results_sorted_clf')
        X_imputed = getattr(__main__, 'X_imputed')
        X_train = getattr(__main__, 'X_train')

    except Exception as e:
        print(f"❌ ERROR: No se pueden obtener variables del notebook")
        print(f"   Detalles: {str(e)}")
        print("\n💡 Este script debe ejecutarse DESDE el notebook")
        print("   Agrega una celda al final con: %run 1_guardar_modelo_clasificacion.py")
        return None

    # Preparar información del modelo
    feature_names = list(X_imputed.columns)
    classes = list(le_target.classes_)

    model_info = {
        'model_name': best_model_name,
        'model_type': 'classification',
        'fecha_entrenamiento': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'metricas': {
            'Accuracy_test': float(results_sorted_clf.loc[best_model_name, 'Accuracy_test']),
            'Precision_test': float(results_sorted_clf.loc[best_model_name, 'Precision_test']),
            'Recall_test': float(results_sorted_clf.loc[best_model_name, 'Recall_test']),
            'F1_test': float(results_sorted_clf.loc[best_model_name, 'F1_test']),
            'CV_Accuracy_mean': float(results_sorted_clf.loc[best_model_name, 'CV_Accuracy_mean']),
            'CV_Accuracy_std': float(results_sorted_clf.loc[best_model_name, 'CV_Accuracy_std'])
        },
        'feature_names': feature_names,
        'classes': classes,
        'n_classes': len(classes),
        'n_features': len(feature_names),
        'n_train_samples': X_train.shape[0],
        'class_encoding': {str(i): clase for i, clase in enumerate(classes)}
    }

    # Agregar hiperparámetros si están disponibles
    if hasattr(best_model, 'best_params_'):
        model_info['hiperparametros'] = str(best_model.best_params_)
    elif hasattr(best_model, 'get_params'):
        model_info['hiperparametros'] = str(best_model.get_params())
    else:
        model_info['hiperparametros'] = "No disponible"

    # Guardar modelo
    print("📦 Guardando archivos...")

    with open('best_model_clasificacion.pkl', 'wb') as f:
        pickle.dump(best_model, f)
    print("   ✓ Modelo guardado: best_model_clasificacion.pkl")

    # Guardar scaler
    with open('scaler_clasificacion.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print("   ✓ Scaler guardado: scaler_clasificacion.pkl")

    # Guardar LabelEncoder
    with open('label_encoder_clasificacion.pkl', 'wb') as f:
        pickle.dump(le_target, f)
    print("   ✓ LabelEncoder guardado: label_encoder_clasificacion.pkl")

    # Guardar información
    with open('model_info_clasificacion.json', 'w', encoding='utf-8') as f:
        json.dump(model_info, f, indent=2, ensure_ascii=False)
    print("   ✓ Información guardada: model_info_clasificacion.json")

    # Crear backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f'modelo_clasificacion_backup_{timestamp}.pkl'
    with open(backup_filename, 'wb') as f:
        pickle.dump({'model': best_model, 'scaler': scaler, 'le_target': le_target}, f)
    print(f"   ✓ Backup creado: {backup_filename}")

    # Resumen
    print("\n" + "=" * 70)
    print("✅ MODELO GUARDADO EXITOSAMENTE")
    print("=" * 70)
    print(f"\n📊 Información del modelo:")
    print(f"   Tipo: Clasificación")
    print(f"   Modelo: {best_model_name}")
    print(f"   Clases: {', '.join(classes)}")
    print(f"   Número de clases: {len(classes)}")
    print(f"   Variables: {len(feature_names)}")
    print(f"\n📈 Métricas de desempeño:")
    print(f"   Accuracy: {model_info['metricas']['Accuracy_test']:.4f}")
    print(f"   Precision: {model_info['metricas']['Precision_test']:.4f}")
    print(f"   Recall: {model_info['metricas']['Recall_test']:.4f}")
    print(f"   F1-Score: {model_info['metricas']['F1_test']:.4f}")
    print(f"   CV Accuracy: {model_info['metricas']['CV_Accuracy_mean']:.4f} (± {model_info['metricas']['CV_Accuracy_std']:.4f})")

    print(f"\n📋 Variables predictoras:")
    for i, var in enumerate(feature_names, 1):
        print(f"   {i}. {var}")

    print("\n" + "=" * 70)
    print("PRÓXIMOS PASOS:")
    print("=" * 70)
    print("1. Crear plantilla Excel: python 2_crear_plantilla_excel_clasificacion.py")
    print("2. Llenar datos en el Excel")
    print("3. Hacer predicciones: python 3_predecir_en_excel_clasificacion.py")
    print("=" * 70 + "\n")

    return model_info


if __name__ == "__main__":
    try:
        model_info = guardar_modelo_clasificacion()
        if model_info is None:
            sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

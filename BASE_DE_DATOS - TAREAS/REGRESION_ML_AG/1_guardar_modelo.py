"""
Script 1: Guardar el Modelo Entrenado
======================================
Este script debe ejecutarse DESPUÉS de entrenar los modelos en el notebook.
Guarda el mejor modelo y el scaler para usar en predicciones futuras.

INSTRUCCIONES:
1. Ejecuta todo el notebook de predicción hasta tener el mejor modelo
2. Ejecuta este script en una celda nueva al final del notebook
3. Esto guardará: best_model.pkl, scaler.pkl, y model_info.json
"""

import pickle
import json
from datetime import datetime

def guardar_modelo_entrenado(best_model, best_model_name, scaler, results_sorted,
                             X_train, feature_names):
    """
    Guarda el modelo entrenado y toda la información necesaria para hacer predicciones

    Parámetros:
    -----------
    best_model : modelo entrenado
    best_model_name : str, nombre del mejor modelo
    scaler : StandardScaler, scaler entrenado
    results_sorted : DataFrame con resultados de todos los modelos
    X_train : DataFrame de entrenamiento
    feature_names : list, nombres de las variables predictoras
    """

    print("=" * 60)
    print("GUARDANDO MODELO ENTRENADO")
    print("=" * 60)

    # 1. Guardar el modelo
    with open('best_model.pkl', 'wb') as f:
        pickle.dump(best_model, f)
    print("✓ Modelo guardado: best_model.pkl")

    # 2. Guardar el scaler
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print("✓ Scaler guardado: scaler.pkl")

    # 3. Guardar información del modelo
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

    print("\n" + "=" * 60)
    print("RESUMEN DEL MODELO GUARDADO")
    print("=" * 60)
    print(f"Modelo: {best_model_name}")
    print(f"R² Score: {model_info['metricas']['R2_test']:.4f}")
    print(f"RMSE: {model_info['metricas']['RMSE_test']:.2f}")
    print(f"MAE: {model_info['metricas']['MAE_test']:.2f}")
    print(f"Variables predictoras: {len(feature_names)}")
    print("\nVariables:")
    for i, var in enumerate(feature_names, 1):
        print(f"  {i}. {var}")

    print("\n" + "=" * 60)
    print("¡LISTO! Ahora puedes usar el script de predicción")
    print("=" * 60)

    return model_info


# CÓDIGO PARA EJECUTAR EN EL NOTEBOOK
# ====================================
# Copia este código en una celda nueva al final del notebook:
"""
# Guardar el modelo entrenado
feature_names = list(X_clean.columns)
model_info = guardar_modelo_entrenado(
    best_model=best_model,
    best_model_name=best_model_name,
    scaler=scaler,
    results_sorted=results_sorted,
    X_train=X_train,
    feature_names=feature_names
)
"""

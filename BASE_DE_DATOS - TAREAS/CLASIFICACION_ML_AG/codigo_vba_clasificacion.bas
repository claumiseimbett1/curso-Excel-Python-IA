
Sub PredecirClaseBiomasa()
    '=============================================================================
    ' MACRO: Predicción de Clase de Biomasa usando Machine Learning
    '=============================================================================
    ' Esta macro ejecuta el script Python que hace las predicciones y actualiza
    ' automáticamente este archivo Excel con los resultados
    '=============================================================================

    Dim pythonPath As String
    Dim scriptPath As String
    Dim command As String
    Dim shell As Object
    Dim waitOnReturn As Boolean: waitOnReturn = True
    Dim windowStyle As Integer: windowStyle = 1  ' 1 = Normal, 0 = Hidden
    Dim resultado As Long

    ' Deshabilitar actualización de pantalla para mejor rendimiento
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False

    ' Mensaje inicial
    MsgBox "Iniciando clasificación de biomasa..." & vbCrLf & vbCrLf & _
           "Este proceso puede tomar unos segundos.", vbInformation, "Clasificador de Biomasa"

    ' Guardar el archivo antes de ejecutar Python
    ThisWorkbook.Save

    ' Detectar la ruta del archivo actual
    scriptPath = ThisWorkbook.Path

    ' Intentar encontrar Python (prueba varios paths comunes)
    pythonPath = ""

    ' Opción 1: Python en PATH del sistema
    pythonPath = "python"

    ' Construir el comando completo
    ' El script predictor_simple_clasificacion.py debe estar en la misma carpeta
    command = "cmd /c cd /d """ & scriptPath & """ && " & pythonPath & " predictor_simple_clasificacion.py"

    ' Ejecutar el comando
    Set shell = CreateObject("WScript.Shell")

    On Error GoTo ErrorHandler
    resultado = shell.Run(command, windowStyle, waitOnReturn)

    ' Esperar un momento para que Python termine de escribir
    Application.Wait (Now + TimeValue("0:00:02"))

    ' Cerrar el archivo actual (sin guardar porque Python ya lo modificó)
    ThisWorkbook.Close SaveChanges:=False

    ' Reabrir el archivo para mostrar las predicciones
    Dim reopenPath As String
    reopenPath = scriptPath & "\" & ThisWorkbook.Name
    Workbooks.Open reopenPath

    ' Mensaje de éxito
    MsgBox "✅ ¡Clasificación completada!" & vbCrLf & vbCrLf & _
           "Las predicciones están en la columna 'Clase_Predicha'", _
           vbInformation, "Éxito"

    Application.ScreenUpdating = True
    Application.DisplayAlerts = True

    Exit Sub

ErrorHandler:
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True

    MsgBox "❌ Error al ejecutar la clasificación." & vbCrLf & vbCrLf & _
           "Detalles del error:" & vbCrLf & _
           Err.Description & vbCrLf & vbCrLf & _
           "Verifica que:" & vbCrLf & _
           "1. Python está instalado" & vbCrLf & _
           "2. El archivo predictor_simple_clasificacion.py está en la misma carpeta" & vbCrLf & _
           "3. Los archivos del modelo (best_model_clasificacion.pkl, etc.) existen", _
           vbCritical, "Error"
End Sub


Sub VerificarPython()
    '=============================================================================
    ' MACRO: Verificar instalación de Python
    '=============================================================================

    Dim shell As Object
    Dim resultado As Long

    Set shell = CreateObject("WScript.Shell")
    resultado = shell.Run("cmd /c python --version", 1, True)

    If resultado = 0 Then
        MsgBox "✅ Python está instalado correctamente", vbInformation
    Else
        MsgBox "❌ Python no encontrado" & vbCrLf & vbCrLf & _
               "Por favor, instala Python desde:" & vbCrLf & _
               "https://www.python.org/downloads/", vbCritical
    End If
End Sub


from flask import Flask, request, jsonify  # Importa Flask y sus funciones para manejar solicitudes y respuestas
from firebase_admin import credentials, firestore, initialize_app  # Importa las funciones necesarias de Firebase
import datetime  # Importa la biblioteca para trabajar con fechas y horas

# Inicializar la aplicación Flask
app = Flask(__name__)  # Crea una instancia de la aplicación Flask

# Configurar Firebase con el archivo de credenciales
try:
    cred = credentials.Certificate("../api/firebase_credentials.json")  # Carga las credenciales de Firebase
    initialize_app(cred, {
        'databaseURL': "https://sensorsystemdb-default-rtdb.firebaseio.com/"  # URL de la base de datos de Firebase
    })
    db = firestore.client()  # Inicializa el cliente Firestore
    coleccion_datos = db.collection('datos_sensores')  # Referencia a la colección 'datos_sensores' en Firestore
except Exception as e:
    print(f"Error al inicializar Firebase: {str(e)}")  # Manejo de errores en la inicialización de Firebase

# Ruta para la página principal
@app.route('/')
def home():
    return "API for Sensor Monitoring System is Running!"  # Mensaje de estado de la API

# Ruta para manejar la solicitud de favicon
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Respuesta vacía para la solicitud de favicon

# Endpoint para recibir datos del sensor
@app.route('/api/datos', methods=['POST'])
def recibir_datos():
    try:
        # Obtener los datos enviados por el sensor
        data = request.get_json()  # Captura los datos JSON enviados en la solicitud

        # Validar que los datos no sean None
        if not data:
            raise ValueError("No se recibieron datos")  # Lanza un error si no hay datos

        # Validar que todos los campos requeridos están presentes
        campos_requeridos = ['idsensor', 'fecha', 'hora', 'pm25', 'pm10', 'co2', 'co', 'voc']
        for campo in campos_requeridos:
            if campo not in data:
                raise ValueError(f"Falta el campo requerido: {campo}")  # Lanza un error si falta algún campo

        # Extraer los campos
        idsensor = data.get('idsensor')
        fecha = data.get('fecha')
        hora = data.get('hora')
        pm25 = data.get('pm25')
        pm10 = data.get('pm10')
        co2 = data.get('co2')
        co = data.get('co')
        voc = data.get('voc')

        # Crear un documento con los datos
        nuevo_dato = {
            "fecha": fecha,
            "hora": hora,
            "idsensor": idsensor,
            "pm25": pm25,
            "pm10": pm10,
            "co2": co2,
            "co": co,
            "voc": voc,
            "timestamp": datetime.datetime.now()  # Marca de tiempo de la recepción
        }

        # Guardar los datos en Firebase
        coleccion_datos.add(nuevo_dato)  # Agrega el nuevo documento a la colección

        return jsonify({"mensaje": "Datos recibidos y almacenados correctamente"}), 200  # Respuesta de éxito

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400  # Respuesta de error si falta algún campo
    except Exception as e:
        print(f"Error inesperado: {str(e)}")  # Manejo de errores inesperados
        return jsonify({"error": "Ocurrió un error inesperado"}), 500  # Respuesta de error general

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Inicia la aplicación en modo debug
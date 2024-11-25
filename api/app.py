from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import datetime

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configurar Firebase con el archivo de credenciales
cred = credentials.Certificate("api/firebase_credentials.json")  # Asegúrate de que esta ruta sea correcta
initialize_app(cred)
db = firestore.client()
coleccion_datos = db.collection('datos_sensores')

# Ruta para la página principal
@app.route('/')
def home():
    return "API for Sensor Monitoring System is Running!"

# Ruta para manejar la solicitud de favicon
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Endpoint para recibir datos del sensor
@app.route('/api/datos', methods=['POST'])
def recibir_datos():
    try:
        # Obtener los datos enviados por el sensor
        data = request.get_json()

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
            "timestamp": datetime.datetime.now()
        }

        # Guardar los datos en Firebase
        coleccion_datos.add(nuevo_dato)

        return jsonify({"mensaje": "Datos recibidos y almacenados correctamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

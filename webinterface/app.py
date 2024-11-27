from flask import Flask, render_template, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import os
import datetime

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta del archivo de credenciales
cred_path = os.path.join(os.path.dirname(__file__), "../api/firebase_credentials.json")

# Verificar si la ruta existe
if not os.path.exists(cred_path):
    raise FileNotFoundError(f"No se pudo encontrar el archivo de credenciales en la ruta: {cred_path}")

# Configurar Firebase con el archivo de credenciales
cred = credentials.Certificate(cred_path)
initialize_app(cred)
db = firestore.client()
coleccion_datos = db.collection('datos_sensores')

# Ruta para la página principal (Home)
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para consultar los datos
@app.route('/api/consultar', methods=['GET'])
def consultar_datos():
    try:
        # Obtener parámetros de la solicitud (sensor_id y fecha)
        sensor_id = request.args.get('sensor_id')
        fecha = request.args.get('fecha')

        # Verificar que los parámetros no sean nulos
        if not sensor_id or not fecha:
            return jsonify({"error": "Faltan parámetros: sensor_id y/o fecha"}), 400

        # Imprimir parámetros para depuración
        print(f"Parámetros recibidos: sensor_id={sensor_id}, fecha={fecha}")

        # Consulta en Firestore
        query = coleccion_datos.where("idsensor", "==", sensor_id).where("fecha", "==", fecha)
        resultados = query.stream()

        # Preparar los datos para la respuesta
        datos = [doc.to_dict() for doc in resultados]

        # Manejo de resultados vacíos
        if not datos:
            return jsonify({"mensaje": "No se encontraron datos para el sensor y la fecha proporcionados"}), 200

        return jsonify(datos), 200

    except Exception as e:
        print(f"Error al consultar datos: {str(e)}")
        return jsonify({"error": str(e)}), 400

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

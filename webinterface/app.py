from flask import Flask, render_template, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import datetime

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configurar Firebase con el archivo de credenciales (asegúrate de apuntar al archivo correcto)
cred = credentials.Certificate("../api/firebase_credentials.json")  # Ajusta la ruta según sea necesario
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

        # Consulta en Firestore
        query = coleccion_datos.where("idsensor", "==", sensor_id).where("fecha", "==", fecha)
        resultados = query.stream()

        # Preparar los datos para la respuesta
        datos = []
        for doc in resultados:
            datos.append(doc.to_dict())

        return jsonify(datos), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

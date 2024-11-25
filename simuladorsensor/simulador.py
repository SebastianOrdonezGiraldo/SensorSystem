import requests
import random
import time
import datetime

# URL de la API
url = "http://127.0.0.1:5001/api/datos"

# Generar y enviar datos periódicamente
while True:
    # Datos aleatorios para simular lecturas de los sensores
    idsensor = "SOG0181"
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    pm25 = round(random.uniform(5, 150), 2)  # Genera un valor entre 5 y 150 (µg/m³)
    pm10 = round(random.uniform(10, 200), 2)  # Genera un valor entre 10 y 200 (µg/m³)
    co2 = round(random.uniform(400, 2000), 2)  # Genera un valor entre 400 y 2000 (ppm)
    co = round(random.uniform(0, 10), 2)       # Genera un valor entre 0 y 10 (ppm)
    voc = round(random.uniform(0, 500), 2)     # Genera un valor entre 0 y 500 (ppm)

    # Crear un diccionario con los datos simulados
    data = {
        "idsensor": idsensor,
        "fecha": fecha,
        "hora": hora,
        "pm25": pm25,
        "pm10": pm10,
        "co2": co2,
        "co": co,
        "voc": voc
    }

    try:
        # Enviar datos a la API mediante POST
        response = requests.post(url, json=data)
        print(f"Datos enviados: {data}, Respuesta del servidor: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar datos: {e}")

    # Esperar unos segundos antes de enviar el próximo dato
    time.sleep(5)

# Código Fuente Comentado

Este documento proporciona una descripción detallada del código fuente del sistema de monitoreo de sensores de calidad del aire. Cada componente del sistema está descrito con comentarios para facilitar la comprensión de su funcionamiento.

## 1. simuladorSensor/simulador.py

Este script es responsable de simular datos de calidad del aire y enviarlos a la API.

### Código Comentado
```python
import requests
import random
import time
import datetime

# URL de la API que recibe los datos
url = "http://127.0.0.1:5001/api/datos"

# Generar y enviar datos de los sensores periódicamente
while True:
    # Datos aleatorios para simular lecturas de los sensores
    idsensor = "SOG0181"
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")  # Obtener la fecha actual
    hora = datetime.datetime.now().strftime("%H:%M:%S")  # Obtener la hora actual
    pm25 = round(random.uniform(5, 150), 2)  # Genera un valor aleatorio para PM2.5 (µg/m³)
    pm10 = round(random.uniform(10, 200), 2)  # Genera un valor aleatorio para PM10 (µg/m³)
    co2 = round(random.uniform(400, 2000), 2)  # Genera un valor aleatorio para CO2 (ppm)
    co = round(random.uniform(0, 10), 2)  # Genera un valor aleatorio para CO (ppm)
    voc = round(random.uniform(0, 500), 2)  # Genera un valor aleatorio para VOC (ppm)

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

    # Enviar los datos a la API mediante una solicitud POST
    try:
        response = requests.post(url, json=data)
        print(f"Datos enviados: {data}, Respuesta del servidor: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar datos: {e}")

    # Esperar 5 segundos antes de enviar el próximo dato
    time.sleep(5)

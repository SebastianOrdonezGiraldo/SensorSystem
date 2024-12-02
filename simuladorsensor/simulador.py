import requests  # Importa la biblioteca para hacer solicitudes HTTP
import random  # Importa la biblioteca para generar números aleatorios
import time  # Importa la biblioteca para manejar el tiempo
import datetime  # Importa la biblioteca para trabajar con fechas y horas

# URL de la API donde se enviarán los datos
url = "http://127.0.0.1:5000/api/datos"

# Bucle infinito para enviar datos periódicamente
while True:
    # Datos aleatorios para simular lecturas de los sensores
    idsensor = "JDHH1012"  # Identificador del sensor
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")  # Obtiene la fecha actual en formato YYYY-MM-DD
    hora = datetime.datetime.now().strftime("%H:%M:%S")  # Obtiene la hora actual en formato HH:MM:SS

    # Genera valores aleatorios para diferentes contaminantes
    pm25 = round(random.uniform(5, 150), 2)  # PM2.5: valor entre 5 y 150 µg/m³
    pm10 = round(random.uniform(10, 200), 2)  # PM10: valor entre 10 y 200 µg/m³
    co2 = round(random.uniform(400, 2000), 2)  # CO2: valor entre 400 y 2000 ppm
    co = round(random.uniform(0, 10), 2)  # CO: valor entre 0 y 10 ppm
    voc = round(random.uniform(0, 500), 2)  # VOC: valor entre 0 y 500 ppm

    # Crear un diccionario con los datos simulados
    data = {
        "idsensor": idsensor,
        "fecha": fecha,
        "hora": hora,
        "pm25": pm25,
        "pm10": pm10,
        "co2": co2,
        "co": co,  #
        "voc": voc
    }

    try:
        # Enviar datos a la API mediante una solicitud POST
        response = requests.post(url, json=data)

        # Imprimir información de respuesta para depurar
        if response.status_code == 200:  # Si la respuesta es exitosa (código 200)
            print(f"Datos enviados correctamente: {data}, Respuesta del servidor: {response.status_code}")
        else:  # Si hubo un error en el envío
            print(f"Error al enviar datos. Código de estado: {response.status_code}, Respuesta: {response.text}")

    except Exception as e:  # Manejo de excepciones en caso de error
        print(f"Error al enviar datos: {e}")

    # Esperar 5 segundos antes de enviar el próximo dato
    time.sleep(10)
# Sistema de Monitoreo de Sensores de Calidad del Aire

Este proyecto es un sistema de monitoreo que simula, captura, almacena y visualiza datos de calidad del aire en tiempo real. Está diseñado para evaluar los niveles de varios contaminantes dentro de una fábrica, proporcionando información clave sobre la calidad del ambiente laboral.

## Características principales
- **Simulación de Sensores**: Genera datos en tiempo real para PM2.5, PM10, CO2, CO y VOC, permitiendo evaluar la calidad del aire de forma continua.
- **API RESTful**: Desarrollada con Flask para recibir, almacenar en Firebase Firestore y permitir consultas de los datos capturados.
- **Visualización Web**: Interfaz web amigable que permite a los usuarios consultar los datos en tablas y gráficos interactivos, mejorando la interpretación de la calidad del aire.
- **Almacenamiento en Firebase Firestore**: Base de datos NoSQL utilizada para el almacenamiento seguro y escalable de los datos simulados.

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación principal.
- **Flask**: Framework para la creación de la API y la interfaz web.
- **Firebase Firestore**: Base de datos NoSQL para almacenar los datos de los sensores.
- **Bootstrap**: Utilizado para estilizar la interfaz web y mejorar la experiencia del usuario.
- **Plotly**: Para la creación de gráficos interactivos.

## Instalación y Ejecución

### Prerrequisitos
- **Python 3.x**: Asegúrate de tener Python instalado. Puedes descargarlo desde [Python.org](https://www.python.org/downloads/).
- **Firebase Admin SDK**: Necesitas un archivo de credenciales de Firebase para conectarte a Firestore.

### Instrucciones

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/TuUsuario/SensorMonitoringSystem.git
   cd SensorMonitoringSystem
   ```

2. **Crear un Entorno Virtual e Instalar Dependencias**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   pip install -r api/requirements.txt
   ```

3. **Configurar Firebase**
   - Coloca el archivo de credenciales de Firebase (`firebase_credentials.json`) en la carpeta `api/`.

4. **Ejecutar la API**
   ```bash
   cd webinterface
   python app.py
   ```
   La aplicación estará disponible en [http://127.0.0.1:5001](http://127.0.0.1:5001).

5. **Ejecutar el Simulador de Sensores**
   En otra terminal, ejecuta el simulador para generar datos:
   ```bash
   cd simuladorSensor
   python simulador.py
   ```

## Uso
1. **Abrir la Interfaz Web**: Dirígete a [http://127.0.0.1:5001](http://127.0.0.1:5001).
2. **Consultar Datos del Sensor**: Ingresa el ID del sensor y selecciona la fecha deseada para consultar los datos disponibles.
3. **Visualizar Datos**: Los datos se muestran en una tabla y en gráficos interactivos para facilitar la interpretación.

## Descripción de los Datos
- **PM2.5**: Concentración de partículas finas (menores a 2.5 micras), medida en µg/m³.
- **PM10**: Concentración de partículas menores a 10 micras, medida en µg/m³.
- **CO2**: Nivel de dióxido de carbono en ppm (partes por millón).
- **CO**: Nivel de monóxido de carbono en ppm, un gas tóxico a niveles elevados.
- **VOC**: Compuestos orgánicos volátiles, medidos en ppm.

## Contribuir
Las contribuciones son bienvenidas. Puedes colaborar con mejoras en el código, optimización de la interfaz, o agregando nuevas funcionalidades. Por favor, abre un *issue* o envía un *pull request* para discutir cualquier cambio importante antes de hacerlos.

## Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, revisa el archivo [LICENSE](LICENSE).

## Contacto
Si tienes preguntas o sugerencias, por favor contacta al desarrollador a través de [tu_email@example.com](mailto:tu_email@example.com).


# Informe Técnico

## 1. Descripción General

El sistema de monitoreo de sensores de calidad del aire es un proyecto diseñado para simular, capturar, almacenar y visualizar datos de calidad del aire en tiempo real dentro de un entorno industrial. El propósito del sistema es ofrecer información útil sobre los niveles de contaminantes en el aire para garantizar un ambiente seguro.

## 2. Arquitectura del Sistema

El sistema está compuesto por los siguientes módulos:

- **Simulador de Sensores**: Genera datos aleatorios de calidad del aire (PM2.5, PM10, CO2, CO, VOC).
- **API Flask**: Recibe los datos del simulador y los almacena en Firebase Firestore.
- **Base de Datos (Firebase Firestore)**: Almacena los datos de los sensores de manera segura y eficiente.
- **Interfaz Web**: Permite a los usuarios consultar los datos almacenados, visualizar tendencias y analizar los valores históricos.

## 3. Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Flask**: Framework para el desarrollo de la API y la interfaz web.
- **Firebase Firestore**: Base de datos NoSQL para almacenar los datos de los sensores.
- **Bootstrap**: Utilizado para mejorar la apariencia y experiencia de la interfaz web.
- **JavaScript y Plotly**: Para la generación de gráficos interactivos.

## 4. Flujo de Datos

1. **Simulación**: El script `simulador.py` genera datos aleatorios cada 5 segundos.
2. **Envío de Datos**: Los datos se envían a la API desarrollada en Flask.
3. **Almacenamiento**: La API almacena los datos en Firestore.
4. **Visualización**: La interfaz web permite a los usuarios ver los datos en tablas y gráficos.

function consultarDatos() {
    const sensorId = document.getElementById('sensor-id').value;
    const fecha = document.getElementById('fecha').value;

    fetch(`/api/consultar?sensor_id=${sensorId}&fecha=${fecha}`)
    .then(response => response.json())
    .then(data => {
        // Mostrar datos en una tabla
        let html = "<table class='table table-bordered'><thead class='thead-dark'><tr><th>Fecha</th><th>Hora</th><th>PM2.5</th><th>PM10</th><th>CO2</th><th>CO</th><th>VOC</th></tr></thead><tbody>";
        data.forEach(row => {
            html += `<tr><td>${row.fecha}</td><td>${row.hora}</td><td>${row.pm25}</td><td>${row.pm10}</td><td>${row.co2}</td><td>${row.co}</td><td>${row.voc}</td></tr>`;
        });
        html += "</tbody></table>";
        document.getElementById('tabla-datos').innerHTML = html;

        // Crear gráfico con Plotly
        const valoresPM25 = data.map(d => d.pm25);
        const horas = data.map(d => d.hora);

        const graficoData = [
            {
                x: horas,
                y: valoresPM25,
                type: 'scatter',
                mode: 'lines+markers',
                marker: { color: 'red' },
                name: 'PM2.5'
            }
        ];

        const layout = {
            title: 'Concentración de PM2.5 durante el Día',
            xaxis: { title: 'Hora' },
            yaxis: { title: 'Concentración (µg/m³)' },
            margin: { t: 40 }
        };

        Plotly.newPlot('grafico', graficoData, layout);
    })
    .catch(error => console.error('Error al consultar los datos:', error));
}

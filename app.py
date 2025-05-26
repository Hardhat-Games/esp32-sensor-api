from flask import Flask, request, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return 'API Activa'

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # Asegúrate de que los datos se reciban correctamente
    if not data:
        return jsonify({'error': 'No se recibieron datos'}), 400

    # Crea el archivo CSV si no existe
    file_exists = os.path.isfile('datos.csv')
    with open('datos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['fecha', 'temperatura', 'humedad', 'sensor'])

        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            data.get('temperatura'),
            data.get('humedad'),
            data.get('sensor')
        ])

    return jsonify({'message': 'Datos recibidos correctamente'}), 200

from flask import Flask, request, jsonify
from database import init_db, insert_sensor_data

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return 'API Activa'

@app.route('/datos', methods=['POST'])
def recibir_datos():
    try:
        data = request.get_json()
        insert_sensor_data(
            sensor_id=data.get('sensor_id', 'esp32'),
            temperatura=data.get('temperatura', 0),
            humedad=data.get('humedad', 0),
            humedad_suelo=data.get('humedad_suelo', 0),
            presion=data.get('presion', 0),
            acelerometro=str(data.get('acelerometro', {})),
            giroscopio=str(data.get('giroscopio', {})),
        )
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

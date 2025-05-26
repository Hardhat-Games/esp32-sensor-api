import os
import psycopg2
from urllib.parse import urlparse

# Obtener URL de conexión desde variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

def connect():
    result = urlparse(DATABASE_URL)
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port

    return psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=hostname,
        port=port
    )

def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sensor_id TEXT,
            temperatura REAL,
            humedad REAL,
            humedad_suelo REAL,
            presion REAL,
            acelerometro TEXT,
            giroscopio TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_sensor_data(sensor_id, temperatura, humedad, humedad_suelo, presion, acelerometro, giroscopio):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_data (sensor_id, temperatura, humedad, humedad_suelo, presion, acelerometro, giroscopio)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (sensor_id, temperatura, humedad, humedad_suelo, presion, acelerometro, giroscopio))
    conn.commit()
    conn.close()

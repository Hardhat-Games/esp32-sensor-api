import sqlite3

DB_NAME = "sensors.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
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
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_data (sensor_id, temperatura, humedad, humedad_suelo, presion, acelerometro, giroscopio)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (sensor_id, temperatura, humedad, humedad_suelo, presion, acelerometro, giroscopio))
    conn.commit()
    conn.close()

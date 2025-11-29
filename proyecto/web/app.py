import os
import mysql.connector
from flask import Flask, render_template_string, url_for

app = Flask(__name__)


DB_HOST = os.environ.get("DATABASE_HOST")
DB_NAME = os.environ.get("DATABASE_NAME")
DB_USER = os.environ.get("DATABASE_USER")
DB_PASS = os.environ.get("DATABASE_PASS")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/')
def index():
    status_msg = "Conexión correcta a la BD"
    logs = []
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT hora, actividad, estado, imagen FROM log;')
        logs = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        status_msg = f"Error de conexión: {e}"

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sistema LOG</title>
        <style>
            body { font-family: sans-serif; text-align: center; padding: 20px; }
            table { margin: 0 auto; border-collapse: collapse; width: 80%; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
            .logo { width: 150px; margin-bottom: 20px; }
            .status { color: green; font-weight: bold; margin-bottom: 20px;}
        </style>
    </head>
    <body>
        <img src="/static/img/logo.jpg" class="logo" alt="Logo">
        
        <div class="status">""" + status_msg + """</div>

        <h2>Tabla de Logs</h2>
        <table>
            <tr>
                <th>Hora</th>
                <th>Actividad</th>
                <th>Estado</th>
                <th>Imagen Ref</th>
            </tr>
            {% for row in logs %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td><img src="/static/img/{{ row[3] }}" width="50"></td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, logs=logs)

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
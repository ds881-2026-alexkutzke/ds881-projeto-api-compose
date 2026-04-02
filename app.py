from flask import Flask, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

# Conexão com o banco de dados via variáveis de ambiente
def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DB_HOST', 'db'),
                database=os.environ.get('DB_NAME', 'app_db'),
                user=os.environ.get('DB_USER', 'app_user'),
                password=os.environ.get('DB_PASSWORD', 'app_pass')
            )
            return conn
        except psycopg2.Error:
            retries -= 1
            time.sleep(2)
    raise Exception("Falha ao conectar no banco de dados.")

@app.route('/')
def index():
    return "API Python rodando em modo de desenvolvimento!"

@app.route('/init')
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS logs (id SERIAL PRIMARY KEY, mensagem VARCHAR(100));')
    conn.commit()
    cur.close()
    conn.close()
    return "Tabela 'logs' criada com sucesso!"

@app.route('/registrar')
def registrar():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO logs (mensagem) VALUES ('Novo acesso registrado!');")
    conn.commit()
    cur.execute('SELECT COUNT(*) FROM logs;')
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"status": "sucesso", "total_registros": count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

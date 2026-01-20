import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_db_connection():
    try:
        DATABASE_URL = os.environ.get('DATABASE_URL')
        if DATABASE_URL:
            conn = psycopg2.connect(DATABASE_URL)
        else:
            conn = psycopg2.connect(
                dbname="portfolio_db",
                user="postgres",
                password="TU_CONTRASEÑA_LOCAL", 
                host="localhost",
                port="5432"
            )
        return conn
    except Exception as e:
        print("Error conectando a la DB:", e)
        return None


@app.route('/')
def home():
   
    return send_from_directory('.', 'index.html')


@app.route('/style.css')
def style():
 
    return send_from_directory('.', 'style.css')


@app.route('/experience')
def experience():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = """
            SELECT id, company, role, description, is_current, 
                   start_date::text, end_date::text 
            FROM experience 
            ORDER BY start_date DESC;
        """
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(results)
    return jsonify([])

@app.route('/projects')
def projects():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM projects;"
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(results)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="portfolio_db",
            user="postgres",
            password="Asmerald12.",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error conectando a la DB", e)
        return None
    
@app.route('/')
def home():
    return "<h1>Bienvenido a la API de mi Portafolio</h1><p>Prueba ir a <a href='/experience'>/experience</a> o <a href='/projects'>/projects</a></p>"


@app.route('/experience')
def experience():
    conn = get_db_connection()
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

@app.route('/projects')
def projects():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    query = "SELECT * FROM projects;"
    
    cur.execute(query)
    results = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
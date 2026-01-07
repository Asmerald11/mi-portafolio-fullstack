import psycopg2
import json
from datetime import date, datetime
from psycopg2.extras import RealDictCursor

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

conn = psycopg2.connect(
    dbname = 'portfolio_db',
    user = 'postgres',
    password = 'Asmerald12.',
    host = 'localhost',
    port = '5432'
)

cur = conn.cursor()

cur.execute('SELECT * FROM experience;')

datos = cur.fetchall()

json_datos = json.dumps(datos, default=json_serial, indent=4)

print(datos)

conn.close()
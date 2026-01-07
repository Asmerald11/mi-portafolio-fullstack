import psycopg2

print("--- INICIANDO LIMPIEZA DE DATOS ---")

try:
    conn = psycopg2.connect(
        dbname="portfolio_db",
        user="postgres",
        password="Asmerald12.", # <--- ¡PON TU CONTRASEÑA AQUÍ!
        host="localhost",
        port="5432"
    )
    conn.set_client_encoding('UTF8') # Forzamos la conexión limpia
    cur = conn.cursor()

    # 1. Borrón y cuenta nueva
    print("Borrando datos corruptos...")
    cur.execute("TRUNCATE TABLE experience RESTART IDENTITY;")
    cur.execute("TRUNCATE TABLE projects RESTART IDENTITY;")

    # 2. Insertar datos limpios (UTF-8 nativo de Python)
    print("Insertando datos limpios...")
    
    # Experiencia
    sql_experience = """
    INSERT INTO experience (company, role, start_date, end_date, description, is_current)
    VALUES
        ('Tech Solutions Inc.', 'Junior Web Developer', '2023-03-01', '2024-01-15', 'Desarrollo de landing pages y colaboración UX/UI.', FALSE),
        ('Freelance', 'Web Designer', '2022-06-01', '2023-02-28', 'Diseño de sitios web para comercios locales.', FALSE),
        ('StartUp Dinámica', 'Full Stack Developer', '2024-02-01', NULL, 'Desarrollo de microservicios con Python.', TRUE);
    """
    cur.execute(sql_experience)

    # Proyectos
    sql_projects = """
    INSERT INTO projects (name, description, tech_stack, repo_url)
    VALUES
        ('Task Master', 'App de tareas con login.', 'React, Node.js', 'https://github.com/test/task'),
        ('Clima App', 'Dashboard de clima.', 'JS, HTML, API', 'https://github.com/test/clima');
    """
    cur.execute(sql_projects)

    # 3. Guardar cambios
    conn.commit() 
    print("¡ÉXITO! Base de datos reparada y limpia.")

    conn.close()

except Exception as e:
    print("Error:", e)
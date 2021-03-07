import sqlite3

# crear una conexion
def crear_conexion():
    try:
        conn = sqlite3.connect('blogdb.db')
        return conn
    except:
        print("Error al conectar a la db")
        # crear un cursor

def crear_tablas(cursor):
    query = """
    CREATE TABLE post (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        contenido TEXT );
    """
    cursor.execute(query)

def listar_posts(cursor):
    try:
        query = """
        SELECT id, titulo, autor, contenido FROM post;
        """
        cursor.execute(query)
        posts = cursor.fetchall()
        return posts
    except:
        crear_tablas(cursor)
        return []


def crear_post(cursor,titulo, autor, contenido):
    query = """
    INSERT INTO post (titulo, autor, contenido) values (?, ?, ?);
    """
    cursor.execute(query, (titulo, autor, contenido))



def getPostById(cursor,id):
    query="""
    select id, titulo, autor, contenido from post where id = ?
    """
    cursor.execute(query,(id,))
    post = cursor.fetchone()
    return post


def borrar_post(cursor,id):
    query="""
    delete from post where id = ?
    """
    cursor.execute(query,(id,))


# ejecutamos instrucciones sql

# hacer permanentes los cambios o revokarlos

# cerrar la conexion
def cerrar_conexion(conn, cursor):
    cursor.close()
    conn.close()
from flask import Flask,render_template, url_for, request, redirect
import sqlite3
from contextodb import *

app = Flask(__name__)


# post = crear_post(cursor, "Mi Segundo post","Yo mismo","Lorem Ipsum bla bla bla")
# conn.commit()


@app.route("/")
def index():
    
    conn = crear_conexion()
    cursor = conn.cursor()
    posts = listar_posts(cursor)
    # conn.close()
    # cursor.close()
    return render_template("postlist.html", posts=posts)

@app.route('/post/create', methods=["GET","POST"])
def create_post():
    if request.method == "POST":
        titulo = request.form['title']
        autor = request.form['autor']
        contenido = request.form['contenido']
        conn = crear_conexion()
        cursor = conn.cursor()
        crear_post(cursor,titulo, autor,contenido)
        conn.commit()
        # conn.close()
        # cursor.close()
        return redirect(url_for('index'))
    else:
        return render_template('postform.html')


def cerrar_conexion():
    cursor.close()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)
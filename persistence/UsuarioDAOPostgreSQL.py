import psycopg2

from model.Usuario import Usuario
from config import db_config_postgre as db_config
from persistence.IUsuarioDAO import IUsuarioDAO


class UsuarioDAOPostgreSQL(IUsuarioDAO):
    def __init__(self):
       self.connection=None

    def open_connection(self):
        new_connection = psycopg2.connect(
            host=db_config.DB_HOST,
            port=db_config.DB_PORT,
            database=db_config.DB_NAME,
            user=db_config.DB_USER,
            password=db_config.DB_PASSWORD)
        self.connection=new_connection

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()

    def create(self, usuario):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, fecha_inicio, salario) VALUES (%s, %s, %s)",
                       (usuario.nombre, usuario.fecha_inicio.strftime("%Y-%m-%d"), usuario.salario))
        self.connection.commit()
        cursor.close()

    def read_one(self):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM usuarios ORDER BY id LIMIT 1 ")
        row = cursor.fetchone()
        usuario = Usuario(row[0], row[1], row[2], row[3])
        cursor.close()
        return usuario

    def read_all(self):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        usuarios = [Usuario(row[0], row[1], row[2], row[3]) for row in rows]
        cursor.close()
        return usuarios

    def update(self, usuario):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE usuarios SET "
            f"nombre='{usuario.nombre}', "
            f"fecha_inicio='{usuario.fecha_inicio.strftime('%Y-%m-%d')}', "
            f"salario='{usuario.salario}'"
            f" WHERE id={usuario.id}")
        self.connection.commit()
        cursor.close()

    def delete(self, usuario):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        cursor.execute(
            f"DELETE FROM usuarios WHERE id={usuario.id}")
        self.connection.commit()
        cursor.close()
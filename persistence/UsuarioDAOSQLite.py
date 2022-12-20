from datetime import datetime
import sqlite3

from model.Usuario import Usuario
from config import db_config_sqlite as db_config
from persistence.IUsuarioDAO import IUsuarioDAO


class UsuarioDAOSQLite(IUsuarioDAO):
    def __init__(self):
       self.connection=None

    def open_connection(self):
        self.connection = sqlite3.connect(db_config.DB_NAME)

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()

    def create(self, usuario):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        sql = f"INSERT INTO usuarios (nombre, fecha_inicio, salario) VALUES " \
              f"('{usuario.nombre}', '{usuario.fecha_inicio.strftime('%Y-%m-%d')}', {usuario.salario})"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def read_one(self):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        sql="SELECT * FROM usuarios ORDER BY id LIMIT 1 "
        cursor.execute(sql)
        row = cursor.fetchone()
        usuario = Usuario(row[0], row[1], datetime.strptime(row[2],'%Y-%m-%d'), row[3])
        cursor.close()
        return usuario

    def read_all(self):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        sql="SELECT * FROM usuarios"
        cursor.execute(sql)
        rows = cursor.fetchall()
        usuarios = [Usuario(row[0], row[1], datetime.strptime(row[2],'%Y-%m-%d'), row[3]) for row in rows]
        cursor.close()
        return usuarios

    def update(self, usuario):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        sql=f"UPDATE usuarios SET " \
            f"nombre='{usuario.nombre}', " \
            f"fecha_inicio='{usuario.fecha_inicio.strftime('%Y-%m-%d')}', " \
            f"salario='{usuario.salario}'" \
            f" WHERE id={usuario.id}"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def delete(self, usuario):
        if self.connection is None:
            raise Exception("No hay conexión con la base de datos")
        cursor = self.connection.cursor()
        sql=f"DELETE FROM usuarios WHERE id={usuario.id}"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()
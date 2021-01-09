import mysql.connector
from mysql.connector import Error

class DAO():
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = '3306',
                user = 'root',
                password = '',
                db = 'despachos'
            )
        except Error as ex:
            print("Error al intentar la conxexion: {0}".format(ex))

    def listarDespachos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM despacho")
                despachos = cursor.fetchall()
                return despachos
            except Error as ex:
                print("Error al intentar la conxexion: {0}".format(ex))

    
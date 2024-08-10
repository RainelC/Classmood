from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import gridfs


def conexion_db():

    load_dotenv()

    # Obtener la URI de MongoDB desde la variable de entorno
    uri = os.getenv("MONGODB_URI")
    # Conectándose al servidor
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Confirmando la conexión
    try:
        client.admin.command('ping')
        print("Conectado!")
    except Exception as e:
        print(e)


    # Seleccionar la base de datos
    db = client['students-db']

    # Seleccionar la colección
    collection = db['students']


    # Crear un objeto GridFs
    fs = gridfs.GridFS(db)

    return db, fs, collection


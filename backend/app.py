from flask import Flask
from flask_cors import CORS
import os
from api import create_api
from config import Config
from utils.setup import init_database, init_directories
<<<<<<< HEAD
=======
from db_sqlite import close_connection
>>>>>>> dev

app = Flask(__name__)
CORS(app) # Cors para habilitar interacción con el navegador web

# Configuración de archivo de Base de Datos JSON
app.config.from_object(Config)
init_directories()
init_database()
# -----------------------------------------------

create_api(app)

<<<<<<< HEAD
=======
@app.teardown_appcontext
def teardown_db(exception):  # Cerrar conexión a la base de datos al finalizar la petición
    close_connection(exception)

>>>>>>> dev
# Ruta de prueba
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

    # Modo Producción
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
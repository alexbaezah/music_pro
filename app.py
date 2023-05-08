from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from controllers.region import region_bp


app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://MUSICPRO:1234@localhost:1521/XE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la instancia de SQLAlchemy
db.init_app(app)

# Registrar el blueprint de la región
app.register_blueprint(region_bp)

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_bootstrap import Bootstrap

#blueprint
from .mi_blueprint import mi_blueprint
from app.productos import productos
from app.clientes import clientes
#Creacion y configuracion 
app = Flask(__name__)
app.config.from_object(Config) 
bootstrap = Bootstrap(app)

#resgistro de blueprints
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)
app.register_blueprint(clientes)

#crear los objetos de SQLAlchemy y migrate
db = SQLAlchemy(app)
migrate = Migrate(app ,
                  db)

from .models import Producto, Cliente, Venta

@app.route('/prueba')
def prueba():
    return render_template("prueba.html")
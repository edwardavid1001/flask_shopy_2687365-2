from flask import Blueprint

#crear y configurar el blueprint
mi_blueprint =Blueprint('mi_blueprint',
                        __name__, 
                        url_prefix = '/ejemplo' )

#crear ruta del blueprint
@mi_blueprint.route('/saludo')
def saludo():
    return 'por que esta tomando vive100'

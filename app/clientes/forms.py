from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired


class ClienteForm(FlaskForm):
    username = StringField('Ingrese su nombre de usuario: ',validators=[InputRequired(message="se requiere el nombre del cliente ")])
    email = StringField('Ingrese su correo: ',validators=[InputRequired(message="se require un email")])
    password = StringField('Ingrese su contraseña: ',validators=[InputRequired(message="se requiere la contraseña")])
    submit = SubmitField('Registrar')



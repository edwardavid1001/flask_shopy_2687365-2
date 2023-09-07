from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange

class ProductForm():
    username = StringField('ingrese producto:' ,
                         validators= [InputRequired(message="nombre requerido")])
    precio = IntegerField("ingrese precio" , validators=[
                                                    InputRequired(message="precio requerido"),
                                                    NumberRange(message="precio inválido",
                                                                min = 10000 ,
                                                                max = 100000)
                                                    ])
class NewProductForm(FlaskForm, ProductForm):
    imagen =FileField(validators=[FileRequired(
                                       message="debe ingresar un archivo"
                                       ),
                                  FileAllowed(['jpg' , 'png'],
                                                    message="solo se admiten imagenes"
                                                 ) ],
                      label ="ingrese imagen del producto:",
                     )
    submit = SubmitField("Registrar")

class EditProductForm(FlaskForm,ProductForm):
         submit = SubmitField("Registrar")
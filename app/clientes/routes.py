from . import clientes
from flask import render_template, redirect, flash
from .forms import ClienteForm

import app


@clientes.route("/crearCliente", methods = ["GET", "POST"])
def crearCliente():
    c = app.models.Cliente()
    form=ClienteForm()
    if form.validate_on_submit():
        #? El Formulario Va A Llenar El Nuevo Objeto Cliente Automaticamente
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()


        flash("Cliente registrado")
        #?Retorna Cliente Registrado
        return redirect('/clientes/listarCliente')
    return render_template("newCliente.html", form=form)

@clientes.route('/listarCliente')
def listar():
    #? Traer Productos De La Base De Datos
    clientes= app.Cliente.query.all()
    #? Mostrar La Vista De Listar Enviandole Los Productos Seleccionados
    return render_template('listarCliente.html', clientes= clientes)

@clientes.route('/editarCliente/<cliente_id>', methods =('GET','POST'))
def editar(cliente_id):
    #Seleccionar el producto con el id
    p=app.models.Cliente.query.get(cliente_id)
    #Cargo el formulario con los atributos del producto
    form_edit=ClienteForm(obj= p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Cliente editado exitosamente")
        return redirect("/clientes/listarCliente")
    return render_template('newCliente.html', form=form_edit)


@clientes.route('/eliminar/<cliente_id>', methods =('GET','POST'))
def eliminar(cliente_id):
    #Seleccionar el producto a eliminar
    p=app.models.Cliente.query.get(cliente_id)
    #Eliminar el producto
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Cliente eliminado correctamente")
    return redirect("/clientes/listarCliente")
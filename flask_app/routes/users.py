from flask import render_template, url_for, request, redirect

from flask_app import app
from flask_app.db import db
from flask_app.ent import UserBO
from flask_app.forms import UserEditionForm, UserCreationForm


@app.route("/users")
def show_users():
    users = UserBO.query.all()
    return render_template('users/users.html', users=users)


@app.route('/user/create', methods=['POST', 'GET'])
def create_user():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            user = UserBO(name=form.name.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()

        return redirect(url_for('show_users'))

    return render_template('users/create.html', form=UserCreationForm())


@app.route('/user/delete/<user_id>')
def delete_user(user_id):
    user = UserBO.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('show_users'))


@app.route('/user/update/<user_id>')
def update_user(user_id):
    user = UserBO.query.filter_by(id=user_id).first()
    if user is None:
        return redirect(url_for('show_users'))

    form = UserEditionForm()
    form.name.data = user.name
    form.id.data = user_id
    return render_template('users/update.html', form=form, user_id=user_id)


@app.route('/user/update/action/<user_id>', methods=['POST'])
def update_user_action(user_id):
    user = UserBO.query.filter_by(id=user_id).first()
    form = UserEditionForm()
    user.name = form.name.data

    db.session.commit()

    return redirect(url_for('show_users'))

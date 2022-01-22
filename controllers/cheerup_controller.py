from flask import Blueprint, request, session, redirect, render_template
from models.cheerup import delete_cheer, get_all_cheerups, insert_cheerup, get_cheer, update_cheer


cheerup_controller = Blueprint(
    "cheerup_controller", __name__, template_folder="../templates/cheerup")


@cheerup_controller.route('/cheerups')
def cheers():
    cheerups = get_all_cheerups()
    return render_template('cheerups.html', cheerups=cheerups)


@cheerup_controller.route('/cheerups/create')
def create():
    if not session.get('user_id'):
        return redirect('/login')
    return render_template('create.html')


@cheerup_controller.route('/cheerups', methods=["POST"])
def insert():
    if not session.get('user_id'):
        return redirect('login')

    user_id = session.get('user_id')
    insert_cheerup(request.form.get("body"),
                   user_id)

    return redirect('/')


@cheerup_controller.route('/cheerups/<id>')
def show(id):
    cheer = get_cheer(id)
    return render_template('show.html', cheer=cheer)


@cheerup_controller.route('/cheerups/<id>/edit')
def edit(id):
    if not session.get('user_id'):
        return redirect('/login')
    cheer = get_cheer(id)
    return render_template('edit.html', cheer=cheer)


@cheerup_controller.route('/cheerups/<id>', methods=["POST"])
def update(id):
    if not session.get('user_id'):
        return redirect('/login')
    body = request.form.get("body")
    user_id = session.get('user_id')

    # UPDATE
    update_cheer(id, body, user_id)

    return redirect('/')


@cheerup_controller.route('/cheerups/<id>/delete', methods=["POST"])
def delete(id):
    if not session.get('user_id'):
        return redirect('/login')
    delete_cheer(id)
    return redirect('/')

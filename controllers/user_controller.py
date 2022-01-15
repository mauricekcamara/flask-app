from flask import Blueprint, request, redirect, render_template
from models.user import insert_user
import bcrypt

user_controller = Blueprint(
    "user_controller", __name__, template_folder="../templates/users")


@user_controller.route('/signup')
def signup():
    return render_template('signup.html')


@user_controller.route('/users', methods=["POST"])
def create_user():
    password = request.form.get("password")
    hashed_password = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode()
    insert_user(
        request.form.get("name"),
        request.form.get("email"),
        hashed_password
    )

    return redirect('/login')
